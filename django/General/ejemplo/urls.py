from django.urls import path

from . import views

app_name = "ejemplo"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pregunta_id>/", views.detail, name="detail"),
    path("<int:pregunta_id>/results/", views.results, name="results"),
    path("<int:pregunta_id>/vote/", views.vote, name="vote"),
]