from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def postlist(request):
    """
    Handles the request to list all posts.
    """
    return Response("OK")