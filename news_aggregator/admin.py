from django.contrib import admin
from .models import NewsSource, Category, NewsArticle

@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'category', 'published_at', 'is_active']
    list_filter = ['source', 'category', 'is_active', 'published_at']
    search_fields = ['title', 'content']
    readonly_fields = ['scraped_at']