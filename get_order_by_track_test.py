#Шведчиков Алексей, 21а когорта - Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data


def test_positive_assert():
    response = requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER_URL,
                         #обозначаем тип данных для body
                         json=data.order_body
                         )
    order_track = response.json()['track']
    url_with_track = configuration.GET_ORDER + '?t=' + str(order_track)
    order_response = requests.get(configuration.URL_SERVICE+url_with_track
                    )
    assert order_response.status_code==200
