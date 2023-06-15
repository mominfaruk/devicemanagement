import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "repliqassignment.settings")
django.setup()

from assettracking.models import Company, Employee, Device

def insert_data():
    # Create companies
    companies = []
    for i in range(10):
        company = Company.objects.create(
            name=f'Company {i+1}',
            address=f'{i+1} Main St',
            contact_number=f'123456789{i}'
        )
        companies.append(company)

    # Create employees
    employees = []
    for i in range(10):
        user = User.objects.create(username=f'employee{i+1}')
        employee = Employee.objects.create(
            company=companies[i],
            user=user,
            name=f'Employee {i+1}',
            designation='Manager' if i < 5 else 'Developer',
            contact_number=f'98765432{i}'
        )
        employees.append(employee)

    # Create devices
    devices = []
    for i in range(10):
        device = Device.objects.create(
            company=companies[i],
            name=f'Device {i+1}',
            description=f'Description for Device {i+1}',
            serial_number=f'Serial-{i+1}',
            condition='Good' if i < 5 else 'Fair'
        )
        devices.append(device)

    print('Data inserted successfully.')

if __name__ == '__main__':
    insert_data()