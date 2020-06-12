from django.urls import path, include
from .views import (
    HomePage,
    ProjectListView,
    SocialMediaView,
    ContactView,
    ProjectDetailView
)


app_name = 'core'


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('social-media/', SocialMediaView.as_view(), name='social-media'),
    path('contact/', ContactView.as_view(), name='contact'),
]