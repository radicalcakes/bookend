import re
import datetime
import string

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.datastructures import MultiValueDictKeyError
import django.core.validators

from users.models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout, Button, Fieldset
from crispy_forms.bootstrap import FormActions


class RegistrationForm(forms.ModelForm):
	class Meta:
		model = User
	
	password1 = forms.CharField(
		widget=forms.PasswordInput(render_value=False)
	)
	password2 = forms.CharField(
		widget=forms.PasswordInput(render_value=False)
	)


	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

	
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = "form-horizontal register_form span6"
		self.helper.form_method = "post"
		self.helper.form_action = "user/join/"
		self.helper.layout = Layout(
			Field("username", css_class="span3", placeholder="Your username"),
			Field("email", css_class="span3", placeholder="Your email"),
			Field("password1", css_class="span3", placeholder="Password"),
			Field("password2", css_class="span3", placeholder="Re-enter Password"),
			Submit("submit", "Sign Up", css_class="btn-large btn-success sign-in-home span2")
		) 



class LoginForm(forms.Form):
	username = forms.CharField(
		label = None,
		max_length = 255,
		required=True
	)

	password = forms.CharField(
		label = None,
		widget=forms.PasswordInput(render_value=False)
	)

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = "form-inline pull-right login_form"
		self.helper.form_method = "post"
		self.helper.form_action = "user/login/"

		self.helper.layout = Layout(
			Field("username", label=None, css_class="span2", placeholder="username"),
			Field("password",label=None, css_class="span2", placeholder="password"),
			Submit("submit", "Login", css_class="btn")
		) 

