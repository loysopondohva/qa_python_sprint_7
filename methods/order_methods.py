import requests
import data
import urls


class OrderMethods:
    @staticmethod
    def order_create(order_body):
        return  requests.post(f'{urls.BASE_URL}{urls.CREATE_ORDER}',json=order_body)

    @staticmethod
    def order_cancel(order_track):
        params = {'track': order_track}
        return requests.put(f'{urls.BASE_URL}{urls.CANCEL_ORDER}', params=params)

    @staticmethod
    def get_orders_list():
        return requests.get(f'{urls.BASE_URL}{urls.GET_ORDERS}')