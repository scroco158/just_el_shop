from django.core.mail import send_mail
import os


def send_information_mail(post_name):

    email_from = os.getenv('EMAIL_HOST_USER')
    send_mail(
        '100 просмотров',
        f'Поздравляю ваш пост {post_name} просмотрели 100 раз',
        email_from,
        ('scroco@mail.ru',)
    )
