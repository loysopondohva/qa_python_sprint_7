import allure
import pytest
from methods.order_methods import OrderMethods
import data

class TestOrder:
    @allure.title('Успешное создание заказа с сгенерированными данными')
    @pytest.mark.parametrize('scooter_color', data.OrderData.scooter_color)
    def test_create_order_random_data_success(self, scooter_color):
        order_data = data.OrderData.create_order_body
        order_data['color'] = scooter_color
        response = OrderMethods.order_create(order_data)
        assert response.status_code == 201
        assert data.Flags.SUCCESS_ORDER_CREATION in response.json()
        OrderMethods.order_cancel(response.json()['track'])

    @allure.title('Успешное получение списка заказов')
    def test_get_order_list_success(self):
        response = OrderMethods.get_orders_list()
        assert response.status_code == 200
        assert data.Flags.SUCCESS_GET_ORDER_LIST in response.json().keys()