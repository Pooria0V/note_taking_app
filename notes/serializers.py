from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'text', 'updated_time']
        extra_kwargs = {
            'user': {'read_only': True}
        }
