from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog', views.index, name='index'),
    path('blog/blogs', views.BlogsView.as_view(), name='blogs'),
    path('blog/bloggers', views.BloggersView.as_view(), name='bloggers'),
    path('blog/<int:pk>/', views.BlogsDetailView.as_view(), name='blogsdetails'),
    path('blog/blogger/<int:pk>/', views.BloggersDetailView.as_view(), name='bloggersdetails'),
    path('blog/<int:pk>/comment/', views.CommentView.as_view(), name='blog_comment'),
    path('blog/update_comment/<int:pk>/', views.CommentUpdateView.as_view(), name='update_comment'),
    path('blog/delete_comment/<int:pk>/', views.CommentDeleteView.as_view(), name='delete_comment'),
]
