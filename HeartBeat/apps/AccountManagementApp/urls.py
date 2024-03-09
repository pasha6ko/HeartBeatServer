from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.RegisterView.as_view(), name="signup"),
    path('signin/', views.SighInView.as_view(), name='signin'),
]

