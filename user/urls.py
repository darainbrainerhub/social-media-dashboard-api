from django.urls import path
from .views import RegisterView, LoginView, UserDetailsView
from .searchview import SearchUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('detail/', UserDetailsView.as_view(), name='user'),
    path('search/', SearchUserView.as_view(), name='search'),
    # path('test/', TestView.as_view(), name='test'),
]
