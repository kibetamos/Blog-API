from django.urls import URLPattern, path
from .views import PostList, PostDetail

URLPattern=[
    path('<int:pk/', PostDetail.as_view()),
    path('', PostList.as_view()),
]