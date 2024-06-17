from django.db import models


class Room(models.Model):
    room_content = models.CharField(max_length=200)


class Note(models.Model):
    note_content = models.CharField(max_length=200)


class Book(models.Model):
    book_content = models.CharField(max_length=200)

