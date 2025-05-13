from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def postList(request):
    """
    Handles the request to print OK.
    """
    return Response("OK")

data={
    "id":7,
    "title":"SaberSASA_SORNA of title",    
    "content":"saber_Modirian of content",
    }

@api_view()
def postDetail(request, pk):
    """
    Handles the request to get a post by its ID.
    Args:
        request: The HTTP request object.
        pk: The primary key of the post.
    """
    return  Response(data)
    #return Response("Post ID: {}".format(pk))