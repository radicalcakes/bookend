# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin, TemplateView

from users.forms import LoginForm, RegistrationForm
from braces.views import LoginRequiredMixin

class Home(TemplateView):
	template_name = "home.html"
	login_form = LoginForm()
	register_form = RegistrationForm()
	
	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context["login_form"] = self.login_form
		context["register_form"] = self.register_form
		return context


