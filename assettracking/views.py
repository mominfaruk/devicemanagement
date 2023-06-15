from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Company, Employee, Device, Checkout, ConditionLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, CheckoutSerializer, ConditionLogSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Company.objects.filter(user=user)
        return Company.objects.none()

    def update(self, request, *args, **kwargs):
        company = self.get_object()
        if company.user == request.user:
            serializer = self.get_serializer(company, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Employee.objects.filter(company__user=user)
        return Employee.objects.none()
    
    def perform_create(self, serializer):
        company=Company.objects.get(user=self.request.user)
        serializer.save(company=company)
    
    def perform_update(self, serializer):
        serializer.save(company__user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Device.objects.filter(company__user=user)
        return Device.objects.none()

    def perform_create(self, serializer):
        serializer.save(company__user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(company__user=self.request.user)


class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Checkout.objects.filter(device__company__user=user)
        return Checkout.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(device__company__user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(device__company__user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()



class ConditionLogViewSet(viewsets.ModelViewSet):
    queryset = ConditionLog.objects.all()
    serializer_class = ConditionLogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return ConditionLog.objects.filter(device__company__user=user)
        return ConditionLog.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(device__company__user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(device__company__user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()
    
    
