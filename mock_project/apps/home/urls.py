from django.urls import path

from mock_project.apps.home.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
]
