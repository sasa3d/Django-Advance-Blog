from django.template import response
from django.test import TestCase , SimpleTestCase
from django.urls import reverse, resolve
from .views import indexView, PostListView


# from core.blog.views import RedirectToMaktab
# Create your tests here.

# class TestUrl(TestCase):
class TestUrl(SimpleTestCase):

    # def test_blog_fbv_index_url_resolve(self):   اگر fbv بود:
    #     url = reverse("blog:fbv-index")
    #     self.assertEquals(resolve(url).func, RedirectToMaktab)

    def test_blog_cbv_index_url_resolve1(self):   # اگر cbv بود:   
        url = reverse("blog:cbv-index")
        self.assertEqual(resolve(url).func.view_class, indexView)  # test: OK
    
    # def test_blog_cbv_index_url_resolve2(self):  # test: FAILED
    #         url = reverse("blog:cbv-index")
    #         self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_post_list_url(self):
        response = self.client.get("/blog/post/")
        self.assertEqual(response.status_code, 302)

    def test_post_detail_url(self):
        # Assuming you have a post with pk=1 for testing
        response = self.client.get("/blog/post/1/")
        self.assertEqual(response.status_code, 302)

    def test_post_create_url(self):
        response = self.client.get("/blog/post/create/")
        print("status:", response.status_code)
        print("redirect to:", response.headers.get("Location"))

        self.assertEqual(response.status_code, 302)

    def test_post_edit_url(self):
        # Assuming you have a post with pk=1 for testing
        response = self.client.get("/blog/post/1/edit/")
        self.assertEqual(response.status_code, 302)

    def test_post_delete_url(self):
        # Assuming you have a post with pk=1 for testing
        response = self.client.get("/blog/post/1/delete/")
        self.assertEqual(response.status_code, 302)
    
