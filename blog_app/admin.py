from django.contrib import admin
from blog_app.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    #fields = ('title','published_date')
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content')
    #ordering = ['-created_date']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
