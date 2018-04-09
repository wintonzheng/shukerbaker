from django.contrib.auth.models import User
from django.db import models


class ShowCase(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True)
    subtitle = models.CharField(max_length=1024, null=True)
    content = models.TextField(null=True)
    video_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'show_case'
