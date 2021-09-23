from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)


    def __str__(self):
        #ID. TITULO
        return f'{self.id}. {self.title}'

