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
    
    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)
    
    # category = serializers.SlugRelatedField(
    #     queryset=Category.objects.all(),
    #     slug_field='name', many=False
    # )

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
    

        """
        Overwrites the to_representation method of the ModelSerializer to include the 
        of the post in the representation. The  is obtained by calling the 
        method of the Post model.
        Args:
            instance (Post): The Post instance to be serialized.
        Returns:
            dict: The serialized representation of the Post instance.
            "برای مجزا کردن داده ها در خروجی
        (زمانیکه یک تک آیتم بهت میدم یک چیز نمایش بده و زمانیکه یک لیست بهت میدم یک چیز دیگه ای بهم نمایش بده)
          """
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')#در صورتی که لیست ارسال شود
        if request.parser_context.get('kwargs').get('pk'):#در صورتی که تک آیتم ارسال شود
            rep.pop('abslt_url', None)
            rep.pop('reltv_url', None)
            rep.pop('absolute_url', None)
            rep.pop('snippet', None)
        else:
             rep.pop('content', None)#در صورتی که لیست ارسال شود

        rep['category'] = CategorySerializer(instance.category).data
        rep.pop('snippet', None)  # Remove 'snippet' field if it exists
        return rep
            

   