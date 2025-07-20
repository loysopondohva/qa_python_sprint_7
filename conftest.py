import pytest
import requests
import allure
import generators
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def create_courier_and_delete():
    with allure.step('Получаем сгенерированные данные курьера'):
        courier_register_body = generators.generate_courier_body()
        login = courier_register_body['login']
        password = courier_register_body['password']
        courier_login_body = {'login': login, 'password': password}
    with allure.step('Создаём курьера'):
        CourierMethods.courier_create(courier_register_body)
    yield [courier_register_body, courier_login_body, login, password]
    with allure.step('Логинимся в систему созданным курьером'):
        courier = CourierMethods.courier_login(courier_login_body)
    with allure.step('Удаляем созданного курьера'):
        CourierMethods.courier_delete(courier.json()['id'])

@pytest.fixture()
def create_courier_data_and_delete():
    with allure.step('Получаем сгенерированные данные курьера'):
        courier_register_body = generators.generate_courier_body()
        login = courier_register_body['login']
        password = courier_register_body['password']

        courier_login_body = {'login': login, 'password': password}
    yield [courier_register_body, courier_login_body, login, password]
    with allure.step('Логинимся в систему созданным курьером'):
        courier = CourierMethods.courier_login(courier_login_body)
    with allure.step('Удаляем созданного курьера'):
        CourierMethods.courier_delete(courier.json()['id'])