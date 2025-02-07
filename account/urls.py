from django.urls import path
from account.views import PodcastLoginView, logout_view, RegisterView


urlpatterns = [
    path("login/", PodcastLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout" ),
    path("register/", RegisterView.as_view(), name="register"),
]
