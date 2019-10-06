from django.test import SimpleTestCase , TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model




class SimpleTests(SimpleTestCase):
	def test_home_page_status_code(self):
		response = self.client.get('/tutortracker/')
		self.assertEqual(response.status_code,200)


	def test_about_page_status_code(self):
		response = self.client.get('/tutortracker/about/')
		self.assertEqual(response.status_code,200)


	def test_home_uses_correct_template(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'home.html')

	def test_about_uses_correct_template(self):
		response = self.client.get(reverse('about'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'about.html')