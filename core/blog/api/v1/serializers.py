from rest_framework import serializers
from ...models import Post , Category # noqa: F401

# class PostSerializer(serializers.Serializer): # نام کلاس == Serializerاسم مدل + کلمه ی 
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
    
    

class PostSerializer(serializers.ModelSerializer):
    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        # fields = '__all__'  # This will include all fields in the model:        # fields = ['id', 'title', 'content', 'status', 'created_at', 'updated_at', 'publish_date', 'author', 'category']
        fields = ['id', 'title', 'content', 'status', 'created_date', 'updated_date', 'published_date', 'author', 'category']
        read_only_fields = ['content']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']