from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='app_image/', default='default.png')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = TaggableManager()
    counted_views = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    login_needed = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category_list = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_show:single_blog', kwargs={'pid': self.id})


class Comment(models.Model):
    intended_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
