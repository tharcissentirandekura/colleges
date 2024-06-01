from django.urls import path
from . import views

app_name = 'colleges'
urlpatterns = [
    path(
        '',
        views.home,
        name='home'
    ),
    path(
        'colleges/',
        views.CollegeListCreate.as_view(),
        name='create-view-create'
    ),#creatig a path for the CollegeListCreate view

    path(
        'colleges/<int:pk>/',
        views.CollegeRetrieveUpdateDestroy.as_view(),
        name='update-delete-retrieve'
    ),
]