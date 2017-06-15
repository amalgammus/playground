from django.db import models
from django.utils import timezone


class Clients(models.Model):
    client_id = models.PositiveSmallIntegerField()
    client_ip = models.GenericIPAddressField(protocol='IPv4')
    client_tmdns = models.CharField(max_length=100)
    client_port = models.PositiveIntegerField()
    client_key = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    deleted_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.datetime.now()
        super(Clients, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.client_id)

    class Meta:
        verbose_name_plural = 'Clients'
