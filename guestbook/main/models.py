from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    postTitle = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    pw = models.CharField(max_length=15, default="password")
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"name : { self.name } , title: {self.postTitle}, content: {self.content[:10]}"

class Reply(models.Model):
    posting = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=30)
    pw = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)
    reply = models.TextField()


class User(models.Model):
    user_id = models.CharField(max_length=30, unique=True, verbose_name="유저 아이디")
    user_pw = models.CharField(max_length=120, unique=True, verbose_name="유저 비밀번호")
    user_name = models.CharField(max_length=30, unique=True, verbose_name="유저 이름")
    user_email = models.EmailField(max_length=120, unique=True, verbose_name="유저 이메일")
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="계정 생성 시간")

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'