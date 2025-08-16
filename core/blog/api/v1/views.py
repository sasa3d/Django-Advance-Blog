from rest_framework.decorators import api_view , permission_classes  # noqa: F401
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly , IsAdminUser  # noqa: F401
from rest_framework.response import Response
from .serializers import PostSerializer  #  noqa: F401 
""" منظور همین فولدر که در فایل serializers.py هستش"""

from rest_framework.views import APIView  # noqa: E402, F401

from rest_framework.generics import GenericAPIView  # noqa: E402  
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin  # noqa: E402, F401


from ...models import Post  # noqa: E402, F401
""" منظور همین فولدر که در فایل models.py 
هستش و ارجاع به سه فولدرهای تو در توی بالاتر"""

from rest_framework import status  # noqa: E402, F401
from django.shortcuts import get_object_or_404  # noqa: E402, F401


    
class PostListView(GenericAPIView , ListModelMixin, CreateModelMixin):
    """Handles the requests to retrieve a list of posts and create a new post."""

    permission_classes = [IsAuthenticatedOrReadOnly]  # noqa: F811
    serializer_class = PostSerializer
    
    def get_queryset(self): #qs
        return Post.objects.filter(status=True)

    def get(self, request, *args , **kwargs):
        """Handles the request to retrieve a list of posts."""
        # posts = Post.objects.filter(status=True)
        # qs = self.get_queryset()
        # serializer = self.serializer_class(qs, many=True)
        # return Response(serializer.data)
        return self.list(request, *args , **kwargs)
    

   
    def post(self, request, *args, **kwargs):
        """Handles the request to create a new post."""
        # serializer = self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.create(request, *args, **kwargs)

@api_view(["GET","PUT","DELETE"])
def PostDetail(request,id):
    
    """
    Handles the request to get a post by its ID.
    Args:
    GET: retrieves the post with the given ID.
    PUT: update or editing the post with the provided data and the given ID.
    DELETE: deletes the post with the given ID.
    
    """

    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
      
    return Response({"Details": "Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)

'''
 class PostDetail(APIView):
    """Handles the requests to retrieve, update, or delete a specific post and
    provides the functionality to get a post by its ID, update it, or delete it by its ID 
    and status=True and returns the serialized data of the post or a success message upon deletion.
    getting details of a post and edit plus removing that post.
   
    Returns:
        : Response: Serialized data of the post or a success message upon deletion.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]  # noqa: F811
    serializer_class = PostSerializer
    
    def get(self,request,id):
        """
        Retrieves a specific post by its ID.
        """
        post = get_object_or_404(Post,pk=id , status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
        
        
    def put(self,request,id):
        """
        Edits a specific post by its ID.
        """
        
        post = get_object_or_404(Post,pk=id , status=True)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)  
     
    def delete(self,request,id):
        """
        Deletes a specific post by its ID.
        """
        post = get_object_or_404(Post,pk=id , status=True)
        post.delete()
        return Response({"Details": "Item removed successfully"}, 
                        status=status.HTTP_204_NO_CONTENT)
 '''



