from django.contrib import admin

# Register your models here.


from .models import Post, Reply, User


admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(User)