#Подключаем файлы и библиотеки
import configuration
import data
import requests



#функция создания заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER_URL,
                         #обозначаем тип данных для body
                         json=body
                         )
#Вызываем функцию и сохраняем ответ в переменную response
response = create_order(data.order_body)

#проверяем что там выводится
#print(response)
#print(response.json())

#функция добавления в URL трека
def add_track_to_url():
    order_track = response.json()['track']
    print(order_track)
    url_with_track=configuration.GET_ORDER + '?t='+str(order_track)
    return url_with_track

GET_ORDER_WITH_TRACK = add_track_to_url()

#функция получения заказа по треку
def get_order_by_track() :
    return requests.get(configuration.URL_SERVICE+GET_ORDER_WITH_TRACK
                    )
order_response = get_order_by_track()
#print(order_response.json())