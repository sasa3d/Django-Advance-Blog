# from django.template import response
from django.urls import reverse
from rest_framework.test import APIClient
import pytest 


@pytest.mark.django_db
class TestBlogPostAPI:
    # @pytest.mark.parametrize("post_id, expected_status", [
    #     (1, 200),
    #     (999, 404),
    #     ("invalid", 400),
    # ])
    def test_get_blog_post_response_200_status(self):
        # response = client.get(f"/api/blog/posts/{post_id}")
        client = APIClient()
        # client.post('/notes/', {'title': 'new idea'}, format='json')
        url= reverse("blog:api-v1:post-list")
        response = client.get(url)
        assert response.status_code == 200