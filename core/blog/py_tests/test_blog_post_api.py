# from django.template import response

from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
import pytest 


""" this decorator is used to define a fixture function that can be used in test functions."""
""" این دکوراتور برای تعریف یک تابع fixture استفاده می‌شود که می‌تواند در توابع تست استفاده شود. """
@pytest.fixture
def api_client():
    """this function is used to create an instance of the APIClient class, which is a test client provided by Django REST framework for testing API endpoints."""
    """ این تابع برای ایجاد یک نمونه از کلاس APIClient استفاده می‌شود، که یک کلاینت تست ارائه شده توسط Django REST framework برای تست نقاط پایانی API است. """
    
    clnt= APIClient()
    return clnt
    # return APIClient() معادل دوخط بالا

""" this decorator is used to mark a test class or test function as requiring access to the database. """
@pytest.mark.django_db
class TestBlogPostAPI:
    # client = APIClient()
    # @pytest.mark.parametrize("post_id, expected_status", [
    #     (1, 200),
    #     (999, 404),
    #     ("invalid", 400),
    # ])
    def test_get_blog_post_response_200_status(self, api_client):
        """this """
        # response = client.get(f"/api/blog/posts/{post_id}")
        # client = APIClient()
        # client.post('/notes/', {'title': 'new idea'}, format='json')
        url= reverse("blog:api-v1:post-list")
        # response = client.get(url)
        response = api_client.get(url)
        assert response.status_code == 200
        
    def test_create_post_response_401_status(self, api_client):
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
        
        # self.client.force_authenticate(user={})
        api_client.force_authenticate(user={})
        
        # response = self.client.post(url, data=data_test)
        response = api_client.post(url, data=data_test)
        assert response.status_code ==403