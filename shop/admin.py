from django.contrib import admin
from shop.models import CategoryModel, SubCategoryModel, ProductModel, ProductImageModel




admin.site.register(ProductImageModel)

class ProductImageTabular(admin.TabularInline):
    model = ProductImageModel
    fields = ('image',)
    extra = 1
    max_num = 5

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name',
        'slug',
        'image',
    ]


@admin.register(SubCategoryModel)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name',
        'slug',
        'category',
    ]


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'discount', 'sell_price')
    list_filter = ('category',)
    search_fields = ('name', 'short_description')
    readonly_fields = ('slug', 'create_at')
    inlines = [ProductImageTabular,]
    fields = [
        'name',
        'slug',
        ('quantity', 'create_at'),
        ('price', 'discount'),
        'category',
        'short_description',
        'description',
    ]
