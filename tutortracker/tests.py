from django.test import SimpleTestCase



class SimpleTests(SimpleTestCase):
	def test_home_page_status_code(self):
		response = self.client.get('/tutortracker/')
		self.assertEqual(response.status_code,200)


	def test_about_page_status_code(self):
		response = self.client.get('/tutortracker/about/')
		self.assertEqual(response.status_code,200)

	def test_login_page_status_code(self):
		response = self.client.get('/accounts/login/')
		self.assertEqual(response.status_code,200)

	def test_logout_page_status_code(self):
		response = self.client.get('/accounts/logout/')\
		#The logout url redirects to home page hence we check for 302 status code. 
		#Read more about 302 status code https://en.wikipedia.org/wiki/HTTP_302
		self.assertEqual(response.status_code,302)