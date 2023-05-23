from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=20)
    book_price = models.IntegerField()
    book_desc = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.book_name

def upload_to(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class Collection(models.Model):
    book_one = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, related_name='book_one')
    book_two = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, related_name='book_two')
    image_url = models.ImageField(upload_to="images", blank=True, null=True)
    
