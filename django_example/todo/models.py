from django.db import models

ASSIGNED_TO = (
    ('1', 'user1'),
    ('2', 'user2'),
    ('3', 'user3'),
)


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=1, choices=ASSIGNED_TO, default='1')
    finished = models.BooleanField(default=False)
    description = models.TextField(blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
