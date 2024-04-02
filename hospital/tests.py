from django.test import TestCase, Client  # Import Client here
from .forms import *
from .models import *


class FormsTestCase(TestCase):
    def test_admin_form(self):
        form_data = {
            'first_name': 'Admin',
            'last_name': 'User',
            'username': 'admin',
            'email': 'admin@example.com',
            'password': 'admin123'
        }
        form = AdminForms(data=form_data)
        self.assertTrue(form.is_valid())

    # Write similar test methods for other forms...


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='test123')

    def test_doctor_creation(self):
        doctor = Doctor.objects.create(
            user=self.user, address='Test Address', mobile='1234567890')
        self.assertEqual(doctor.get_name, 'testuser')  # Remove the parentheses from get_name

    # Write similar test methods for other models...


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/index.html')
