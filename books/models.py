from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, allow_unicode=True)
    biography = models.TextField(blank=True)

    # for serializer
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, allow_unicode=True)

    # for serializer
    def __str__(self):
        return self.name

class BookInfo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, allow_unicode=True)
    authors = models.ManyToManyField(Author, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')
    description = models.TextField(blank=True)
    published = models.PositiveSmallIntegerField(null=True, blank=True)
    language = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='covers/%Y', blank=True)
    downloads = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    # for admin
    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=['-created']), models.Index(fields=['title'])]

class BookFile(models.Model):
    class Format(models.TextChoices):
        PDF = 'pdf', 'PDF'
        EPUB = 'epub', 'EPUB'

    book_info = models.ForeignKey(BookInfo, related_name='book_files', on_delete=models.CASCADE)
    format = models.CharField(max_length=10, choices=Format.choices)
    size = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to='books/%Y')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book_info', 'format'],
                name='unique_format_and_file'
            )
        ]