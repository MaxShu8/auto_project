import random

page_load_timeout = 90
element_time_out = 60

token = "6951649128:AAHb3triQhmOw7omlTsVyN8waiTzurvvzjI"  # prod "NsCmDMTnLPxEge0YDaPnmA5XbRz4zb1oUR11HfxT"  # Мой токен "6951649128:AAHb3triQhmOw7omlTsVyN8waiTzurvvzjI"
chat_id = "939111831"
chat_id_predprod = '-1002166234481'  # Канал "Сайт Предпрод" (для отладки)
group_id_for_message_bot = '-1002488973536'  # Группа "Сообщения бота (Возовоз)"


token_debug_bot = "264498281:AAGpVqga9RQBKp7umUEcZsxENMYp3Oj2RQw"  # Для проверки Дадаты
chanel_vozovoz_error = "-1001285771517"  # Для проверки Дадаты


"""Данные для проверки предпрода"""
group_id_predprod = '-1002166638192'  # Группа "Сайт Предпрод"


"""Данные для мониторинга заявок"""
chat_id_prod = "-134461853"  # Группа "Боевой сайт"
token_vozovoz_bot = "176408403:AAHrPudaMSGowaCgHUM9Wr8fvrDy4eXtEYI"  # возовозовский бот


"""Данные для проверки авторизации"""
mobile = {'79990220038': 'an2015906'}
email = {'m.shumileiko@vozovoz.ru': 'an2015906'}


"""Данные для проверки мини-калькулятора"""
city_from = 'Москва'
city_to = 'Санкт-Петербург'
city_ru3 = 'Красноярск'
city_kz = 'Алматы'
city_kz1 = 'Астана'
city_by = 'Минск'
city_by1 = 'Витебск'
order_mini_calc = '220581294'
invalid_number_order_1 = '123'
invalid_number_order_2 = '888888888'
invalid_number_order_3 = 'абвгabc'
invalid_number_order_4 = '#$%^&'


"""Валюта"""
currency_rub = '₽'
currency_ber = 'Br'
currency_kzt = '₸'


"""Общие габариты"""
# Кол-во мест (выберем рандомно от 1 до 99)
value_places = str(random.randint(1, 99))

# Объем (выберем рандомно)
value_volume = str(round((random.random() * 10), 2))

# Вес (выберем рандомно)
value_weight = str(random.randint(1, 99))


"""Данные КА физ.лицо"""
# Физ.лицо
individual_fio = "Шумилейко Максим Валерьевич"
individual_fio_2 = "Иванкин Сергей Алексеевич"
individual_phone_full = "79990220038"
individual_phone = "9990220038"
individual_phone_2_full = "79817842624"
individual_phone_2 = "9817842624"
individual_email = "m.shumileiko@vozovoz.ru"
individual_payment_account = "123123123123"
individual_bik = "044525974"
incorrect_phone = "9999999999"
individual_order = "220581294"
individual_order_part = "220581"
individual_order_2 = "230450460"
individual_order_3 = "240912889"
invalid_individual_order = "888888888"
individual_order_with_text = "тЕСТОВЫЙ НОМЕР"


# Прочие данные
individual_fio_not_full = "Шумилей"
individual_fio_swap_places = "Максим Шумилейко"
individual_fio_low_case = "шумилейко максим"
individual_fio_with_spaces = " Шумилейко Максим Валерьевич "
individual_email_not_full = "@vozov"


add_individual_fio_ka = "Шумилейко Артем Валерьевич"
add_individual_phone_ru = "9679799793"
# add_individual_phone_bel = "777777777"
add_individual_phone_rf = f"900{str(random.randint(100, 999))}8888"
add_individual_phone_bel = f"77{str(random.randint(100, 999))}7777"
add_individual_phone_kz = f"777{str(random.randint(100, 999))}7777"
add_test_name_ka = "Тестовый пример"
add_test_name_ka_2 = "Тестовый примерчик"
add_test_name_ka_3 = "Тестовый примерище"


"""Данные КА юр.лицо"""
# Юр.лицо РФ
company_inn_number = "7702680818"
company_kpp_number = "770201001"
company_order_number = "240752045"
company_phone_number = "74957084213"
company_email_number = "otpravka@tinko.ru"
company_email_number_not_full = "@tink"
company_name = "ООО \"ТОРГОВЫЙ ДОМ ТИНКО\""
manager_name = "Менеджер"
company_name2 = "ООО \"ЭДЕЛЬВЕЙС\""
company_inn_number2 = "7838315731"
company_kpp_number2 = "784201001"


# Юр.лицо КЗ
company_inn_number_kz = "181240025812"
company_phone_number_kz = "77088651040"
company_email_number_kz = "tooelaran@gmail.com"
company_name_kz = "ELARAN"


"""Данные для тестовых оплат на деве"""
number_card_alfa_test = "4111111111111111"
cardholder_name_test = "SUCCESSPAYMENT"
expiration_date_test = "1224"
cvv_cvc_code_test = "123"
url_alfa_test = "https://alfa.rbsuat.com/"


"""Данные для тестовых оплат на проде Альфа"""
number_card_alfa = "2200153912350015"
expiration_date_alfa = "0834"
cvv_cvc_code_alfa = "735"
url_alfa = "https://pay.alfabank.ru/"


"""Данные для тестовых оплат на проде ВТБ"""
number_card_vtb = "2200240256664885"
expiration_date_vtb = "0831"
cvv_cvc_code_vtb = "970"
url_vtb = "https://"


"""Города"""
cities = ['Санкт-Петербург', 'Красноярск', 'Москва', 'Брянск', 'Сыктывкар', 'Ростов', 'Новосибирск', 'Барнаул',
          'Тюмень', 'Тверь', 'Волгоград', 'Екатеринбург', 'Астрахань', 'Мурманск', 'Нижний Новгород', 'Вологда',
          'Самара', 'Владивосток', 'Архангельск', 'Казань']


"""Всякие данные для разных тестов"""
# Для формы обратной связи
test_message = "Тестовое сообщение"
test_white_space = "   "
passw = "an2015906"
passw2 = "123123"




