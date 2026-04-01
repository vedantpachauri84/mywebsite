from django.contrib import admin
from .models import Post, Author,Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ('title','date','author')
    list_display = ('title', 'date', 'author')
    prepopulated_fields = {'intro':('title',)}
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('title','date','author')
    list_display = ('title', 'date', 'author')

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Comment)