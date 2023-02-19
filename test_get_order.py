import configuration
import requests
import create_order

#получаем заказ по сохраненному номеру
def test_get_order():
    return requests.get(configuration.URL_SERVICE+configuration.GET_ORDER+str(create_order.track))

response = test_get_order()
#print(response.status_code)

#сравниваем статус заказа
assert (response.status_code) == 200


