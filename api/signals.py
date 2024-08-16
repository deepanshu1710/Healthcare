from django.apps import AppConfig
from django.contrib.auth.models import Group

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        create_user_groups()

def create_user_groups():
    Group.objects.get_or_create(name='Patients')
    Group.objects.get_or_create(name='Doctors')
