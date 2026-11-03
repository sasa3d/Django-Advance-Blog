from django.test import SimpleTestCase , TestCase
from ..forms import PostForm # ..forms import PostForm
from datetime import datetime
from ..models import Category, Post

from accounts.models import Profile ,User

class TestPostModel(TestCase):
    """ this class is used to test the Post model in the blog app. """
    def setUp(self):
         # Create a Post instance
                self.user = User.objects.create_user(email="test@example.com", password="testpassword")
                self.profile=Profile.objects.create(
                    user=self.user,
                    first_name="Test", 
                    last_name="User" ,
                    description= "Test user description",  
                                       )
        
    def test_post_model_creation_with_valid_data(self):
        """
        Test the creation of a Post model instance with valid data.
        """
        post = Post.objects.create(
            author=self.profile ,
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
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        