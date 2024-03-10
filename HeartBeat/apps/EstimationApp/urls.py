from django.urls import path
from . import views

urlpatterns = [
    path("like/", views.LikeView.as_view(), name="like"),
    path("dislike/", views.DislikeView.as_view(), name="dislike"),
]

