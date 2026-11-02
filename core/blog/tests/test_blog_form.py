from django.test import SimpleTestCase
from ..forms import PostForm # ..forms import PostForm
from datetime import datetime


class TestPostForm(SimpleTestCase):
    def test_post_form_with_valid_data(self):
        
        form = PostForm(data={
            "title": "Test Post",
            "content": "This is a test post content.",
            "published_date": datetime.now(),
        })
        self.assertTrue(form.is_valid(), form.errors)
        
    def test_post_form_with_empty_title(self):
        form = PostForm(data={
            "title": "",
            "content": "This is a test post content.",
            "published_date": datetime.now(),
        })
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)



    # def test_post_form_invalid_data(self):
    #     form_data = {
    #         'title': '',
    #         'content': '',
    #     }
    #     form = PostForm(data=form_data)
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('title', form.errors)
    #     self.assertIn('content', form.errors)