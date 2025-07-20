import allure
import pytest
from methods.courier_methods import CourierMethods
import data


class TestCourierCreate:
    @allure.title('Тестирование успешного создания курьера')
    @allure.description('Тут проверяем, что курьер создается с сгенерированными данными')
    def test_courier_create_success(self, create_courier_data_and_delete):
        courier_register_body = create_courier_data_and_delete[0]
        response = CourierMethods.courier_create(courier_register_body)
        expected_data = data.ResponseData.COURIER_CREATION_SUCCESS
        assert response.status_code == expected_data['code']
        assert response.json() == expected_data['message']

    @allure.title('Тестирование создания курьера без поля name')
    @allure.description('Тут проверяем, что курьер создается без поля Имя')
    def test_courier_create_without_name_success(self, create_courier_data_and_delete):
        courier_register_body = create_courier_data_and_delete[0]
        del courier_register_body['name'] # Удаляем поле имя из тела запроса.
        response = CourierMethods.courier_create(courier_register_body)
        expected_data = data.ResponseData.COURIER_CREATION_SUCCESS
        assert response.status_code == expected_data['code']
        assert response.json() == expected_data['message']

    @allure.title('Тестирование невозможности создания двух одинаковых курьеров')
    @allure.description('Проверяем создание курьера с одинаковыми данными 2 раза подряд')
    def test_courier_creation_dublicate_failed(self, create_courier_data_and_delete):
        courier_register_body = create_courier_data_and_delete[0]
        courier_first = CourierMethods.courier_create(courier_register_body)
        courier_second = CourierMethods.courier_create(courier_register_body)
        expected_data = data.ResponseData.COURIER_CREATION_FAILED_ALREADY_EXIST
        assert courier_second.status_code == expected_data['code']
        assert courier_second.json()['message'] == expected_data['message']

    @allure.title('Тестирование невозможности создания курьера с незаполненными обязательными полями')
    @allure.description('Проверяем создание курьера сначала без логина, потом без пароля')
    @pytest.mark.parametrize('login, password',[
        (data.CourierData.create_courier_login,''),('',data.CourierData.create_courier_password)])
    def test_courier_creation_without_login_password_failed(self, login, password):
        courier_register_body = {'login': login, 'password': password}
        response = CourierMethods.courier_create(courier_register_body)
        expected_data = data.ResponseData.COURIER_CREATION_FAILED_NO_LOGIN_PASSWORD
        assert response.status_code == expected_data['code']
        assert response.json()['message'] == expected_data['message']

class TestCourierLogin:
    @allure.title('Тестирование успешного логина курьера в систему')
    @allure.description('Тут проверяем, что заранее созданный курьер может логиниться в систему')
    def test_courier_login_success(self, create_courier_and_delete):
        courier_login_body = create_courier_and_delete[1]
        response = CourierMethods.courier_login(courier_login_body)
        expected_data = {'code': 200}
        assert response.status_code == expected_data['code']
        assert response.json()['id'] > 0

    @allure.title('Тестирование выдаваемой ошибки при попытке логина незарегистрированного пользователя')
    @allure.description('Тут проверяем, что вход в систему невозможен при отсутствующем пользователе')
    def test_courier_login_courier_not_exist_failed(self):
        courier_login_body = data.CourierData.random_courier_login_data
        response = CourierMethods.courier_login(courier_login_body)
        expected_data = data.ResponseData.COURIER_LOGIN_NOT_FOUND
        assert response.status_code == expected_data['code']
        assert response.json()['message'] == expected_data['message']

    @allure.title('Тестирование выдаваемой ошибки при некорректном логине')
    @allure.description('Тут проверяем, что правильно выдаются ошибки при некорректно указанных логине или пароле в запросе')
    @pytest.mark.parametrize('login_modifier, password_modifier, expected', [
        (lambda login: "", lambda pwd: pwd, data.ResponseData.COURIER_LOGIN_FAILED_NO_LOGIN_PASSWORD),        # пустой логин
        (lambda login: login, lambda pwd: "", data.ResponseData.COURIER_LOGIN_FAILED_NO_LOGIN_PASSWORD),      # пустой пароль
        (lambda login: "", lambda pwd: "", data.ResponseData.COURIER_LOGIN_FAILED_NO_LOGIN_PASSWORD),         # пустой логин и пароль
        (lambda login: login + "_wrong", lambda pwd: pwd, data.ResponseData.COURIER_LOGIN_NOT_FOUND),  # неправильный логин
        (lambda login: login, lambda pwd: pwd + "_wrong", data.ResponseData.COURIER_LOGIN_NOT_FOUND)  # неправильный пароль
    ])
    def test_courier_login_invalid_cases_failed(self, login_modifier, password_modifier, expected):
        with allure.step('Создаём пользователя'):
            login = data.CourierData.create_courier_login
            password = data.CourierData.create_courier_password
            courier_body = {'login': login, 'password': password, 'firstName': 'Test'}
            CourierMethods.courier_create(courier_body)

        with allure.step('Модифицируем логин и пароль'):
            test_login = login_modifier(login)
            test_password = password_modifier(password)
            login_body = {'login': test_login, 'password': test_password}

        with allure.step('Пробуем войти в систему'):
            response = CourierMethods.courier_login(login_body)

        with allure.step('Проверяем ошибку'):
            assert response.status_code == expected['code']
            assert response.json()['message'] == expected['message']