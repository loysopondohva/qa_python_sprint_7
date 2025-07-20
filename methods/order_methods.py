import requests
import data


class OrderMethods:
    @staticmethod
    def order_create(order_body):
        print(order_body)
        return  requests.post(f'{data.Url.BASE_URL}{data.Url.CREATE_ORDER}',json=order_body)

    @staticmethod
    def order_cancel(order_track):
        params = {'track': order_track}
        return requests.put(f'{data.Url.BASE_URL}{data.Url.CANCEL_ORDER}', params=params)

    @staticmethod
    def get_orders_list():
        return requests.get(f'{data.Url.BASE_URL}{data.Url.GET_ORDERS}')