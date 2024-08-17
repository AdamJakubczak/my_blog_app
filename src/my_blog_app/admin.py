from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_author', 'post_date')
    search_fields = ('post_title', )
    list_filter = ('post_author', )