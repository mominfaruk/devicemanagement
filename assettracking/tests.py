from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Company, Employee, Device

class AssetTrackingAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a company
        self.company = Company.objects.create(
            name='Example Company',
            address='123 Main St',
            contact_number='1234567890'
        )

        # Create an employee
        self.employee = Employee.objects.create(
            company=self.company,
            name='John Doe',
            designation='Manager',
            contact_number='9876543210'
        )

        # Create a device
        self.device = Device.objects.create(
            company=self.company,
            name='Laptop',
            description='Dell Latitude',
            serial_number='ABC123',
            condition='Good'
        )

    def test_create_company(self):
        url = '/companies/'
        data = {
            'name': 'New Company',
            'address': '456 Elm St',
            'contact_number': '0987654321'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 2)

    def test_get_employee(self):
        url = f'/employees/{self.employee.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_update_device(self):
        url = f'/devices/{self.device.id}/'
        data = {
            'name': 'New Laptop',
            'description': 'HP EliteBook',
            'serial_number': 'XYZ789',
            'condition': 'Excellent'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'New Laptop')
        self.assertEqual(response.data['condition'], 'Excellent')

    def test_delete_employee(self):
        url = f'/employees/{self.employee.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)
