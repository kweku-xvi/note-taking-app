from django.urls import path
from . import views
from .views import CreateNoteView, UpdateNoteView, DeleteNoteView

urlpatterns = [
    path('', views.welcome, name='welcome-page'),
    path('home/', views.home, name='home-page'),
    path('note/create', CreateNoteView.as_view(), name='create-note'),
    path('note/<int:pk>/update/', UpdateNoteView.as_view(), name='update-note'),
    path('note/<int:pk>/delete/', DeleteNoteView.as_view(), name='delete-note'),
]