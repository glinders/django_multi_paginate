from django.contrib import admin

from .models import (
    Room,
    Note,
    Book,
)

admin.site.register(Room)
admin.site.register(Note)
admin.site.register(Book)
