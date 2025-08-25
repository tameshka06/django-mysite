from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignUpForm, PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})


def blog_list(request):
    return render(request, "blog/blog_list.html")




def create_blog(request):
    return render(request, "blog/create_blog.html")


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # привязываем автора
            post.save()
            return redirect("post_list")  # редиректим на список постов
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # пока не подтвердил email
            user.save()

            # отправка письма
            send_mail(
                "Подтверждение регистрации",
                "Привет! Подтверди email для активации аккаунта.",
                settings.DEFAULT_FROM_EMAIL,
                [form.cleaned_data["email"]],
                fail_silently=False,
            )
            return render(request, "registration/confirm_email.html")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
