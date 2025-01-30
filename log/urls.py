from django.urls import path
from . import views


app_name = "log"


urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.show, name="show"),
    path("<int:pk>/edit", views.edit, name="edit"),
    path("<int:pk>/update", views.update, name="update"),
    path("<int:pk>/delete", views.delete, name="delete"),
    path("search/", views.board_search, name="search"),
    path("add_favorite/", views.add_favorite, name="add_favorite"),
    path("remove_favorite/", views.remove_favorite, name="remove_favorite"),
]
