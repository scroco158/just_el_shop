import random
import string
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
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


def password_reset(request):
    """ Создание нового пароля пользователя по электронному адресу"""

    if request.method == 'POST':
        email_address = request.POST.get('email_address')
        print(email_address)
        user = User.objects.filter(email=email_address).first()

        if user is None:
            return render(request, 'users/password_reset.html',
                          {'error_message': 'Пользователя с такой почтой не существует'})

        new_password = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
        print(new_password)
        user.set_password(new_password)
        user.save()
        send_mail(
            subject='Новый пароль',
            message=f'Ваш новый пароль {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        success_url = reverse_lazy('users:login')
        return HttpResponseRedirect(success_url)

    return render(request, 'users/password_reset.html')
