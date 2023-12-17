import configuration
import requests
import data

#Создание нового заказа
def post_new_order(body_order):
    return requests.post(configuration.BASE_URL + configuration.ORDER_PATH,
                         json=body_order,
                         headers=data.headers)

#Получение заказа по треку
def get_order(track):
    return requests.get(configuration.BASE_URL + configuration.GET_ORDER_PATH,
                         params={"t":track},
                         headers=data.headers)