from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=20)
    book_price = models.IntegerField()
    book_desc = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.book_name