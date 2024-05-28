from rest_framework.urls import path
from .views import LikeCreateView, CommentCreateView

urlpatterns = [
    path("like-dislike/<int:pk>/", LikeCreateView.as_view()),
    path('comment/<int:pk>/', CommentCreateView.as_view()),
]