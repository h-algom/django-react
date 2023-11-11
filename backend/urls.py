from django.contrib import admin
from django.urls import path
from core.message import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/messages/", views.message_list, name='message_list')
]
