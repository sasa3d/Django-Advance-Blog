from rest_framework import serializers
from ...models import Post , Category # noqa: F401
from accounts.models import Profile # noqa: F401

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# class PostSerializer(serializers.Serializer): # نام کلاس == Serializerاسم مدل + کلمه ی 
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
 
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    reltv_url = serializers.ReadOnlyField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    abslt_url = serializers.HyperlinkedIdentityField(
        view_name='blog:api-v1:post-detail', read_only=True)
    
  
    class Meta:
        model = Post
        # fields = '__all__'  # This will include all fields in the model:        # fields = ['id', 'title', 'content', 'status', 'created_at', 'updated_at', 'publish_date', 'author', 'category']
        fields = ['id', 'title','image','content','snippet' , 'status',
                  'reltv_url','absolute_url', 'abslt_url',
                  'created_date', 'updated_date', 'published_date',
                  'author', 'category']
        read_only_fields = ['author']
        
    def get_abs_url(self, obj):
        request = self.context.get('request') # گرفتن شی(object) ریکوئست از کانتکست
        if request is None:
            return None
        # return request.build_absolute_uri(obj.get_absolute_api_url())
        return request.build_absolute_uri(obj) , request.build_absolute_uri(obj.pk)

    def get_abslt_url(self, obj):
        return obj.get_absolute_api_url()
    

    def to_representation(self, instance):
        """ برای مجزا کردن داده ها در خروجی
        (زمانیکه یک تک آیتم بهت میدم یک چیز نمایش بده و زمانیکه یک لیست بهت میدم یک چیز دیگه ای بهم نمایش بده)
        
        This method is used to override the default to_representation method of the serializer.
        It removes the 'abslt_url', 'reltv_url', 'absolute_url', and 'snippet' fields from the response
        when a single post is requested, and the 'content' field when a list of posts is requested.
        It also adds a 'category' field to the response, which contains the serialized data of the post's category.
        """
        rep = super().to_representation(instance)
        rqst = self.context.get('request')#در صورتی که لیست ارسال شود request
        if rqst.parser_context.get('kwargs').get('pk'):#در صورتی که تک آیتم ارسال شود
            rep.pop('abslt_url', None)
            rep.pop('reltv_url', None)
            rep.pop('absolute_url', None)
            rep.pop('snippet', None)
        else:
             rep.pop('content', None)#در صورتی که لیست ارسال شود
       # TODO: check if the 'category' field exists in the response and remove it if it does
       # TODO: The line `rep['category'] = CategorySerializer(instance.category, context={'request':
       # TODO: rqst}).data` is creating a serialized representation of the category associated with the post
       # TODO: instance.
        rep['category'] = CategorySerializer(instance.category,context={'request': rqst}).data
        rep.pop('snippet', None)  # Remove 'snippet' field if it exists
        return rep
    
    def create(self , validated_data):
        """
        Create a new Post instance, automatically assigning the author based on the authenticated user.

        This method overrides the default `create` behavior to link the new `Post`
        to the `Profile` of the currently authenticated user. It's crucial for
        scenarios where the author of a post should not be explicitly sent in
        the request payload but rather derived from the session or token.

        It leverages the `request` context, accessible via `self.context.get('request')`,
        to retrieve the `User` object associated with the active session.
        From this `User`, it then fetches the corresponding `Profile` instance
        by querying `Profile.objects.get(user__id=self.context.get('request').user.id)`.
        This ensures that the 'author' field of the new `Post` is correctly
        populated with the `Profile` of the creator.

        Args:
            validated_data (dict): A dictionary containing the validated data
                                   for creating the new `Post` instance.
                                   The 'author' field, if present, will be
                                   overwritten by the current user's profile.

        Returns:
            Post: The newly created `Post` instance.

        Raises:
            django.core.exceptions.ObjectDoesNotExist: If no `Profile` is found
                                                       for the authenticated user.
            TypeError: If `self.context.get('request').user` is an `AnonymousUser`
                       or `None` (i.e., the user is not authenticated),
                       as `AnonymousUser` typically lacks an `id` attribute
                       or a corresponding `Profile`.
                       
        یک نمونه جدید Post را ایجاد می‌کند و نویسنده را بر اساس کاربر احراز هویت شده به طور خودکار اختصاص می‌دهد.

        این متد رفتار پیش‌فرض `create` را بازنویسی می‌کند تا `Post` جدید را
        به `Profile` کاربر فعلی احراز هویت شده پیوند دهد. این رویکرد برای سناریوهایی
        که نویسنده یک پست نباید صراحتاً در بدنه درخواست ارسال شود، بلکه باید
        از نشست (session) یا توکن استخراج گردد، حیاتی است.

        این متد از `context` مربوط به `request`، که از طریق `self.context.get('request')`
        قابل دسترسی است، بهره می‌برد تا شیء `User` مرتبط با نشست فعال را بازیابی کند.
        سپس، با استفاده از این `User`، نمونه `Profile` مربوطه را با کوئری
        `Profile.objects.get(user__id=self.context.get('request').user.id)`
        بازیابی می‌کند. این اطمینان را می‌دهد که فیلد 'author' `Post` جدید به درستی
        با `Profile` خالق آن پر شود.

        پارامترها:
            validated_data (dict): دیکشنری حاوی داده‌های اعتبارسنجی شده
                                   برای ایجاد نمونه جدید `Post`.
                                   فیلد 'author'، در صورت وجود، با پروفایل کاربر فعلی
                                   بازنویسی خواهد شد.

        بازگشت:
            Post: نمونه `Post` که به تازگی ایجاد شده است.

        خطاها:
            django.core.exceptions.ObjectDoesNotExist: اگر هیچ `Profile` برای
                                                       کاربر احراز هویت شده یافت نشود.
            TypeError: اگر `self.context.get('request').user` یک `AnonymousUser`
                       یا `None` باشد (یعنی کاربر احراز هویت نشده باشد)،
                       زیرا `AnonymousUser` معمولاً فاقد ویژگی `id` یا
                       `Profile` متناظر است.
        """

        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)
            

   