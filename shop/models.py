from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify




class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name='url')
    image = models.ImageField(upload_to='category/icon/', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class SubCategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name='url')
    category = models.ForeignKey(to=CategoryModel, on_delete=models.CASCADE, related_name='subcategories', verbose_name='Категория')

    class Meta:
        db_table = 'sub_category'
        verbose_name = 'Под категория'
        verbose_name_plural = 'Под категории'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name='url')
    category = models.ForeignKey(to=SubCategoryModel, on_delete=models.CASCADE, verbose_name='Категория')
    short_description = models.CharField(max_length=500, verbose_name='Короткое описание')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def sell_price(self):
        if self.discount:
            return round(self.price - (self.discount * self.price / 100), 2)
        return self.price


class ProductImageModel(models.Model):
    product = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE, related_name='images', verbose_name='Продукты')
    image = models.ImageField(upload_to='product/image/', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'
        ordering = ('-id',)
    
    def __str__(self):
        return f'фото - {self.pk}, продукт {self.product.name}'

    def clean(self):
        if self.product.images.count() >= 5:
            raise ValidationError('Максиму 5 изображений')
