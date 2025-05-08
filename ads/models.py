from django.utils import timezone
from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _

class Ad(models.Model):
    publisher = models.ForeignKey(
        to=User,
        related_name='ads',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('publisher')
    )
    title = models.CharField(verbose_name=_('title'), max_length=255)
    caption = models.TextField(verbose_name=_('caption'))
    image = models.ImageField(verbose_name=_('image'), upload_to='ad_images', null=True, blank=True)
    is_public = models.BooleanField(verbose_name=_('is_public'), default=True)
    date_added = models.DateTimeField(verbose_name=_('date published'), default=timezone.now())


    class Meta:
        get_latest_by = 'date_added'
        ordering = ('-date_added',)
        verbose_name = _('ad')
        verbose_name_plural = _('ads')

    def __str__(self):
        return self.title