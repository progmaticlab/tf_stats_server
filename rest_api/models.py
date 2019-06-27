from django.db import models


class Stats(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tf_id = models.CharField(max_length=50, blank=False,
                             unique_for_date="created")
    vmachines = models.CharField(max_length=5, blank=False)
    vnetworks = models.CharField(max_length=5, blank=False)
    vrouters = models.CharField(max_length=5, blank=False)
    vm_interfaces = models.CharField(max_length=5, blank=False)
