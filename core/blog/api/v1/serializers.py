from rest_framework import serializers
from ...models import Post , Category # noqa: F401

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
    class Meta:
        model = Post
        # fields = '__all__'  # This will include all fields in the model:        # fields = ['id', 'title', 'content', 'status', 'created_at', 'updated_at', 'publish_date', 'author', 'category']
        fields = ['id', 'title', 'content','snippet' , 'status',
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
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

   