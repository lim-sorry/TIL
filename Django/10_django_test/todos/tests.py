from django.test import TestCase
from accounts.models import User

# Create your tests here.
class TodoTest(TestCase):
    def test_todo_index(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url,'/accounts/login/?next=/todos/')

        User.objects.create_user(username='testuser',password='password')
        self.client.login(username='testuser',password='password')
        self.assertTemplateUsed(response,'todos/index.html')