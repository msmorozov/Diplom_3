import allure
from faker import Faker

@allure.step('Генерация тестовых данных пользователя из РФ')
def create_user_data():
    fake = Faker('ru_RU')
    user_data = {
        "email": fake.email(),
        "name": fake.first_name(),
        "password": fake.password()
    }
    return user_data
