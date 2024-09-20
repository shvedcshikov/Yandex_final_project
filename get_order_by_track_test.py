#Шведчиков Алексей, 21а когорта - Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_requests


def test_positive_assert():
    response = sender_stand_requests.create_order(data.order_body)
    print(response.json())
    url_with_track = sender_stand_requests.add_track_to_url(response)
    print(url_with_track)
    order_response = sender_stand_requests.get_order_by_track(url_with_track)
    print(order_response)
    assert order_response.status_code == 200
    return url_with_track, response, order_response


