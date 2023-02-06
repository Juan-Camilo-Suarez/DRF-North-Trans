import factory

from api.models import ApplicationRegister, User


class RegisterFactory(factory.Factory):
    class Meta:
        model = ApplicationRegister

    name = factory.Faker("name")
    city = factory.Faker("city")
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")
    user_position = "client"


class UserFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.Faker("email")
    name = factory.Faker("name")
    password = factory.Faker("password")
    # regula quien puede ir al admin
    role = "client"
