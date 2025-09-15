from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly , IsAdminUser  # noqa: F401
from rest_framework.response import Response  # noqa: F401
from .serializers import PostSerializer   , CategorySerializer
""" منظور همین فولدر که در فایل serializers.py هستش"""

from ...models import Post, Category # noqa: E402
""" منظور همین فولدر که در فایل models.py هستش و ارجاع به سه فولدرهای تو در توی بالاتر"""

from rest_framework import status  # noqa: E402, F401
from django.shortcuts import get_object_or_404  # noqa: E402, F401

from rest_framework.generics import  ListCreateAPIView  , RetrieveUpdateDestroyAPIView  # noqa: E402
from rest_framework.viewsets import ViewSet , ModelViewSet  # noqa: E402, F401
from .permissions import IsOwnerOrReadOnly  # noqa: E402, F401
from django_filters.rest_framework import DjangoFilterBackend  # noqa: E402
from rest_framework.filters import SearchFilter


# class PostListView(GenericAPIView , ListModelMixin, CreateModelMixin):
class PostListView(ListCreateAPIView):

    """Handles the requests to retrieve a list of posts and create a new post."""

    permission_classes = [IsAuthenticatedOrReadOnly]  # noqa: F811
    serializer_class = PostSerializer
    
    def get_queryset(self): #qs
        return Post.objects.filter(status=True)



class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # noqa: F811
    serializer_class = PostSerializer
    # queryset = Post.objects.filter(status=True)
    def get_queryset(self): #== queryset = Post.objects.filter(status=True)
        return Post.objects.filter(status=True) 
    lookup_field = 'id'
    

# Example for ViewSet in CBV : 
# class PostViewSet(ViewSet): 
class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True) #todo == def get_queryset(self):   return Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend , SearchFilter] 
    filterset_fields = ['category','author','status'] 
    search_fields = ['title','content']                                         
    

class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    
    
    
    # def retrieve(self, request, pk=None):
    #     #queryset = self.get_queryset()
    #     post_object = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer_class(post_object)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # def update(self, request, pk=None):
    #     post_object = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer_class(post_object, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def partial_update(self, request, pk=None):
    #     post_object = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer_class(post_object, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     post_object = get_object_or_404(self.queryset, pk=pk)
    #     post_object.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    