from django.contrib import admin

from .models import Post

@admin.register(Post)


class postModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','images']

# Register your models here.


