"""
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.
ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ
{
    "orders": []
}
вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', "r", encoding='utf-8') as json_file:
        data_from_file = json.load(json_file)
        data_from_file['orders'].append(
            {'item': item,
             'quantity': quantity,
             'price': price,
             'buyer': buyer,
             'date': date
             })
    with open('orders.json', "w", encoding='utf-8') as json_file:
        json.dump(data_from_file, json_file, indent=4, ensure_ascii=False)


write_order_to_json('ноутбук', '5', '100', 'Apple', '25.01.2002')
