from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Car

class CarTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        test_user = get_user_model().objects.create_user(
            username='testuser', password='password'
        )
        test_user.save()

        Car.objects.create(
            buyer=test_user,
            car_model='Test Model',
            car_brand='Test Brand',
            car_price=10000,
            is_bought=True
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_car_list_view(self):
        response = self.client.get(reverse('cars'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_list.html')
        self.assertContains(response, 'Test Model')

    def test_car_detail_view(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('details', args=[car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_details.html')
        self.assertContains(response, 'Test Model')

    def test_create_car_view(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_car.html')

    def test_update_car_view(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('update', args=[car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_update.html')

    def test_delete_car_view(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('delete', args=[car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_delete.html')


class CarModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='testuser', password='password'
        )
        test_user.save()

        cls.car = Car.objects.create(
            buyer=test_user,
            car_model='Test Model',
            car_brand='Test Brand',
            car_price=10000,
            is_bought=True
        )

    def test_car_string_representation(self):
        self.assertEqual(str(self.car), 'Test Model')

    def test_car_model_fields(self):
        self.assertEqual(self.car.car_model, 'Test Model')
        self.assertEqual(self.car.car_brand, 'Test Brand')
        self.assertEqual(self.car.car_price, 10000)
        self.assertEqual(self.car.is_bought, True)
        self.assertTrue(self.car.buy_time)

    def test_car_get_absolute_url(self):
        self.assertEqual(self.car.get_absolute_url(), f'/car_details/{self.car.id}')
