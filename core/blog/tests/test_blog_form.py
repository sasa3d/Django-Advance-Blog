from django.test import SimpleTestCase , TestCase
from ..forms import PostForm # ..forms import PostForm
from datetime import datetime


class TestPostForm(SimpleTestCase):
    """
     This class is used to test the PostForm form in the blog app.
     این کلاس برای تست فرم PostForm در اپلیکیشن بلاگ استفاده می شود.   
    """
    def test_post_form_with_valid_data(self):
        """ 
        This method tests the PostForm form with valid data.
        این متد فرم PostForm را با داده های معتبر تست می کند
        .و چون داده های معتبر هستند، فرم باید معتبر باشد و is_valid() باید True برگرداند.
        """
        form = PostForm(data={
            "title": "Test Post",
            "content": "This is a test post content.",
            "status":True,
            "published_date": datetime.now(),
        })
        self.assertTrue(form.is_valid())
        
   