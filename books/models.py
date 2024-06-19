from django.db import models
from users.models import User


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    pages = models.IntegerField(verbose_name='تعداد صفحات', blank=True, null=True)
    cover = models.ImageField(upload_to='books/', verbose_name='عکس', blank=True)
    author = models.ForeignKey('authors.Author', verbose_name='نویسنده', on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey('publishers.Publisher', verbose_name='ناشر', on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey('users.User', verbose_name='مالک', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
