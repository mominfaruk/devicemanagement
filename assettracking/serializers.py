from rest_framework import serializers
from .models import Company, Employee, Device, Checkout, ConditionLog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'user' ,'name', 'address', 'contact_number']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'designation', 'contact_number']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'description', 'serial_number', 'condition']

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['id', 'employee', 'device', 'checkout_date', 'return_date']

class ConditionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionLog
        fields = ['id', 'device', 'checked_out_condition', 'checked_in_condition', 'date']
