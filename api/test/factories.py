import factory

from api.models import ApplicationRegister


class RegisterFactory(factory.Factory):
    class Meta:
        model = ApplicationRegister

    name = factory.Faker("name")
    city = factory.Faker("city")
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")
    user_position = "client"
