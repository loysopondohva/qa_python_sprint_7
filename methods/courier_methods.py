import requests
import data


class CourierMethods:
    @staticmethod
    def courier_create(body):
        return requests.post(f'{data.Url.BASE_URL}{data.Url.CREATE_COURIER}', json=body)

    @staticmethod
    def courier_login(login_body):
        courier = requests.post(f'{data.Url.BASE_URL}{data.Url.LOGIN_COURIER}', json=login_body)
        return courier

    @staticmethod
    def courier_delete(courier_id):
        return requests.delete(f'{data.Url.BASE_URL}{data.Url.DELETE_COURIER}{courier_id}')