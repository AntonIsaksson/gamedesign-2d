from django.db import models
from django.utils import timezone
from PIL import Image


class Category(models.Model):
    CATEGORY_CHOICE = [
        ('AC', 'Animated Creatures'),
        ('AO', 'Animated Objects'),
        ('L', 'Landscapes')
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
        ('H', 'Hero'),
        ('E', 'Enemy'),
        ('N', 'Neutral')
    ]

    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text_content = models.TextField(default=None)
    color = models.CharField(max_length=30, choices=COLOR_CHOICE, default='Blue')
    character_type = models.CharField(max_length=30, choices=TYPE_CHOICE, default='Blue')
    image = models.ImageField( upload_to='images/', blank=True, null=True)
    date_made = models.DateTimeField(default=timezone.now)

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
        ('N', 'Neutral')
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