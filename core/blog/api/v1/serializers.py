from rest_framework import serializers

class PostSerializer(serializers.Serializer): # نام کلاس == Serializerاسم مدل + کلمه ی 
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    