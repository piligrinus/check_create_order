import configuration
import data
import requests

#создаем заказ
def create_new_order(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставялем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


response = create_new_order(data.order_body)

#print(response.status_code)
#print(response.json())

#запоминаем номер заказа
track = response.json()["track"]
#print(track)