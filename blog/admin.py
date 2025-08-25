# blog/admin.py
from django.contrib import admin
from .models import Post  # убедись, что Post есть в models.py

admin.site.register(Post)
