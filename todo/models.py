from django.db import models


CHOICES_STATUS = [
    ("todo", "TODO"),
    ("doing", "DOING"),
    ("done", "DONE"),
]
class Todo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    status = models.CharField(max_length=10, choices=CHOICES_STATUS)
    created_at = models.TimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    