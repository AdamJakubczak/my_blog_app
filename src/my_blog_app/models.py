from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=150)
    post_content = models.TextField(null=False)
    post_date = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
