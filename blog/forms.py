from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже используется")
        return email


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image", "video"]  # author не пишем!

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            # Проверка размера файла
            if image.size > 5 * 1024 * 1024:  # 5MB, с запасом
                raise forms.ValidationError("Изображение слишком большое (макс. 5MB)")

            # Проверка расширения
            valid_extensions = ["jpg", "jpeg", "png"]
            ext = image.name.split(".")[-1].lower()
            if ext not in valid_extensions:
                raise forms.ValidationError("Можно загружать только JPG или PNG")

            # Проверка разрешения
            img = Image.open(image)
            max_width, max_height = 1920, 1080
            if img.width > max_width or img.height > max_height:
                # Уменьшаем пропорционально
                img.thumbnail((max_width, max_height))

                # Сохраняем в память
                output = BytesIO()
                img.save(output, format=img.format)
                output.seek(0)

                # Перезаписываем image на уменьшенный
                image = InMemoryUploadedFile(
                    output,
                    "ImageField",
                    image.name,
                    f"image/{ext}",
                    sys.getsizeof(output),
                    None,
                )
        return image

    def clean_video(self):
        video = self.cleaned_data.get("video")
        if video:
            if video.size > 10 * 1024 * 1024:  # 10MB
                raise forms.ValidationError("Видео слишком большое (макс. 10MB)")

            valid_extensions = ["mp4", "mov", "avi"]
            ext = video.name.split(".")[-1].lower()
            if ext not in valid_extensions:
                raise forms.ValidationError("Можно загружать только MP4, MOV или AVI")

        return video
