from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'

    STATUSES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    ]

    user = models.ForeignKey(User, verbose_name='User',
                             blank=False, null=False)
    title = models.CharField(max_length=100, verbose_name='Title',
                             blank=False, null=False)
    status = models.CharField(max_length=15, verbose_name='Status',
                              default=STATUS_DRAFT, choices=STATUSES,
                              blank=False, null=False)
    ingredients = models.TextField(verbose_name='Ingredients',
                                   blank=True, null=True)
    lead = models.TextField(verbose_name='Lead',
                            blank=True, null=True)
    content = models.TextField(verbose_name='Content',
                               blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Created at',
                                      auto_now_add=True,
                                      blank=False, null=False)
    updated_at = models.DateTimeField(verbose_name='Updated at',
                                      auto_now=True,
                                      blank=False, null=False)

    def __str__(self):
        return '{}: {}'.format(self.user, self.title)
