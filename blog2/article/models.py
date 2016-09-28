from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from django.utils.text import slugify

# Create your models here.



class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-timestamp", "-updated"]





