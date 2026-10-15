from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["status"]
    list_display = ["title", "status", "author", "published_at"]
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ["title"]
