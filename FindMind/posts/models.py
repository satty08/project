from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
        'posts:single',
        kwargs={
        'username':self.user.username,
        'pk':self.pk
        }
        )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
