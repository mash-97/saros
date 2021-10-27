from django.db import models
from django.contrib.auth import get_user_model 
from django.db.models.signals import pre_save 
from django.dispatch import receiver 
from saros.utils import *

class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, null = True, blank = True)
    text = models.TextField()
    published_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

