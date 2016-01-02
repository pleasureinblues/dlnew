from django.contrib import admin
from product.models import Category, ProductProfile, UserProfile, Brand, Customer_ps_contact



# Register your models here.



class ProductProfileAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'brand', 'model_name', 'processor','ram','hdd', 'price', 'category', 'condition')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}


class UserProfileAdmin(admin.ModelAdmin):
    pass

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brand_name',)}


class Customer_ps_conactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number','email','product', 'subject','message')

admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductProfile, ProductProfileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Customer_ps_contact, Customer_ps_conactAdmin)




