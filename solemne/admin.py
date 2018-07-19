from django.contrib import admin
from solemne.models import Brand, Category, Product

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','sort_order','status','created_at','updated_at')
    #list_filter = ('owner','active')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku','name','price','brand','category','status','created_at','updated_at',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
