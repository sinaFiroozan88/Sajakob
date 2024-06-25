from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
#
# from books.models import Book
# from genres.models import Genre


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    favorite_books = models.ManyToManyField('books.Book', related_name='favorite_books_users', blank=True)
    favorite_genres = models.ManyToManyField('genres.Genre', related_name='favorite_genres_users', blank=True)
    read_books = models.ManyToManyField('books.Book', related_name='read_books_users', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Adding a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Adding a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )

    def __str__(self):
        return self.username
