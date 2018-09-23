from django.urls import path
from howdy import views


urlpatterns = [
    path(r'^$', views.HomePageView.as_view()),
]