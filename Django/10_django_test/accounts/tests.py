from django.test import TestCase
from .models import User

# Create your tests here.
class AccountTestClass(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser',password='password')
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_user_model_create(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.username,'testuser')

    def test_user_str_method(self):
        user = User.objects.get(pk=1)
        self.assertEqual(str(user),'User object (1)')

    def test_user_phtone_field_max_length(self):
        user = User.objects.get(pk=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEqual(max_length,11)

    def test_base_template(self):
        response = self.client.get('/accounts/')
        self.assertContains(response,'login')
        self.assertNotContains(response,'logout')

        self.client.login(username='testuser',password='password')
        response = self.client.get('/accounts/')
        self.assertContains(response,'logout')
        self.assertNotContains(response,'login')