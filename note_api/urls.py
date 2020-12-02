from django.urls import path, include
from rest_framework.routers import DefaultRouter

from note_api.views import NoteVieSet

app_name = 'note'

router = DefaultRouter()

router.register('note', NoteVieSet, basename='note')

urlpatterns = [
    path('', include(router.urls))
]