from django.contrib import admin

from bookshop.models import Book, Store, Publisher, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'is_active', 'address']
