from .models import User
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.views.generic import CreateView
# Create your views here.

class SignUpView(CreateView):
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy('registration')
    template_name = 'registration.html'
