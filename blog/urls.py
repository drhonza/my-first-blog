from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Connect root URL of blog app to post_list view
]
