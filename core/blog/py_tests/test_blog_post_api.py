from django.template import response

import pytest 

class TestBlogPostAPI:
    # @pytest.mark.parametrize("post_id, expected_status", [
    #     (1, 200),
    #     (999, 404),
    #     ("invalid", 400),
    # ])
    def test_get_blog_post_response_200_status(self):
        # response = client.get(f"/api/blog/posts/{post_id}")
        assert 1==2