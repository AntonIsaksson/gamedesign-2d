from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import Membership
from PIL import Image
from django.contrib.contenttypes.fields import GenericRelation

CATEGORY_CHOICE = [
        ('Animated Creatures', 'Animated Creatures'),
        ('Animated Objects', 'Animated Objects'),
        ('Landscapes', 'Landscapes')
    ]

COLOR_CHOICE = [
        ('B', 'Blue'),
        ('G', 'Green'),
        ('R', 'Red'),
        ('Y', 'Yellow'),
        ('BR', 'Brown'),
        ('W', 'White'),
        ('BL', 'Black'),
        ('O', 'Other')
    ]

class Category(models.Model):

    title = models.CharField(max_length=20, choices=CATEGORY_CHOICE, default='Animated Creatures')

    def __str__(self):
        return self.title


class AllItems(models.Model):

    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text_content = models.TextField(default=None)
    color = models.CharField(max_length=30, choices=COLOR_CHOICE, default='Blue')
    image = models.ImageField( upload_to='images', blank=True, null=True)
    date_made = models.DateTimeField(default=timezone.now)
    
    class Meta:
        abstract = True


"""-------------Creature/Character Models----------------"""
class Creature(AllItems):
    
    TYPE_CHOICE = [
        ('H', 'Main Character'),
        ('E', 'Villain'),
        ('N', 'Neutral')
    ]

    allowed_memberships = models.ManyToManyField(Membership)
    character_type = models.CharField(max_length=30, choices=TYPE_CHOICE, default='Neutral')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('creature:detail', kwargs={'title': self.title})



"""-------------Object Models----------------"""
class Object(AllItems):

    TYPE_CHOICE = [
        ('V', 'Vegetation'),
        ('Man-Made', (
                ('wood', 'Wood'),
                ('stone', 'Stone')
            )
        ),
        ('O', 'Other')
    ]

    allowed_memberships = models.ManyToManyField(Membership)
    object_type = models.CharField(max_length=30, choices=TYPE_CHOICE, default='Other')

    def __str__(self):
        return self.title




"""-------------Landscape Models----------------"""
class LandscapeFree(AllItems):

    TYPE_CHOICE = [
        ('forest', 'Forest'),
        ('dessert', 'Dessert'),
        ('city', 'City'),
        ('mountains', 'Mountains'),
        ('other', 'Other')
    ]

    allowed_memberships = models.ManyToManyField(Membership)
    landscape_type = models.CharField(max_length=30, choices=TYPE_CHOICE, default='Other')

    def __str__(self):
        return self.title


class LandscapePremium(AllItems):

    TYPE_CHOICE = [
        ('forest', 'Forest'),
        ('dessert', 'Dessert'),
        ('city', 'City'),
        ('mountains', 'Mountains'),
        ('other', 'Other')
    ]

    landscape_type = models.CharField(max_length=30, choices=TYPE_CHOICE, default='Other')

    def __str__(self):
        return self.title