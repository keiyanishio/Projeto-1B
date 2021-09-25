from django.db import models



class Tag(models.Model):
    texto=models.TextField(null=True)

    def __str__(self):
        return  f'{self.texto}'


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    tags = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        #ID. TITULO
        return f'{self.id}. {self.title}'

