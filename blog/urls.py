from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post-list', views.post_list, name='post_list'),
    path('post/<int:pk>/detail', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    url('cv/', views.cv_page(), name='cv_page'),
    # path('post-cv', views.blog_cv, name='blog_cv'),
]
