import requests
import json
from Settings import *
import various_data
import datetime

dict_of_orders = {'250007916': 'вес места больше 500 кг; ширина больше 0,8',
                  '250007954': 'вес места больше 1000 кг; ширина больше 0,8',
                  '250007992': 'вес места больше 1500 кг; ширина больше 0,8',
                  '250008005': 'длина одного места больше или равна 4 м.',
                  '250008023': 'длина одного места больше или равна 6 м.',
                  '250008028': 'длина одного места больше или равна 8 м.',
                  '250008047': 'до 40 кг; длина больше 1,2 м',
                  '250008068': 'больше 40 кг; МТ+отвоз 1 кат',
                  '250008090': 'больше 40 кг; МТ+отвоз 2 кат и выше',
                  '250008094': 'больше 40 кг, длина больше 1,2 м',
                  '250008101': 'больше 40 кг, ширина больше 0,8 м',
                  '250008121': 'с разбором упаковки на адресе (без фото)',
                  '250008136': 'с разбором упаковки на терминале (без фото)',
                  '250008166': 'заказана услуга "ПБ"',
                  '250008229': 'заказана услуга "Паллетирование"',
                  '250008288': 'г. Москва Время заявки после 12 часов',
                  '250008418': 'г. Санкт-Петербург Время заявки после 12 часов',
                  '250008761': 'нет грузового лифта (получатель)',
                  '250010015': 'более 1 места 5 или 6 категории (получатель)',
                  '250010041': 'краевые города, начиная с 3 категории (получатель)',
                  '250010046': 'нет грузового лифта (отправитель)',
                  '250010053': 'более 1 места 5 или 6 категории (отправитель)',
                  '250010055': 'краевые города, начиная с 3 категории (отправитель)',
                  '250012082': 'экспресс-перевозка (Понедельник) Мск --> СПб',
                  '250012087': 'экспресс-перевозка (Вторник) Мск --> СПб',
                  '250012096': 'экспресс-перевозка (Среда) Мск --> СПб',
                  '250012099': 'экспресс-перевозка (Четверг) Мск --> СПб',
                  '250012103': 'экспресс-перевозка (Пятница) Мск --> СПб',
                  '250022271': 'экспресс-перевозка (Понедельник) Мск --> Екатеринбург',
                  '250022441': 'экспресс-перевозка (Вторник) Мск --> Екатеринбург',
                  '250022446': 'экспресс-перевозка (Среда) Мск --> Екатеринбург',
                  '250022454': 'экспресс-перевозка (Четверг) Мск --> Екатеринбург',
                  '250022459': 'экспресс-перевозка (Пятница) Мск --> Екатеринбург',
                  '250022537': 'экспресс-перевозка (Вторник) Мск --> Краснодар',
                  '250022544': 'экспресс-перевозка (Среда) Мск --> Краснодар',
                  '250023198': 'экспресс-перевозка (Понедельник) Мск --> Новосибирск',
                  '250023201': 'экспресс-перевозка (Вторник) Мск --> Новосибирск',
                  '250023204': 'экспресс-перевозка (Среда) Мск --> Новосибирск',
                  '250023206': 'экспресс-перевозка (Четверг) Мск --> Новосибирск',
                  '250023209': 'экспресс-перевозка (Пятница) Мск --> Новосибирск',
                  '250023296': 'экспресс-перевозка (Понедельник) Мск --> Хабаровск',
                  '250023325': 'экспресс-перевозка (Вторник) Мск --> Хабаровск',
                  '250023326': 'экспресс-перевозка (Среда) Мск --> Хабаровск',
                  '250023331': 'экспресс-перевозка (Четверг) Мск --> Хабаровск',
                  '250023336': 'экспресс-перевозка (Пятница) Мск --> Хабаровск',
                  '250023353': 'экспресс-перевозка (Понедельник) Мск --> Симферополь',
                  '250023386': 'экспресс-перевозка (Вторник) Мск --> Симферополь',
                  '250023409': 'экспресс-перевозка (Среда) Мск --> Симферополь',
                  '250023411': 'экспресс-перевозка (Четверг) Мск --> Симферополь',
                  '250023414': 'экспресс-перевозка (Пятница) Мск --> Симферополь',
                  '250023434': 'экспресс-перевозка (Понедельник) Мск --> СПб',
                  '250023435': 'экспресс-перевозка (Вторник) Мск --> СПб',
                  '250023440': 'экспресс-перевозка (Среда) Мск --> СПб',
                  '250023446': 'экспресс-перевозка (Четверг) Мск --> СПб',
                  '250023449': 'экспресс-перевозка (Пятница) Мск --> СПб',
                  '250023454': 'экспресс-перевозка (Понедельник) Мск --> Екатеринбург',
                  '250023457': 'экспресс-перевозка (Вторник) Мск --> Екатеринбург',
                  '250023458': 'экспресс-перевозка (Среда) Мск --> Екатеринбург',
                  '250023459': 'экспресс-перевозка (Четверг) Мск --> Екатеринбург',
                  '250023463': 'экспресс-перевозка (Пятница) Мск --> Екатеринбург',
                  '250027069': 'экспресс-перевозка (Понедельник) Мск --> Краснодар',
                  '250027078': 'экспресс-перевозка (Вторник) Мск --> Краснодар',
                  '250027095': 'экспресс-перевозка (Среда) Мск --> Краснодар',
                  '250022570': 'экспресс-перевозка (Четверг) Мск --> Краснодар',
                  '250022585': 'экспресс-перевозка (Пятница) Мск --> Краснодар',
                  '250041282': 'экспресс-перевозка (Понедельник) Мск --> Новосибирск',
                  '250041289': 'экспресс-перевозка (Вторник) Мск --> Новосибирск',
                  '250041295': 'экспресс-перевозка (Среда) Мск --> Новосибирск',
                  '250041299': 'экспресс-перевозка (Четверг) Мск --> Новосибирск',
                  '250041301': 'экспресс-перевозка (Пятница) Мск --> Новосибирск',
                  '250041304': 'экспресс-перевозка (Понедельник) Мск --> Хабаровск',
                  '250041308': 'экспресс-перевозка (Вторник) Мск --> Хабаровск',
                  '250041310': 'экспресс-перевозка (Среда) Мск --> Хабаровск',
                  '250041319': 'экспресс-перевозка (Четверг) Мск --> Хабаровск',
                  '250041322': 'экспресс-перевозка (Пятница) Мск --> Хабаровск',
                  '250041331': 'экспресс-перевозка (Понедельник) Мск --> Симферополь',
                  '250041337': 'экспресс-перевозка (Вторник) Мск --> Симферополь',
                  '250041339': 'экспресс-перевозка (Среда) Мск --> Симферополь',
                  '250041344': 'экспресс-перевозка (Четверг) Мск --> Симферополь',
                  '250041349': 'экспресс-перевозка (Пятница) Мск --> Симферополь'}

list_of_orders_days = ['250007916', '250007954', '250007992', '250008005', '250008023', '250008028', '250008047',
                       '250008068', '250008090', '250008094', '250008101', '250008121', '250008136', '250008166',
                       '250008229', '250008288', '250008418', '250008761', '250010015', '250010041', '250010046',
                       '250010053', '250010055', '250012082', '250022271', '250023198', '250023296', '250023353',
                       '250012087', '250022441', '250022537', '250023201', '250023325', '250023386', '250012096',
                       '250022446', '250022544', '250023204', '250023326', '250023409', '250012099', '250022454',
                       '250023206', '250023331', '250023411', '250012103', '250022459', '250023209', '250023336',
                       '250023414', '250023434', '250023435', '250023440', '250023446', '250023449', '250023454',
                       '250023457', '250023458', '250023459', '250023463', '250027069', '250027078', '250027095',
                       '250022570', '250022585', '250041282', '250041289', '250041295', '250041299', '250041301',
                       '250041304', '250041308', '250041310', '250041319', '250041322', '250041331', '250041337',
                       '250041339', '250041344', '250041349']

express_orders = ['250012082', '250012087', '250012096', '250012099', '250012103', '250022271', '250022441',
                  '250022446', '250022454', '250022459', '250022537', '250022544', '250023198', '250023201',
                  '250023204', '250023206', '250023209', '250023296', '250023325', '250023326', '250023331',
                  '250023336', '250023386', '250023409', '250023411', '250023414']

class GetExistData:
    """Запрос данных по имеющемуся заказу и создание заказа на его основании"""

    def __init__(self):
        self.base_url_api = 'https://vozovoz.ru/api/'
        self.token = '?token=l1l7ewao3g3fq7PhzPAc7pf67yNwzDaJyohtaFzU'  #  BL4qFLqwKVnnPlFtCTkYPqB9RvRQxfjvmSfe6V36  l1l7ewao3g3fq7PhzPAc7pf67yNwzDaJyohtaFzU
        self.token_org = '?token=BL4qFLqwKVnnPlFtCTkYPqB9RvRQxfjvmSfe6V36'
        self.token_dev = '?token=zKj90ZSz389J15XG2gKfei0OiTitisjaAwQ7Mkhy'  # мой ЛК +79990220038
        self.token_test_prod = "?token=NsCmDMTnLPxEge0YDaPnmA5XbRz4zb1oUR11HfxT"  # тестовый прод +79910012655

    def parsing_json(self, json_dict):

        # Достанем все, что находится в data
        list_of_data = json_dict['response']

        # Достанем basePrice и price
        new_base_price = list_of_data['basePrice']
        new_price = list_of_data['price']

        # Достанем все услуги с ценами, которые находятся в service
        list_of_service = list_of_data['service']
        new_dict_of_prices = {}
        for i in list_of_service:
            service = i['name']
            price_of_service = i['price']
            new_dict_of_prices[service] = price_of_service
        # print(f'Стоимость: {new_base_price}, С учетом скидок: {new_price}, \n{new_dict_of_prices}')
        return new_base_price, new_price, new_dict_of_prices

    def get_data_of_exist_order(self, order):

        day_start = ''
        day_end = ''

        json_action_get = {
            "object": "order",
            "action": "get",
            "params": {
                "filters": {
                    "number": [f"{order}"]
                },
                "limit": 100,  # ограничение количества результатов выборки
                "offset": 0,  # смещение по выборке
                "mode": {
                    # "isCanceled": False, # Должен ли заказ быть отменён для попадания в выборку
                    "isGiven": False,  # Должен ли заказ быть выдан для попадания в выборку
                    "isPaid": False,  # Должен ли быть оплачен заказ для попадания в выборку
                    "isTaken": False
                }
            }
        }

        url_post = self.base_url_api + self.token_test_prod

        # Запрос данных о заказе (метод POST)
        response_post = requests.post(url_post, json=json_action_get)

        # Проверка статус-кода
        assert response_post.status_code == 200

        # Json в формате словаря
        json_dict = response_post.json()

        # Достанем все, что находится в data
        list_of_data = json_dict['response']['data'][0]

        # Достанем number, basePrice и price
        number = list_of_data['number']
        reference_base_price = list_of_data['basePrice']
        reference_price = list_of_data['price']

        # дополнительно достанем дату начала/конца рейса, если заказ из списка экспрессных
        if order in list_of_orders_days:
            transportation_start_date = list_of_data['gateway']['dispatch']['point']['date'].split('T')[0]

            components_data_start = transportation_start_date.split("-")
            year_of_start = int(components_data_start[0])
            month_of_start = int(components_data_start[1])
            day_of_start = int(components_data_start[2])

            # Создание объекта datetime
            date_1 = datetime.datetime(year_of_start, month_of_start, day_of_start)

            # Вывод дня недели
            day_start = date_1.weekday()

            # Найдем дату прибытия
            transportation_end_date = list_of_data['gateway']['destination']['point']['date'].split('T')[0]

            components_data_end = transportation_end_date.split("-")
            year_of_end = int(components_data_end[0])
            month_of_end = int(components_data_end[1])
            day_of_end = int(components_data_end[2])

            # Создание объекта datetime
            date_2 = datetime.datetime(year_of_end, month_of_end, day_of_end)

            # Вывод дня недели
            day_end = date_2.weekday()

        else:
            pass

        # достанем терминал или адрес в отправлении
        point_dispatch = list_of_data['gateway']['dispatch']['point']
        point_disp = 'address'
        for i in point_dispatch.keys():
            if i == 'terminal':
                point_disp = i
            else:
                pass

        # достанем терминал или адрес в получении
        point_destination = list_of_data['gateway']['destination']['point']
        point_dest = 'address'
        for i in point_destination.keys():
            if i == 'terminal':
                point_dest = i
            else:
                pass

        # Достанем все услуги с ценами, которые находятся в service
        list_of_service = list_of_data['service']
        reference_dict_of_prices = {}
        for i in list_of_service:
            service = i['name']
            price_of_service = i['price']
            reference_dict_of_prices[service] = price_of_service

        return number, reference_base_price, reference_price, reference_dict_of_prices, day_start, day_end, point_disp, point_dest

    def get_data_of_date_order(self, dispatch, destination, day_start, day_end, point_disp, point_dest, number):

        """Запросим доступные даты для расчета заказа, чтобы не было ошибки"""
        dispatch_date = ''
        destination_date = ''

        json_schedule_get = {
            "object": "schedule",
            "action": "get",
            "params": {
                "dispatch": {f"{point_disp}": f"{dispatch}"},
                "destination": {f"{point_dest}": f"{destination}"}
                }
            }

        url_post = self.base_url_api + self.token_test_prod

        # Запрос данных о датах (метод POST)
        response_post = requests.post(url_post, json=json_schedule_get)

        # Проверка статус-кода
        assert response_post.status_code == 200

        # Json в формате словаря
        json_dict = response_post.json()

        # Достанем все, что находится в data
        list_of_data = json_dict['response']

        if day_start in [0, 1, 2, 3, 4, 5, 6] and number not in ['250008288', '250008418']:  # тут проверяем если приходит нужный день недели

            # Получим все доступные даты отправления
            for k, v in list_of_data.items():

                dispatch_date = k.split("-")
                year = int(dispatch_date[0])
                month = int(dispatch_date[1])
                day_create = int(dispatch_date[2])

                # Создание объекта datetime
                date = datetime.datetime(year, month, day_create)

                # Вывод дня недели
                start_day_of_week = date.weekday()

                # Получим текущий день недели
                # current_day_of_week = datetime.datetime.now()
                current_date = datetime.datetime.now().strftime('%Y-%m-%d')

                if day_start == start_day_of_week and k != current_date:
                    dispatch_date = k
                    break

            dictionary = list_of_data[dispatch_date]['destination']

            # сделаем из словаря список и получим первое значение (чтобы далее искать по нему)
            list_of_data = list(dictionary)

            find_first_value = list_of_data[0]
            dict_date_need = dictionary[find_first_value]

            need_end_dates = list(dict_date_need)   # ['2024-07-25', '2024-07-26', '2024-07-27', '2024-07-29', '2024-07-30', '2024-07-31']
            next_date = 0

            for d_date in need_end_dates:
                destination_date = d_date.split("-")
                year = int(destination_date[0])
                month = int(destination_date[1])
                day_create = int(destination_date[2])

                # Создание объекта datetime
                date = datetime.datetime(year, month, day_create)

                # Вывод дня недели
                end_day_of_week = date.weekday()

                if day_end == end_day_of_week:
                    if number in ['250041304', '250041308', '250041310']:
                        """Отдельное условие, чтобы выбрать через неделю для заказов в Хабаровск"""

                        if next_date == 1:
                            destination_date = d_date
                            break
                        else:
                            next_date += 1
                    else:
                        destination_date = d_date
                        break

                elif number in express_orders:
                    destination_date = d_date
                    break

                if day_end == 6:
                    if next_date == 1:
                        destination_date = d_date
                        break
                    else:
                        next_date += 1

        elif number in ['250008288', '250008418']:

            # Получим первые доступные даты для отправки/прибытия
            for k, v in list_of_data.items():
                dispatch_date = k
                dictionary = v['destination']

                # сделаем из словаря список и получим первое значение (чтобы далее искать по нему)
                list_of_data = list(dictionary)
                find_first_value = list_of_data[0]  # узнаем первый элемент словаря (23:00), чтобы искать по нему

                # подставим ключ, чтобы найти его значение
                dict_date_need = dictionary[find_first_value]

                need = list(dict_date_need)
                destination_date = need[1]
                break

        else:
            print('Не удалось рассчитать дату')

        return dispatch_date, destination_date

    # def create_price_with_simular_data(self):
    #
    #     json_action_set = {
    #         "object": "order",
    #         "action": "set",
    #         "params": {
    #             "cargo": {
    #                 "category": "",
    #                 "correspondence": False,
    #                 "dimension": {
    #                     "max": {
    #                         "height": 1.24,
    #                         "length": 1.24,
    #                         "weight": 550,
    #                         "width": 1.24
    #                     },
    #                     "quantity": 2,
    #                     "volume": 1.89,
    #                     "weight": 1100
    #                 },
    #                 "insurance": "",
    #                 "insuranceNdv": True,
    #                 "wrapping": {
    #                     "palletCollar": 0,
    #                     "hardPackageVolume": 0
    #                 }
    #             },
    #             "customId": "",
    #             "gateway": {
    #                 "dispatch": {
    #                     "point": {
    #                         "location": "Москва",
    #                         "address": "Москва, ул Никулинская, д 35, стр 1",
    #                         "date": f"2024-07-16T00:00:00"
    #                     },
    #                     "service": {
    #                         "needLoading": "",
    #                         "scannedConsignationNote": False,
    #                         "specificLoading": "",
    #                         "retrieveAD": []
    #                     },
    #                     "customer": {
    #                         "email": "",
    #                         "type": "corporation",
    #                         "companyName": "Общество с ограниченной ответственностю Моряк",
    #                         "name": "ООО Моряк",
    #                         "phone": "79589584545",
    #                         "inn": "9725129600",
    #                         "kpp": "",
    #                         "sendCode": True
    #                     }
    #                 },
    #                 "destination": {
    #                     "point": {
    #                         "location": "Краснодар",
    #                         "address": "Краснодар г, Бульварная 22",
    #                         "date": "2024-07-19T00:00:00",
    #                         "driverComment": "",
    #                         "time": {
    #                             "start": "09:00",
    #                             "end": "18:00",
    #                             "fix": False
    #                         }
    #                     },
    #                     "service": "",
    #                     "customer": {
    #                         "type": "corporation",
    #                         "companyName": "ООО Белый Кит",
    #                         "name": "ООО Белый Кит",
    #                         "phone": [
    #                             "79589586565"
    #                         ],
    #                         "kpp": "",
    #                         "inn": "7718915222",
    #                         "email": "m.shumileiko@vozovoz.ru",
    #                         "sendCode": False
    #                     }
    #                 }
    #             },
    #             "payer": {
    #                 "companyName": "ООО Моряк",  # Наименование компании, если юр.лицо
    #                 "email": "m.shumileiko@vozovoz.ru",  # e-mail лица
    #                 "name": "ООО Моряк",  # ФИО физического/контактного лица
    #                 "phone": "79589584545",  # или массив телефонов
    #                 "sendCode": True,  # посылать СМС с кодом
    #                 "type": "corporation",  # юр. лицо, или "individual" для физ. лиц
    #                 "inn": "9725129600",  # ИНН, обязательный для юр. лица плательщика
    #                 "kpp": ""  # КПП
    #             },
    #             "promoCode": ""
    #         }
    #     }
    #
    #     url_post = self.base_url_api + self.token
    #
    #     # Запрос на создание заказа (метод POST)
    #     response_post = requests.post(url_post, json=json_action_set)
    #     print(response_post)
    #
    #     # Проверка статус-кода
    #     assert response_post.status_code == 200
    #     if response_post.status_code == 200:
    #         print(
    #             f'\033[0;42m Проверка статус-кода --- УСПЕШНО!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_post.status_code}]')
    #     else:
    #         print(
    #             f'\033[0;41m Проверка статус-кода --- ПРОВАЛ!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_post.status_code}]')
    #
    #     json_response = json.loads(response_post.text)

    # def compare_data_of_orders(self, reference_base_price, reference_price, dict_of_prices):

    def get_price_with_simular_data(self, number, day_start, day_end, point_disp, point_dest):

        """Запросы расчета стоимости заказа по имеющимся данным эталонных заявок"""
        json_price_get = {}

        if number == '250007916':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.24,
                                "length": 1.24,
                                "weight": 550,
                                "width": 1.24
                            },
                            "quantity": 2,
                            "volume": 1.89,
                            "weight": 1100
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "address": "2-й Котляковский пер, д 2А",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "email": "",
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "name": "ООО \"Моряк\"",
                                "phone": "79589584545",
                                "inn": "9725129600",
                                "kpp": "",
                                "sendCode": True
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "address": "Краснодар",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "name": "ООО \"Белый кит\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "kpp": "",
                                "inn": "7718915222",
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "companyName": "ООО \"Моряк\"",  # Наименование компании, если юр.лицо
                        "email": "m.shumileiko@vozovoz.ru",  # e-mail лица
                        "name": "ООО \"Моряк\"",  # ФИО физического/контактного лица
                        "phone": "79589584545",  # или массив телефонов
                        "sendCode": True,  # посылать СМС с кодом
                        "type": "corporation",  # юр. лицо, или "individual" для физ. лиц
                        "inn": "9725129600",  # ИНН, обязательный для юр. лица плательщика
                        "kpp": ""  # КПП
                    },
                    "promoCode": ""
                }
            }

        elif number == '250007954':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Домодедово', 'Иркутск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.15,
                                "length": 1.15,
                                "width": 1.15,
                                "weight": 1100
                            },
                            "quantity": 2,
                            "volume": 1.51,
                            "weight": 2200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Домодедово",
                                "address": "",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Иркутск",
                                "address": "",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",  # юр. лицо, или "individual" для физ. лиц
                        "companyName": "ООО \"Белый кит\"",  # Наименование компании, если юр.лицо
                        "inn": "7718915222",  # ИНН, обязательный для юр. лица плательщика
                        "kpp": "",  # КПП
                        "email": "m.shumileiko@vozovoz.ru",  # e-mail лица
                        "name": "ООО \"Белый кит\"",  # ФИО физического/контактного лица
                        "phone": "79589586565",  # или массив телефонов
                        "sendCode": True  # посылать СМС с кодом
                    },
                    "promoCode": ""
                }
            }

        elif number == '250007992':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Краснодар', 'Красноярск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 1,
                                "weight": 1550
                            },
                            "quantity": 1,
                            "volume": 1.89,
                            "weight": 1550
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Краснодар",
                                "address": "",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Красноярск",
                                "address": "",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008005':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Челябинск', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 4,
                                "width": 1,
                                "weight": 350
                            },
                            "quantity": 1,
                            "volume": 6,
                            "weight": 350
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Челябинск",
                                "address": "",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "address": "",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008023':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Красноярск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 5.9,
                                "width": 1,
                                "weight": 400
                            },
                            "quantity": 1,
                            "volume": 5.9,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "address": "2-й Котляковский пер, д 2А",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Красноярск",
                                "address": "Красноярск",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008028':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 0.61,
                                "length": 8,
                                "width": 0.61,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 3.12,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "address": "2-й Котляковский пер, д 2А",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "address": "Санкт-Петербург",
                                "date": f"{destination_date}",
                                "driverComment": ""
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008047':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Краснодар', 'Липецк', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 0.65,
                                "length": 1.5,
                                "width": 0.65,
                                "weight": 30
                            },
                            "quantity": 1,
                            "volume": 0.66,
                            "weight": 30
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "hardPackageVolume": 0.66
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Краснодар",
                                "address": "Краснодар",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Липецк",
                                "address": "Липецк",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008068':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Казань', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.8,
                                "weight": 250
                            },
                            "quantity": 4,
                            "volume": 1.51,
                            "weight": 1000
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "hardPackageVolume": 1.66
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Казань",
                                "terminal": "1f32b26c-af5b-11e9-bba1-00155df27330",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "address": "Краснодар",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008090':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Самара', 'Саратов', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.8,
                                "weight": 200
                            },
                            "quantity": 9,
                            "volume": 3.02,
                            "weight": 1800
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "hardPackageVolume": 3.32
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Самара",
                                "address": "Самара",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Саратов",
                                "address": "Саратов",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008094':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Краснодар', 'Липецк', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 0.95,
                                "length": 1.5,
                                "width": 0.95,
                                "weight": 300
                            },
                            "quantity": 1,
                            "volume": 1.42,
                            "weight": 300
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "hardPackageVolume": 1.64
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Краснодар",
                                "address": "Краснодар",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Липецк",
                                "address": "Липецк",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008101':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Красноярск', 'Казань', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "hardPackageVolume": 1.38
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Красноярск",
                                "address": "Красноярск",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Казань",
                                "address": "Казань",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008121':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Казань', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.8,
                                "weight": 250
                            },
                            "quantity": 4,
                            "volume": 1.51,
                            "weight": 1000
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "hardPackageVolumeUOD": 1.66
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Казань",
                                "address": "Казань",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "address": "Краснодар",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008136':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Краснодар', 'Липецк', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 0.91,
                                "length": 1.2,
                                "width": 0.91,
                                "weight": 300
                            },
                            "quantity": 1,
                            "volume": 1.04,
                            "weight": 300
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "hardPackageVolumeUOD": 1.21
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Краснодар",
                                "address": "Краснодар",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Липецк",
                                "terminal": "56cc8f0d-73d4-11ee-ae69-ac1f6b447939",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008166':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Нижний Новгород', 'Самара', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.12,
                                "length": 1.15,
                                "width": 0.75,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.01,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 1.15
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Нижний Новгород",
                                "address": "Нижний Новгород",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Самара",
                                "address": "Самара",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008229':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Липецк', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1,
                                "width": 1,
                                "weight": 300
                            },
                            "quantity": 1,
                            "volume": 1.5,
                            "weight": 300
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletizingExtraPackageVolume": 1.5
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Липецк",
                                "terminal": "56cc8f0d-73d4-11ee-ae69-ac1f6b447939",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "address": "Санкт-Петербург",
                                "date": f"{destination_date}",
                                "driverComment": ""
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659654585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008288':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Иркутск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.15,
                                "length": 1.15,
                                "width": 1.15,
                                "weight": 150
                            },
                            "quantity": 4,
                            "volume": 1.51,
                            "weight": 600
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "address": "2-й Котляковский пер, д 2А",
                                "date": f"{dispatch_date}",
                                "time": {
                                    "start": "12:30",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Иркутск",
                                "address": "Иркутск",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008418':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Санкт-Петербург', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.15,
                                "length": 1.15,
                                "width": 1.15,
                                "weight": 180
                            },
                            "quantity": 3,
                            "volume": 1.51,
                            "weight": 500
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "address": "Санкт-Петербург",
                                "date": f"{dispatch_date}",
                                "time": {
                                    "start": "14:30",
                                    "end": "19:30",
                                    "fix": False
                                }
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "address": "Краснодар",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250008761':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Челябинск', 'Саратов', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 30
                            },
                            "quantity": 3,
                            "volume": 1,
                            "weight": 90
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Челябинск",
                                "address": "Челябинск",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Саратов",
                                "address": "Саратов",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": {
                                "needLoading": {
                                    "used": True,
                                    "floor": 2,
                                    "hasLift": False
                                }
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250010015':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Казань', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.45,
                                "length": 1.45,
                                "width": 1.45,
                                "weight": 240
                            },
                            "quantity": 3,
                            "volume": 6.4,
                            "weight": 480
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCustomer": 1
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Казань",
                                "address": "Казань",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "address": "Краснодар",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": {
                                "needLoading": {
                                    "used": True,
                                    "floor": 9,
                                    "hasLift": True
                                }
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250010041':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Нижний Новгород', 'Всеволожск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.2,
                                "length": 1.2,
                                "width": 0.8,
                                "weight": 150
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 150
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Нижний Новгород",
                                "address": "",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": "",
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Всеволожск",
                                "address": "",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "10:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": {
                                "needLoading": {
                                    "used": True,
                                    "floor": 5,
                                    "hasLift": True
                                }
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250010046':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Челябинск', 'Саратов', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 80
                            },
                            "quantity": 3,
                            "volume": 1,
                            "weight": 90
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Челябинск",
                                "address": "Челябинск",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": {
                                    "used": True,
                                    "floor": 2,
                                    "hasLift": False
                                },
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Саратов",
                                "address": "Саратов",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "10:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250010053':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Казань', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 0.8,
                                "weight": 300
                            },
                            "quantity": 3,
                            "volume": 3.02,
                            "weight": 900
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCustomer": 3,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Казань",
                                "address": "Казань",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": {
                                    "used": True,
                                    "floor": 5,
                                    "hasLift": True
                                },
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "address": "Краснодар",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250010055':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Всеволожск', 'Красноярск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.2,
                                "length": 1.2,
                                "width": 0.8,
                                "weight": 150
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 150
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Всеволожск",
                                "address": "Всеволожск",
                                "date": f"{dispatch_date}"
                            },
                            "service": {
                                "needLoading": {
                                    "used": True,
                                    "floor": 4,
                                    "hasLift": True
                                },
                                "scannedConsignationNote": False,
                                "specificLoading": "",
                                "retrieveAD": []
                            },
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Красноярск",
                                "address": "Красноярск",
                                "date": f"{destination_date}",
                                "driverComment": "",
                                "time": {
                                    "start": "09:00",
                                    "end": "18:00",
                                    "fix": False
                                }
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250012082':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250012087':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79589584545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79589584545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250012096':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250012099':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250012103':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250022271':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250022441':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250022446':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250022454':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250022459':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250022537':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "terminal": "24682c78-8a09-11ea-bbd1-00155d069401",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250022544':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "terminal": "24682c78-8a09-11ea-bbd1-00155d069401",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023198':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023201':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023204':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023206':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023209':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023296':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023325':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023326':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023331':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023336':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023353':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023386':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023409':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023411':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023414':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023434':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023435':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023440':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023446':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023449':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Санкт-Петербург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Санкт-Петербург",
                                "terminal": "186eb895-f638-11ed-b19c-0cc47a3455a3",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023454':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023457':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023458':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023459':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79589586565"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250023463':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Екатеринбург', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Екатеринбург",
                                "terminal": "2eb331e1-b9c8-11e9-bb92-00155dec7107",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250027069':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "terminal": "24682c78-8a09-11ea-bbd1-00155d069401",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250027078':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "terminal": "24682c78-8a09-11ea-bbd1-00155d069401",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250027095':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "terminal": "24682c78-8a09-11ea-bbd1-00155d069401",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250022570':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "terminal": "24682c78-8a09-11ea-bbd1-00155d069401",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250022585':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Краснодар', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Краснодар",
                                "terminal": "24682c78-8a09-11ea-bbd1-00155d069401",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041282':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041289':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041295':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041299':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041301':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Новосибирск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Новосибирск",
                                "terminal": "5b439c86-5727-11ec-af02-506b4b6ad201",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041304':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041308':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041310':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041319':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041322':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Хабаровск', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Хабаровск",
                                "terminal": "59b2236c-3bf1-11e9-813f-00155d903d0c",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041331':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый кит\"",
                                "inn": "7718915222",
                                "kpp": "",
                                "name": "ООО \"Белый кит\"",
                                "phone": "79589586565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79589584545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый кит\"",
                        "inn": "7718915222",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый кит\"",
                        "phone": "79589586565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041337':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041339':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 2,
                            "volume": 1,
                            "weight": 400
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": "79658966565",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": [
                                    "79658964545"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Северный Олень\"",
                        "inn": "7743440565",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Северный Олень\"",
                        "phone": "79658966565",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041344':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1.5,
                                "length": 1.2,
                                "width": 0.5,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 0.94,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Моряк\"",
                                "inn": "9725129600",
                                "kpp": "",
                                "name": "ООО \"Моряк\"",
                                "phone": "79659654545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": [
                                    "79659658585"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Моряк\"",
                        "inn": "9725129600",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Моряк\"",
                        "phone": "79659654545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        elif number == '250041349':

            # Получим валидные даты
            dispatch_date, destination_date = self.get_data_of_date_order('Москва', 'Симферополь', day_start, day_end, point_disp, point_dest, number)

            json_price_get = {
                "object": "price",
                "action": "get",
                "params": {
                    "cargo": {
                        "category": "",
                        "correspondence": False,
                        "dimension": {
                            "max": {
                                "height": 1,
                                "length": 1.2,
                                "width": 1,
                                "weight": 200
                            },
                            "quantity": 1,
                            "volume": 1.2,
                            "weight": 200
                        },
                        "insurance": "",
                        "insuranceNdv": True,
                        "wrapping": {
                            "palletCollar": 0,
                            "hardPackageVolume": 0
                        }
                    },
                    "customId": "",
                    "gateway": {
                        "dispatch": {
                            "point": {
                                "location": "Москва",
                                "terminal": "0f807fbb-f367-11eb-a8b9-7cfe909e8460",
                                "date": f"{dispatch_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Белый медведь\"",
                                "inn": "7721479569",
                                "kpp": "",
                                "name": "ООО \"Белый медведь\"",
                                "phone": "79659854545",
                                "sendCode": True,
                                "email": ""
                            }
                        },
                        "destination": {
                            "point": {
                                "location": "Симферополь",
                                "terminal": "6bb9b7ea-a39d-11e9-bba1-00155df27330",
                                "date": f"{destination_date}"
                            },
                            "service": "",
                            "customer": {
                                "type": "corporation",
                                "companyName": "ООО \"Северный Олень\"",
                                "inn": "7743440565",
                                "kpp": "",
                                "name": "ООО \"Северный Олень\"",
                                "phone": [
                                    "79659657474"
                                ],
                                "email": "m.shumileiko@vozovoz.ru",
                                "sendCode": False
                            }
                        }
                    },
                    "payer": {
                        "type": "corporation",
                        "companyName": "ООО \"Белый медведь\"",
                        "inn": "7721479569",
                        "kpp": "",
                        "email": "m.shumileiko@vozovoz.ru",
                        "name": "ООО \"Белый медведь\"",
                        "phone": "79659854545",
                        "sendCode": True
                    },
                    "promoCode": ""
                }
            }

        else:
            print(f'{number} - указанный заказ не обнаружен!')

        url_post = self.base_url_api + self.token_test_prod

        # Запрос данных о датах (метод POST)
        response_post = requests.post(url_post, json=json_price_get)

        # Проверка статус-кода
        assert response_post.status_code == 200

        # Json в формате словаря
        json_dict = response_post.json()

        new_base_price, new_price, new_dict_of_prices = self.parsing_json(json_dict)

        return new_base_price, new_price, new_dict_of_prices

    def comparison_data_orders(self, number):
        """Сравним полученные данные эталонного и нового заказов"""

        number, reference_base_price, reference_price, reference_dict_of_prices, day_start, day_end, point_disp, point_dest = self.get_data_of_exist_order(number)

        # Получим данные нового заказа
        new_base_price, new_price, new_dict_of_prices = self.get_price_with_simular_data(number, day_start, day_end, point_disp, point_dest)

        reference_dict = reference_dict_of_prices
        new_dict = new_dict_of_prices
        print(f'\033[0;42m=====Проверка по эталонному заказу: {number}=====\033[0;0m')
        msg = ''

        if reference_base_price != new_base_price and reference_price != new_price:

            print(f'Стоимость базовая: {reference_base_price} не соответствует {new_base_price}')
            print(f'Стоимость со скидкой: {reference_price} не соответствует {new_price}')
            msg = f'Стоимость: {reference_price} не соответствует {new_price}\n'

            # достанем данные из эталонного словаря и сравним с данными нового
            for rk, rv in reference_dict.items():
                for nk, nv in new_dict.items():
                    if rk == nk:
                        if rv != nv:
                            print(f'В услуге "{rk}" не соответствует стоимость: ОР {rv} || ФР {nv}')
                            msg += f'🔹В услуге "{rk}" не соответствует стоимость: ОР {rv} || ФР {nv}\n'
                        else:
                            pass
            send_message_tg(f'🚚 Проверка по заказу: {number} \n📋 Описание заказа: {dict_of_orders[number]}\n\n{msg}', token_vozovoz_bot, group_id_predprod)   # был chat_id
            send_message_tg(f'🚚 Проверка по заказу: {number} \n📋 Описание заказа: {dict_of_orders[number]}\n\n{msg}', token, chat_id_predprod)

            return 1
        else:
            print('🟢 Расхождений в стоимости не обнаружено!')
            # msg = '🟢 Расхождений в стоимости не обнаружено!'
            return 0


# Запрашиваем данные стоимости по заказам
get = GetExistData()


def check_request_orders():
    send_message_tg(f'🔔 Запуск проверки стоимостей на основе эталонных заявок...\n', token, group_id_predprod)
    send_message_tg(f'🔔 Запуск проверки стоимостей на основе эталонных заявок...\n', token, chat_id_predprod)
    counter_success = 0
    counter_not_pass = 0
    number_of_not_pass_orders = ''
    counter_failed = 0
    number_of_failed_order = ''

    for number_of_order in dict_of_orders.keys():

        try:
            figure = get.comparison_data_orders(number_of_order)
            if figure == 1:
                counter_not_pass += figure
                number_of_not_pass_orders += number_of_order
            else:
                counter_success += 1

        except Exception as e:
            print(f'🔴 Запрос по заказу {number_of_order} не обработан...попробуем снова...\nОшибка: {e}')
            send_message_tg(f'🔴 Запрос с заказом {number_of_order} не обработан...попробуем снова...\nОшибка: {e}', token_vozovoz_bot, group_id_predprod)
            send_message_tg(f'🔴 Запрос с заказом {number_of_order} не обработан...попробуем снова...\nОшибка: {e}', token, chat_id_predprod)

            try:
                figure = get.comparison_data_orders(number_of_order)
                if figure == 1:
                    counter_not_pass += figure
                    number_of_not_pass_orders += number_of_order
                else:
                    counter_success += 1

            except Exception as e:
                send_message_tg(f'🔴 Запрос с заказом {number_of_order} не обработан во второй раз...\nОшибка: {e}', token_vozovoz_bot, group_id_predprod)
                send_message_tg(f'🔴 Запрос с заказом {number_of_order} не обработан...попробуем снова...\nОшибка: {e}', token, chat_id_predprod)
                counter_failed += 1
                number_of_failed_order += number_of_order
                continue
            continue

    send_message_tg(f'✅ Результаты проверки по эталонам!\n🔹Заявок всего: {counter_success + counter_not_pass + counter_failed}\n🔹Заявок с разницей в стоимости: {counter_not_pass}\n🔹Обработано с ошибкой: {counter_failed}', token_vozovoz_bot, chat_id_prod)
    send_message_tg(f'✅ Результаты проверки по эталонам!\n🔹Заявок всего: {counter_success + counter_not_pass + counter_failed}\n🔹Заявок с разницей в стоимости: {counter_not_pass}\n🔹Обработано с ошибкой: {counter_failed}', token, chat_id_predprod)


check_request_orders()


# list_of_orders = ['250027078']
#
# for number_of_order in list_of_orders:
# # for number_of_order in dict_of_orders.keys():
#
#     try:
#         get.comparison_data_orders(number_of_order)
#
#     except Exception as e:
#         print(f'🔴 Запрос по заказу {number_of_order} не обработан...попробуем снова...\nОшибка: {e}')
#         send_message_tg(f'🔴 Запрос с заказом {number_of_order} не обработан...попробуем снова...\nОшибка: {e}', token, chat_id)
#         try:
#             get.comparison_data_orders(number_of_order)
#         except Exception as e:
#             send_message_tg(f'🔴 Запрос с заказом {number_of_order} снова не обработан...\nОшибка: {e}', token, chat_id)
#             continue
#         continue

