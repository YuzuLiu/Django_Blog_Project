from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
]

urlpatterns += [
    path('blog/<int:pk>/create', views.CreateComment.as_view(), name='create-comment'),
]

urlpatterns += [
    path('signup/', views.user_signup, name='signup'),
]