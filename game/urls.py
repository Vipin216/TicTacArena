from django.urls import path
from . import views


urlpatterns = [
    path("create-room/",views.create_room,name="create_room"),
    path("room/<str:room_code>/",views.waiting_room,name="waiting_room"),
]