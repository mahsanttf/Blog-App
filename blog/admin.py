from django.contrib import admin
from .models import BlogAuthor, Blog, BlogComment

admin.site.register(BlogAuthor)
admin.site.register(Blog)
admin.site.register(BlogComment)
