from django.test import TestCase
from unittest import TestCase
from api.models import ApplicationRegister
from api.test.factories import RegisterFactory


# Create your tests here.
class RegisterTestCase(TestCase):
    def setUp(self) -> None:
        # user_register = RegisterFactory()
        self.user = ApplicationRegister.objects.create(RegisterFactory)
