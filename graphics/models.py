from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import Membership
from PIL import Image


class Category(models.Model):
    CATEGORY_CHOICE = [
        ('Animated Creatures', 'Animated Creatures'),
        ('Animated Objects', 'Animated Objects'),
        ('Landscapes', 'Landscapes')
    ]

    title = models.CharField(max_length=20, choices=CATEGORY_CHOICE, default='Animated Creatures')

    def __str__(self):
        return self.title


class Creature(models.Model):
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
    TYPE_CHOICE = [
        ('H', 'Main Character'),
        ('E', 'Villain'),
        ('N', 'Neutral')
    ]

    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text_content = models.TextField(default=None)
    color = models.CharField(max_length=30, choices=COLOR_CHOICE, default='Blue')
    character_type = models.CharField(max_length=30, choices=TYPE_CHOICE, default='Blue')
    image = models.ImageField( upload_to='images/creatures', blank=True, null=True)
    date_made = models.DateTimeField(default=timezone.now)
    allowed_memberships = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Object(models.Model):
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

    TYPE_CHOICE = [
        ('V', 'Vegetation'),
        ('Man-Made', (
                ('wood', 'Wood'),
                ('stone', 'Stone')
            )
        ),
        ('O', 'Other')
    ]


    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text_content = models.TextField(default=None)
    color = models.CharField(max_length=30, choices=COLOR_CHOICE, default='Blue')
    object_type = models.CharField(max_length=30, choices=TYPE_CHOICE, default='Blue')
    image = models.ImageField(default='default.jpg', upload_to='images/objects')
    date_made = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Landscape(models.Model):
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

    TYPE_CHOICE = [
        ('forest', 'Forest'),
        ('dessert', 'Dessert'),
        ('city', 'City'),
        ('mountains', 'Mountains')
    ]

    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text_content = models.TextField(default=None)
    main_color = models.CharField(max_length=30, choices=COLOR_CHOICE, default='Blue')
    landscape_type = models.CharField(max_length=30, choices=TYPE_CHOICE, default='Blue')
    image = models.ImageField(default='default.jpg', upload_to='images/landscapes')
    date_made = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title