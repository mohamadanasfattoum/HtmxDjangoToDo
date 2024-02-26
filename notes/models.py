from django.db import models

class Todo(models.Model):
    note = models.TextField(max_length=3000)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.note
    