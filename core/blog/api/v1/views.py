from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly , IsAdminUser  # noqa: F401
from rest_framework.response import Response
from .serializers import PostSerializer  #  noqa: F401 
""" منظور همین فولدر که در فایل serializers.py هستش"""

from ...models import Post  # noqa: E402, F401
""" منظور همین فولدر که در فایل models.py 
هستش و ارجاع به سه فولدرهای تو در توی بالاتر"""

from rest_framework import status  # noqa: E402, F401
from django.shortcuts import get_object_or_404  # noqa: E402, F401

"""
@api_view(["GET","POST"])
def postList(request):
    if request.method == "GET": 
    .
    .
    .
    Handles the requests to list all posts or create a new post.

    GET:
        Retrieves a list of all posts with status=True.
        Returns serialized data of the posts.

    POST:
        Creates a new post with the provided data.
        Validates the data using PostSerializer.
        Saves the post if the data is valid and returns the serialized data.
        Returns an error response if the data is invalid.
    """
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
#@permission_classes([IsAuthenticatedOrReadOnly])# Only authenticated users can access this view  قرار بگیرد وگرنه کار نمیکند @api_view(["GET","POST"])و حتما باید بعداز 
def postList(request):
    if request.method == "GET": 
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True) 
        """ 
        many=True means that we have more than one object
        for example, if we have 10 posts, we need to set many=True
        because we have 10 posts and we want to serialize all of them.
        """
    
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        


"""
@api_view(["GET","PUT","DELETE"])
Handles the API requests to update or remove a post by its ID.
Args:
    GET: retrieves the post with the given ID.
    PUT: update or editing the post with the provided data and the given ID.
    DELETE: deletes the post with the given ID.
"""
@api_view(["GET","PUT","DELETE"])
def postDetail(request,id):
    """
    Handles the request to get a post by its ID.
    Args:
        request: The HTTP request object.
        pk: The primary key of the post.
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
