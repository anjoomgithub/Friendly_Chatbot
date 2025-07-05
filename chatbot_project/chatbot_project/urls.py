from django.contrib import admin
from django.urls import path
from chatbot.views import chat_view, save_profile, download_report, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_view, name='chat'),
    path('save-profile/', save_profile, name='save_profile'),
    path('download-report/<int:profile_id>/', download_report, name='download_report'),
    path('profile/<int:profile_id>/', profile_view, name='profile'),
]