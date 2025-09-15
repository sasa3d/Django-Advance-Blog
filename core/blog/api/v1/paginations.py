from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# class BlogPostPagination(PageNumberPagination): #todo Default Pagination
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class CustomBlogPostPagination(PageNumberPagination):
    page_size = 4
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'Total_Objects': self.page.paginator.count,
            'Total_Pages': self.page.paginator.num_pages,
            'results': data
        })