from django.db import models
from django.contrib.auth.models import User

# 📝 Blog Post Model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']   # default: latest first

    def __str__(self):
        return self.title


# 📩 Contact Form Model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']   # latest contact messages first

    def __str__(self):
        return f"{self.name} ({self.email})"
