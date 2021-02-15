from django.db import models
from django.contrib.postgres.fields import ArrayField



class Users(models.Model):
    user_email = models.EmailField(max_length=254, null=False)
    user_password = models.CharField(max_length=254)
    user_settings = models.JSONField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Tokens(models.Model):
    ACCESS_TYPE_CHOICES = [
        ('online', 'online'),
        ('offline', 'offline')
    ]

    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    token = models.TextField()
    refresh_token = models.TextField()
    access_type = models.CharField(max_length=8, choices=ACCESS_TYPE_CHOICES)
    drive = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"


class Books(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=254, default="Undefined-book-name")
    author_name = models.CharField(max_length=254, default="Undefined-author-name")
    author_lastname = models.CharField(max_length=254, default="Undefined-author-lastname")
    link = models.TextField()
    tags = ArrayField(
        models.CharField(max_length=254)
    )
    label = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.book_name} by {self.author_name} {self.author_lastname}. Owned by {self.user_id}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    


class Notes(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    note = models.TextField()
    text_pointer = models.IntegerField()

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"


class Bookmarks(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    text_pointer = models.IntegerField()

    class Meta:
        verbose_name = "Bookmark"
        verbose_name_plural = "Bookmarks"
