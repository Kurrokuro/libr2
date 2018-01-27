from django.db import models
from django.utils import timezone
# import django

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    def __str__(self):
        return '%s %s' % (self.name, self.surname)

class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    details = models.TextField(null=True)
    vote = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    cover = models.ImageField(upload_to='book_covers', null=True, blank=True)
    book_pdf = models.FileField(upload_to='pdf/%y/%m/%d', null=False, blank=False, default="")
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.cover






