from django.test import SimpleTestCase



class SimpleTests(SimpleTestCase):
	def test_signup_page_status_code(self):
		response = self.client.get('/accounts/signup/')
		self.assertEqual(response.status_code,200)