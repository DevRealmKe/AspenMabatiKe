from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(HomeDetail)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','slug')
    prepopulated_fields={'slug':('category_name',)}

admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','createdat')
    prepopulated_fields={'slug':('product_name',)}


admin.site.register(Product,ProductAdmin)

admin.site.register(Gallery)
