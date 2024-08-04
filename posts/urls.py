from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>',views.post_detail,name='post_detail'),
    path('home_page/', views.home_page, name='home_page')
]