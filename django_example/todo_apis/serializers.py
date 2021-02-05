from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'assigned_to',
                  'finished', 'created_at', 'modified_at']

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        if hasattr(self, 'initial_data'):
            unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
            print(unknown_keys)
            if unknown_keys:
                raise ValidationError("Got unknown fields: {}".format(unknown_keys))
        return attrs
