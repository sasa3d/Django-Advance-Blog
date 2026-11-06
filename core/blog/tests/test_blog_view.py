from datetime import datetime

from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import User,Profile
from blog.models import Post, Category


class TestBlogViews(TestCase):
    """ this class is used to test the views of the blog app. 
    این کلاس برای تست ویوهای اپلیکیشن بلاگ استفاده می‌شود. 
    """
    
    def setUp(self):
        """ Set up the test client for making requests. 
        این متد برای راه‌اندازی کلاینت تست برای ارسال درخواست‌ها استفاده می‌شود. 
        """
        self.client = Client()
        
          # Create a Post instance
        self.user = User.objects.create_user(email="test@example.com", password="testpassword")
        self.profile=Profile.objects.create(
        user=self.user,
        first_name="Test", 
        last_name="User" ,
        description= "Test user description")  
        
        self.post = Post.objects.create(
                author=self.profile ,
                title="Test Post",
                content="This is a test post content.",
                status=True,
                category=None,  # You can set this to a valid Category instance if needed
                published_date=datetime.now(),
            )
        
        
    def test_blog_index_url_response_200(self):
        """ Test the blog index URL response.
        این متد برای تست پاسخ URL صفحه اصلی بلاگ استفاده می‌شود. 
        """
        url=reverse('blog:cbv-index')
        response= self.client.get(url) 
         # response = self.client.get(reverse('blog:index')) ترکیب همون دوخط بالا
        
        self.assertEqual(response.status_code, 200)
        
    def test_blog_index_url_response_successfull(self):
            """ Test the blog index URL response is successful.
            این متد برای تست موفقیت‌آمیز بودن پاسخ URL صفحه اصلی بلاگ استفاده می‌شود.
            """
            url=reverse('blog:cbv-index')
            response= self.client.get(url) 
             # response = self.client.get(reverse('blog:cbv-index')) ترکیب همون دوخط بالا
            
            self.assertEqual(response.status_code, 200)
            self.assertTrue(str(response.content).find("index") )
            self.assertTrue(str(response.content).find("cbv") )
            self.assertTrue(str(response.content).find("saber") )
            # self.assertTemplateUsed(response,template_name="index.html")
               
        

    def test_blog_home_view(self):
        """ Test the blog home view.
        این متد برای تست ویو صفحه اصلی بلاگ استفاده می‌شود. 
        """
        url=reverse('blog:cbv-index')
        response= self.client.get(url) 
        # response = self.client.get(reverse('blog:index')) ترکیب همون دوخط بالا
       
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,template_name="index.html")
        
    # def test_blog_post_detail_logged_in_response(self):
    #     pass
    
    def test_blog_post_detail_anonymouse_response(self) :
        response = self.client.get(
            reverse("blog:post-detail", kwargs={"pk": self.post.pk})
)
        # print("Redirects to:", response.get("Location"))
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(
        response.status_code,
        302,
        f"Redirected to: {response.headers.get('Location')}",
)
    
    def test_blog_post_detail_anonymous_response(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.pk})
        response = self.client.get(url)

        self.assertRedirects(
            response,
            f"/accounts/login/?next={url}",
            fetch_redirect_response=False,
        )


    # def test_blog_list_view(self):
    #     """ Test the blog list view.
    #     این متد برای تست ویو لیست بلاگ استفاده می‌شود. 
    #     """
    #     response = self.client.get(reverse('blog:blog-list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/blog_list.html')

    # def test_blog_detail_view(self):
    #     """ Test the blog detail view.
    #     این متد برای تست ویو جزئیات بلاگ استفاده می‌شود. 
    #     """
    #     # Create a sample post for testing
    #     from ..models import Post, Category
    #     from accounts.models import Profile, User
    #     user = User.objects.create_user(email="", password="testpassword")
    #     profile = Profile.objects.create(user=user)
