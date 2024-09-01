from django.db import models
from django.utils.text import slugify

class TagLine(models.Model):
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# Create your models here.
class Posts(models.Model):
    title_course = models.CharField(max_length=50)
    describe = models.TextField(default="no describe", null=True)
    day = models.DateField(auto_now_add=True)  # Automatically set the date when the object is created
    time = models.TimeField(auto_now_add=True)  # Automatically set the time when the object is created
    images = models.FileField(upload_to='images', max_length=100)
    slug = models.SlugField(max_length=255, blank=True,editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(TagLine,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_course)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_course
    
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.post}"