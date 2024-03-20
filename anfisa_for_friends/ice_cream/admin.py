from django.contrib import admin

# Register your models here.
from .models import Category, Topping, Wrapper, IceCream

admin.site.empty_value_display = 'Не задано'

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

admin.site.register(IceCream, IceCreamAdmin)

class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Wrapper)
admin.site.register(Topping)
