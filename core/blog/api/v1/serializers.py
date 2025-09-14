from rest_framework import serializers
from ...models import Post , Category # noqa: F401

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
        # read_only_fields = ['content']
        
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
            

   