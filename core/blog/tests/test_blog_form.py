from django.test import SimpleTestCase , TestCase
from ..forms import PostForm # ..forms import PostForm
from datetime import datetime
from ..models import Category


class TestPostForm(TestCase):
    
    def test_post_form_with_valid_data(self):
        """
        Use TestCase and supply Category's object in PostForm test 
        """
        category_obj = Category.objects.create(name="Hello Test Category")  # Create a category object for testing
        form = PostForm(data={
            "title": "Test Post",
            "content": "This is a test post content.",
            "status":True,
            # "category":None,# حتی نباید خالی باشد
            "category": category_obj,
            "published_date": datetime.now(),
        })
        self.assertTrue(form.is_valid())
        
       
    def test_post_form_with_no_data(self):
        """
        Test PostForm with no data
        """
       
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        