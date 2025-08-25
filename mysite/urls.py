from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Главная страница — список постов
    path("", blog_views.post_list, name="home"),
    # Блог
    path("blog/", include("blog.urls")),
    # Встроенные страницы авторизации: login, password_change и т.д.
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path(
        "accounts/password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # Регистрация
    path("accounts/signup/", blog_views.signup, name="signup"),
    # Красивый logout (будет перенаправлять на главную)
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]

# Подключаем медиа-файлы в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
