"""
Команда добавляет администратора.
"""
import os

from django.core.management.base import BaseCommand

basedir = os.path.abspath(os.path.dirname(__file__))

name_admin = 'admin'
pass_admin = '12345'
email_admin = 'admin@a.ru'


class Command(BaseCommand):

    def handle(self, *args, **options):
        from django.contrib.auth import get_user_model
        user = get_user_model().objects.filter(username=name_admin).first()
        if not user:
            get_user_model().objects.create_superuser(username=name_admin,
                                                      password=pass_admin,
                                                      email=email_admin)
