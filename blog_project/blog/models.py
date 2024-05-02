from django.db import models
import uuid

from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

# Create your models here.

class Type(models.Model):
    """Model representing a blog type."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a blog type (e.g. News, food, travel etc.)"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('type-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='type_name_case_insensitive_unique',
                violation_error_message = "Type already exists (case insensitive match)"
            ),
        ]

class Blog(models.Model):
    """Model representing a blog."""
    title = models.CharField(max_length=200)
    post_date = models.DateField()
    blogger = models.ForeignKey('Blogger', on_delete=models.RESTRICT, null=True)

    content = models.TextField(
        max_length=2000, help_text="Enter the content of the blog")

    type = models.ForeignKey(Type, on_delete=models.RESTRICT, null=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular blog across whole website")

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])

class Blogger(models.Model):
    """Model representing an blogger."""
    name = models.CharField(max_length=100)
    bio = models.TextField(
        max_length=1000, help_text="Enter the bio of the blogger", default='')

    def get_absolute_url(self):
        """Returns the URL to access a particular blogger instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'
