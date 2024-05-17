from .models import Meter,Meter_Data

from rest_framework import serializers

class MeterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meter
        fields = "__all__"



class MeterDataSerializers(serializers.ModelSerializer):
    created = serializers.SerializerMethodField(read_only=True)
    def get_created(self, obj):
        return obj.created.strftime("%m-%d-%Y - %I:%M%p")

    class Meta:
        model = Meter_Data
        exclude = ['modified']

class MeterDetailSerializers(serializers.ModelSerializer):
    meter_data_list = serializers.SerializerMethodField()
    class Meta:
        model = Meter
        fields = "__all__"
    
    def get_meter_data_list(self, obj):
        pending_orders = obj.get_meter_data_list()
        serializer = MeterDataSerializers(pending_orders, many=True, read_only=True)
        return serializer.data