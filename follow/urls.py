from django.urls import path
from .views import FollowToggleView, FollowerCountView

urlpatterns = [
    path('follow-unfollow/<int:user_id>/', FollowToggleView.as_view(), name='follow-unfollow'),
    path('followers/<int:user_id>/', FollowerCountView.as_view(), name='follower-count'),
]
