from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config import settings
from users.forms import UserRegisterForm
from users.models import User
import secrets


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        host = self.request.get_host()
        print(type(host), ' <- хост -> ', host)
        url = f'http://{host}/users/email-confirm/{token}/'
        user.save()
        send_mail(
            subject='Confirm your email',
            message=f'Please confirm your email {url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    print(' *******************')
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


