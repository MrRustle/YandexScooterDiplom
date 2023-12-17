# Коннов Кирилл, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


#Создание заказа и получение трека
def create_new_order():
    order_body = data.order_body.copy()
    response = sender_stand_request.post_new_order(order_body)
    return response.json()["track"]


def test_order():
    track = create_new_order()
    response = sender_stand_request.get_order(track)
    assert response.status_code == 200