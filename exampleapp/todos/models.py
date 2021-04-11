from django.db import models

#bunlar tablolarımız ve columnlarımız

class Todo(models.Model):
    content = models.TextField()

