from rest_framework.serializers import ModelSerializer

from rest_api.models import Stats


class StatsSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = ('tf_id',
                  'vmachines',
                  'vnetworks',
                  'vrouters',
                  'vm_interfaces')
