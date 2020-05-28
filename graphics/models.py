from django.db import models
from django.utils import timezone
from PIL import Image

class GraphicDesigns(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    text_content = models.TextField()
    color = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg', upload_to='graphic_image')
    date_made = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)