from django.shortcuts import render
from rest_framework import viewsets

from note_api import serializers
from note_api.models import Note


class NoteVieSet(viewsets.ModelViewSet):
    serializer_class = serializers.NoteSerializer
    queryset = Note.objects.all()
