from django.contrib import admin
from myapp.models import Bookdb

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bookdb, AuthorAdmin)