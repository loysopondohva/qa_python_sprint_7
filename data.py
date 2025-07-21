import generators


class CourierData:
    create_courier_body = generators.generate_courier_body()
    create_courier_login = generators.generate_login()
    create_courier_password = generators.generate_password()
    random_courier_login_data = {'login': generators.generate_login(), 'password': generators.generate_password()}

class OrderData:
    create_order_body = generators.generate_order_body()
    scooter_color = [['BLACK'], ['GREY'], [''], (['BLACK'],['GREY'])]

class ResponseData:
    COURIER_CREATION_SUCCESS = {
        'code': 201,
        'message': {'ok': True}
    }
    COURIER_CREATION_FAILED_NO_LOGIN_PASSWORD = {
        'code': 400,
        'message': 'Недостаточно данных для создания учетной записи'
    }
    COURIER_CREATION_FAILED_ALREADY_EXIST = {
        'code': 409,
        'message': 'Этот логин уже используется. Попробуйте другой.'
    }
    COURIER_LOGIN_FAILED_NO_LOGIN_PASSWORD = {
        'code': 400,
        'message': 'Недостаточно данных для входа'
    }
    COURIER_LOGIN_NOT_FOUND = {
        'code': 404,
        'message': 'Учетная запись не найдена'
    }


class Flags:
    SUCCESS_ORDER_CREATION = 'track'
    SUCCESS_GET_ORDER_LIST = 'orders'