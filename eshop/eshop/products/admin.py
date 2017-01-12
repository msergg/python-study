from django.contrib import admin
from .models import Product, Comment

# class CommentInline(admin.TabularInline):

class CommentInline(admin.StackedInline):
    model = Comment



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc')
    search_fields = ('name', 'desc')
    inlines = [CommentInline, ]

admin.site.register(Product, ProductAdmin)


admin.site.register(Comment)

