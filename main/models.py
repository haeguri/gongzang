from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from markdownx.models import MarkdownxField

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles')
    title = models.CharField("제목", max_length=50, null=False, blank=False)
    # body = models.TextField("본문", null=False, blank=False)
    body = MarkdownxField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('main:article_detail', kwargs={'pk': self.id})