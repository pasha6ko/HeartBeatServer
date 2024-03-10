from django.urls import path
from . import views

urlpatterns = [
    path("createprofile/", views.CreateProfileView.as_view(), name="createprofile"),
    path("profileinteraction/", views.ProfileInteractionView.as_view(), name="profileinteraction"),
]

