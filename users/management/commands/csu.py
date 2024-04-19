from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='admin@admin.com',
                                   phone_number='+15555555555',
                                   country='United Kingdom')
        user.set_password('<PASSWORD>')
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

