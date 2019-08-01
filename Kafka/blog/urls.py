from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path('', login_required(views.Home.as_view()) , name='blog-home'),


    path('user/<str:username>', login_required(views.UserPostListView.as_view()) , name='blog-user-post'),
    path('post/<int:pk>/',login_required(views.PostDetailView.as_view()), name='blog-details'),
    path('post/new/', login_required(views.PostCreateView.as_view()), name='blog-create'),
    path('post/<int:pk>/update/', login_required(views.PostUpdateView.as_view()), name='blog-update'),
    path('post/<int:pk>/delete/', login_required(views.PostDeleteView.as_view()), name='blog-delete'),
    path('about/', views.About.as_view(), name='blog-about'),

]