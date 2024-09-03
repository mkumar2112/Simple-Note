from django.urls import path
from .views import *

urlpatterns = [
    path('notes', NoteAPIView.as_view() , name='Note CRUD Operations'),
    path('notes/<id>', NoteAPIView.as_view() , name='Note RUD Operations'),
]