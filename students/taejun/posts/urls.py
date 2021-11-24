from django.urls import path

from posts.views import PostView, CommentView, LikeView

urlpatterns = [
    path('', PostView.as_view()),
    path('/comment', CommentView.as_view()),
    path('/like', LikeView.as_view()),
]
