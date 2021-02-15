from django.contrib import admin
from .models import Users, Tokens, Books, Notes, Bookmarks

class CommonIdShow(admin.ModelAdmin):
    readonly_fields=("id",)
    

# Register your models here.
admin.site.register(Users, CommonIdShow)
admin.site.register(Tokens, CommonIdShow)
admin.site.register(Books, CommonIdShow)
admin.site.register(Notes, CommonIdShow)
admin.site.register(Bookmarks, CommonIdShow)