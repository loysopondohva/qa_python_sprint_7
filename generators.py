import pytest
from faker import Faker
import allure

fake = Faker('ru-RU')

def generate_login():
    generated_login = fake.user_name()
    return generated_login

def generate_password():
    generated_password = fake.password()
    return generated_password

def generate_name():
    generated_name = f"{fake.first_name()} {fake.last_name()}"
    return generated_name

@allure.step('Генерируем данные для регистрации курьера')
def generate_courier_body():
    courier = {
        'login': generate_login(),
        'password': generate_password(),
        'name': generate_name()
    }
    return courier

@allure.step('Генерируем данные для регистрации заказа')
def generate_order_body():
    order_body = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": fake.random_int(1,10),
            "phone": fake.phone_number(),
            "rentTime": fake.random_int(1,20),
            "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
            "comment": fake.sentence(),
            "color": fake.random_element(elements=[['BLACK'], ['GREY'], [''], (['BLACK'],['GREY'])])
        }
    return order_body