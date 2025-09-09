from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for easier navigation
    list_filter = ('author', 'publication_year')
    
    # Enable search by title or author
    search_fields = ('title', 'author')