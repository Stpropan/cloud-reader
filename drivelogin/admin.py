from django.contrib import admin
from .models import Users, Tokens, Books, Notes, Bookmarks

# Register your models here.
admin.site.register(Users)
admin.site.register(Tokens)
admin.site.register(Books)
admin.site.register(Notes)
admin.site.register(Bookmarks)