from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.fields import DecimalField, DictField, FileField, DateField, ListField
from datetime import datetime
from .models import EnergyCost, EnergyTradingCompany
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator


'''
    THIS SERIALIZERS ARE REDUNDANT WE CAN USE energycost_set IN THE EnergyCompanySeriales
    TO GET ALL COST ORGANIZED SO

    TO DO:

    SET AN API THAT IN THE /energycompany/ GIVES ID AND NAME AS DATA AND
    INT /energycompany/<id>/ GIVES A LIST OF THE COST AND EXTRA INFORMATION
    ABOUT THE COMPANY, /energycost/ SHOULD BE DELETED

    THIS COMMENT IS A REMAINDER
'''

class EnergyCompanySerializer(ModelSerializer):
    class Meta:
        model = EnergyTradingCompany
        fields = ['id','name']

class UnixTimestamp(DateField):
    def to_internal_value(self, value):
        return super().to_internal_value(value)
    
    def to_representation(self, value):
        try:
            ret = datetime(*value.timetuple()[:-4]).timestamp()
        except AttributeError as e:
            ret = super().to_representation(value)
        return ret

class EnergyCostSerializer(ModelSerializer):
    unix_timestamp = UnixTimestamp(source='month_year')

    class Meta:
        model = EnergyCost
        fields = ['unix_timestamp','cost','trading_company']


class EnergyCostExcelSheet(Serializer):
    file = FileField()
        
