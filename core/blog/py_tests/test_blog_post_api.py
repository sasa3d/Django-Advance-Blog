# from django.template import response
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
import pytest 


@pytest.mark.django_db
class TestBlogPostAPI:
    client = APIClient()
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
        
    def test_create_post_response_401_status(self):
        """ This test is for api post request in pytest 
        این تست برای بررسی وضعیت پاسخ درخواست پست API در pytest است. """
        # client = APIClient()
        url = reverse("blog:api-v1:post-list")
        data_test= {
            'title' : 'test',
            'content' : 'describe for me' ,
            'status' : True ,
            'published_date' : timezone.now()
        }
        response = self.client.post(url, data=data_test)
        assert response.status_code == 401