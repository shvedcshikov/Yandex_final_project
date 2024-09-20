#Подключаем файлы и библиотеки
import configuration
import requests



#функция создания заказа
def create_order(body):
     return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER_URL,
                          json=body
                          )

#функция добавления в URL трека
def add_track_to_url(response):
     return configuration.GET_ORDER + '?t='+str(response.json()['track'])

#функция получения заказа по треку
def get_order_by_track(url_with_track) :
     return requests.get(configuration.URL_SERVICE+url_with_track
                     )
