from django.db import models

class Task(models.Model):
    TODO = 0
    DONE = 1

    STATUS_CHOICES = (
    # We create a tuple of status choices
        (TODO, 'To do'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255)

    # The task's status, default status = TODO
    status = models.IntegerField(choices=STATUS_CHOICES, default=TODO)
