from django.db import models

from .category import Category

class Note(models.Model):

    # statuses
    ACTIVE = 'active'
    INACTIVE = 'inactive'

    STATUSES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=19999, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="notes", blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUSES, default=ACTIVE)