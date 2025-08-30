from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     # Fields to display in the list view
    list_display = ("title", "author", "publication_year")

    # Fields you can filter by in the sidebar
    list_filter = ("publication_year", "author")

    # Search functionality
    search_fields = ("title", "author")