from django.urls import path

from . import views

urlpatterns = [
    path('post/<slug:pk>/', views.BlogDetailView.as_view(),name='post_detail'),
    path('', views.BlogListView.as_view(),name='home'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(),name='post_edit'),

]
