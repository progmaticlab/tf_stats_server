from django.db import models


class Stats(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    host_id = models.CharField(max_length=20, blank=False)
    vmachines = models.CharField(max_length=5, blank=False)
    vnetworks = models.CharField(max_length=5, blank=False)
    vrouters = models.CharField(max_length=5, blank=False)
    vm_interfaces = models.CharField(max_length=5, blank=False)

    class Meta:
        ordering = ('created',)
