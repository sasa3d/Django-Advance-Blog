from django.test import SimpleTestCase , TestCase
from ..forms import PostForm # ..forms import PostForm
from datetime import datetime
from ..models import Category, Post

from accounts.models import Profile ,User

class TestPostModel(TestCase):
    """ this class is used to test the Post model in the blog app. """
    def test_post_model_creation_with_valid_data(self):
        """
        Test the creation of a Post model instance with valid data.
        """
        # Create a Post instance
        user = User.objects.create_user(email="test@example.com", password="testpassword")
        profile=Profile.objects.create(
            user=user,
            first_name="Test", 
            last_name="User" ,
            description= "Test user description",  
                               )
        
        post = Post.objects.create(
            author=profile ,
            title="Test Post",
            content="This is a test post content.",
            status=True,
            category=None,  # You can set this to a valid Category instance if needed
            published_date=datetime.now(),
        )

        # Check if the instance was created successfully
        self.assertIsInstance(post, Post)
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "This is a test post content.")
        self.assertTrue(post.status)