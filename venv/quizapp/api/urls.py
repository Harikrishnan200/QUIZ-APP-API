from django.contrib import admin
from django.urls import path
from exam_app.views import TestView
from auth_app.views import RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TestView.as_view(), name='test'),

    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]


