"""This module defines the models for this app."""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """Represents a category for books."""

    categories = (
        ('finance', 'Finance'),
        ('spiritual', 'Spiritual'),
        ('health', 'Health'),
        ('leadership', 'Leadership'),
        ('biographies', 'Biographies')
    )

    category = models.CharField(max_length=20, choices=categories)

    def __str__(self):
        """Return the string representation of the category."""
        return self.category


class Book(models.Model):
    """Book model."""

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='book_like', blank=True)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    buy_button = models.URLField(
        max_length=200, default='https://www.amazon.com/')

    class Meta:
        """Order the books by tittle."""

        ordering = ["title"]

    def __str__(self):
        """Return the string representation of the book."""
        return self.title

    def number_of_likes(self):
        """Return the number of likes for the book."""
        return self.likes.count()


class Comment(models.Model):
    """Represents a comment on a book."""

    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """Order the comments by created_on date."""
        
        ordering = ["created_on"]

    def __str__(self):
        """Return the string representation of the comment."""
        return f"Comment {self.body} by {self.name}"
