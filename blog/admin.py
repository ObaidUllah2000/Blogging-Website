from django.contrib import admin
from blog.models import Blog, Contact
# Register your models here.

# class BlogAdmin(admin,@admin.register()
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/main.css",)
        }
        js = ("js/test.js",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)