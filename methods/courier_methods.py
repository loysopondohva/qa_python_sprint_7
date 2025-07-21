import requests
import data
import urls

class CourierMethods:
    @staticmethod
    def courier_create(body):
        return requests.post(f'{urls.BASE_URL}{urls.CREATE_COURIER}', json=body)

    @staticmethod
    def courier_login(login_body):
        courier = requests.post(f'{urls.BASE_URL}{urls.LOGIN_COURIER}', json=login_body)
        return courier

    @staticmethod
    def courier_delete(courier_id):
        return requests.delete(f'{urls.BASE_URL}{urls.DELETE_COURIER}{courier_id}')