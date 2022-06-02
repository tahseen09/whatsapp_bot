from django.urls import path
from hadith.views import receive_message, message_status


urlpatterns = [
    path("delivery", message_status, name="delivery"),
    path("", receive_message, name="message"),
]
