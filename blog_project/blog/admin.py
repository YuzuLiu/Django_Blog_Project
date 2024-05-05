from django.contrib import admin
from .models import Blog, Blogger, Type, Comment

# Define the admin class
class BloggerAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('title', 'blogger', 'post_date', 'type')
    list_filter=('type', 'post_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('blog', 'author', 'date_time', 'description')
    list_filter=('date_time',)

# Register your models here.
admin.site.register(Blogger, BloggerAdmin)
admin.site.register(Type)