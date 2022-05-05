from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.title} from {self.year}'
