from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer  #  noqa: F401 
""" منظور همین فولدر که در فایل serializers.py هستش"""

from ...models import Post  # noqa: E402, F401
""" منظور همین فولدر که در فایل models.py 
هستش و ارجاع به سه فولدرهای تو در توی بالاتر"""

@api_view()
def postList(request):
    """
    Handles the request to print OK.
    """
    return Response("OK")

# data={
#     "id":7,
#     "title":"SaberSASA_SORNA of title",    
#     "content":"saber_Modirian of content",
#     }

@api_view()
def postDetail(request,id):
    """
    Handles the request to get a post by its ID.
    Args:
        request: The HTTP request object.
        pk: The primary key of the post.
    """
    
    
    post = Post.objects.get(pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)
