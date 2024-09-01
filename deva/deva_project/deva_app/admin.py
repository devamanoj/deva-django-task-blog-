from django.contrib import admin
from .models import Posts,Author,Comment,TagLine
# Register your models here.
admin.site.register(Posts)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(TagLine)