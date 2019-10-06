from django.test import SimpleTestCase , TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SimpleTests(SimpleTestCase):

	def test_signup_page_status_code(self):
		response = self.client.get('/accounts/signup/')
		self.assertEqual(response.status_code,200)

	def test_login_page_status_code(self):
		response = self.client.get('/accounts/login/')
		self.assertEqual(response.status_code,200)

	def password_change_page_status_code(self):
		response = self.client.get('/accounts/password_change/')
		self.assertEqual(response.status_code,200)

	def test_password_change_done_page_status_code(self):
		response = self.client.get('/accounts/password_change/done/')
		self.assertEqual(response.status_code,302)

	def test_password_reset_page_status_code(self):
		response = self.client.get('/accounts/password_reset/')
		self.assertEqual(response.status_code,200)

	def test_password_reset_done_page_status_code(self):
		response = self.client.get('/accounts/password_reset/done/')

	def test_logout_page_status_code(self):
		response = self.client.get('/accounts/logout/')\
		#The logout url redirects to home page hence we check for 302 status code. 
		#Read more about 302 status code https://en.wikipedia.org/wiki/HTTP_302
		self.assertEqual(response.status_code,302)

	def test_signup_uses_correct_template(self):
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'signup.html')

	def test_login_uses_correct_template(self):
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_logout_by_name(self):
		response = self.client.get(reverse('logout'))
		self.assertEqual(response.status_code,302)


	def test_login_uses_correct_template(self):
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_login_uses_correct_template(self):
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_pwrc_uses_correct_template(self):
		response = self.client.get(reverse('password_reset_complete'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'registration/password_reset_complete.html')

	def test_pwrd_uses_correct_template(self):
		response = self.client.get(reverse('password_reset_done'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'registration/password_reset_done.html')

	def test_pwrf_uses_correct_template(self): #password reset form
		response = self.client.get(reverse('password_reset'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'registration/password_reset_form.html')


class SignupPageTest(TestCase):
	
	username = 'newuser'
	email = 'newuser@email.com'

	def test_signup_form(self):
		new_user = get_user_model().objects.create_user(self.username, self.email)
		self.assertEqual(get_user_model().objects.all().count(),1)
		self.assertEqual(get_user_model().objects.all()[0].username, self.username)
		self.assertEqual(get_user_model().objects.all()[0].email, self.email)