
from django.urls import path 
from . import views

urlpatterns = [
    path("",views.index, name="home"),
    path("edit/<str:pk>/",views.editing, name="edit"),
    path("msg/<str:pk>/", views.msg, name='msg'),
    # path("msgs/", views.error_404_view, name='err')
]

