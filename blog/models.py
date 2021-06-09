from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import AbstractUser
# class ArgoUser(AbstractUser):
#     pass


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    user = models.ForeignKey(ArgoUser, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    descriptions = models.CharField(max_length=150, verbose_name='Описание')
    content = models.TextField(verbose_name='Текст', null=True)
    image = models.ImageField(verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    favourite = models.ManyToManyField(ArgoUser, related_name="fav_post", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    user = models.ForeignKey(ArgoUser, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
