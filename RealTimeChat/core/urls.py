from django.contrib.auth.views import LogoutView

from django.urls import path
from . import views 

urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('signup/',views.signup,name='signup'),
    path('logout/',LogoutView.as_view(),name='logout'),
]