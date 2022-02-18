from django.contrib import admin

# Register your models here.
from .models import Publisher,Author,Book

admin.site.register(Publisher)
admin.site.register(Author)
# admin.site.register(Book)


@admin.register(Book)   
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date')
    ordering = ('-publication_date',)
    search_fields = ('title',)

