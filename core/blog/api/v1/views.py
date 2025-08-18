from rest_framework.decorators import api_view , permission_classes  # noqa: F401
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly , IsAdminUser  # noqa: F401
from rest_framework.response import Response  # noqa: F401
from .serializers import PostSerializer   
""" منظور همین فولدر که در فایل serializers.py هستش"""

from rest_framework.views import APIView  # noqa: E402, F401

from rest_framework.generics import  ListCreateAPIView  , RetrieveUpdateDestroyAPIView  # noqa: E402
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin  # noqa: E402, F401


from ...models import Post  # noqa: E402, F401
""" منظور همین فولدر که در فایل models.py هستش و ارجاع به سه فولدرهای تو در توی بالاتر"""

from rest_framework import status  # noqa: E402, F401
from django.shortcuts import get_object_or_404  # noqa: E402, F401


    
# class PostListView(GenericAPIView , ListModelMixin, CreateModelMixin):
class PostListView(ListCreateAPIView):

    """Handles the requests to retrieve a list of posts and create a new post."""

    permission_classes = [IsAuthenticatedOrReadOnly]  # noqa: F811
    serializer_class = PostSerializer
    
    def get_queryset(self): #qs
        return Post.objects.filter(status=True)

    # def get(self, request, *args , **kwargs):
    #     """Handles the request to retrieve a list of posts."""
    #     # posts = Post.objects.filter(status=True)
    #     # qs = self.get_queryset()
    #     # serializer = self.serializer_class(qs, many=True)
    #     # return Response(serializer.data)
    #     return self.list(request, *args , **kwargs)
    

   
    # def post(self, request, *args, **kwargs):
    #     """Handles the request to create a new post."""
    #     # serializer = self.serializer_class(data=request.data)
    #     # serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     # return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return self.create(request, *args, **kwargs)



"""  class PostDetail(APIView):
    '''Handles the requests to retrieve, update, or delete a specific post and
    provides the functionality to get a post by its ID, update it, or delete it by its ID 
    and status=True and returns the serialized data of the post or a success message upon deletion.
    getting details of a post and edit plus removing that post.
   
    Returns:
        : Response: Serialized data of the post or a success message upon deletion.
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]  # noqa: F811
    serializer_class = PostSerializer
    
    def get(self,request,id):
        '''
        Retrieves a specific post by its ID.
        '''
        post = get_object_or_404(Post,pk=id , status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
        
        
    def put(self,request,id):
        '''
        Edits a specific post by its ID.
        '''
        
        post = get_object_or_404(Post,pk=id , status=True)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)  
     
    def delete(self,request,id):
        '''
        Deletes a specific post by its ID.
        '''
        post = get_object_or_404(Post,pk=id , status=True)
        post.delete()
        return Response({"Details": "Item removed successfully"}, 
                        status=status.HTTP_204_NO_CONTENT)
  """


    # class PostDetail(GenericAPIView):
    #     permission = [IsAuthenticatedOrReadOnly]
    #     serializer_class = PostSerializer
    
    # def get(self,request,id):
    #     '''
    #     Retrieves a specific post by its ID.
    #     '''
    #     post = get_object_or_404(Post,pk=id , status=True)
    #     serializer = self.serializer_class(post)
    #     return Response(serializer.data)


# class PostDetail(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
# class PostDetail(RetrieveAPIView):
# class PostDetail(RetrieveUpdateAPIView):
# class PostDetail(RetrieveDestroyAPIView):
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # noqa: F811
    serializer_class = PostSerializer
    # queryset = Post.objects.filter(status=True)
    def get_queryset(self): #== queryset = Post.objects.filter(status=True)
        return Post.objects.filter(status=True) 
    lookup_field = 'id'

    # def get(self, request, *args, **kwargs):
    #     '''
    #     Retrieves a specific post by its ID.
    #     '''
    #     return self.retrieve(request, *args, **kwargs)


    # def put(self, request, *args, **kwargs):
    #     '''
    #     Edits a specific post by its ID.
    #     '''
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     '''
    #     Deletes a specific post by its ID.
    #     '''
    #     return self.destroy(request, *args, **kwargs)
        
