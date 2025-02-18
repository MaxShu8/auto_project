import os
import random
import string
import time
import json
from pages.contacts_page import *
from Settings import *
import datetime
import Methods

# a = '196140, Санкт-Петербург г, Шушары п, Пулковское тер., д. 106/1, корп. 106/1'.replace(',', '').split()
# new = []
#
# for i in a:
#     if i == 'корп.' or i == 'кв-л':
#         continue
#     if not i in new:
#         new.append(i)
#
# new = ' '.join(new)
#
# print(new)


# cities = ['Санкт-Петербург', 'Красноярск', 'Москва']


# def choice_cities(cities):
#
#     city1 = random.choice(cities)
#     city2 = random.choice(cities)
#     if city2 == city1:
#         cities.remove(city1)
#         city2 = random.choice(cities)
#         cities.append(city1)
#     else:
#         pass
#
#     return print(city1), print(city2)
#
#
# for i in range(1, int(len(cities)+1)):
#     choice_cities(cities)

# url_cur = 'vozovoz.ru/update/fsfsf'
# url = 'vozovoz.ru/update/'
#
# if url in url_cur:
#     print('True')
#
# def a(test1, test2):
#     try:
#         start = time.time()
#         b()
#         end = time.time()
#         result = end - start
#         return print(round(result, 2))
#     except Exception as e:
#         print(e)
#
#
#
# def b():
#     print('b')
#
# def c():
#     print('c')


# def primer():
#     print('proverka')
#     a = '1'
#     b = '2'
#     c = '3'
#     return a, b, c
#
#
# a, b, c = primer()
#
# print(a)

# def hours_to_write(happy_hours):
#     week1 = happy_hours + 2
#     week2 = happy_hours + 4
#     week3 = happy_hours + 6
#     return week1, week2, week3
#
# result = hours_to_write(4)
# print(list(result)[0]) # Вывод: 6, 8, 10


# with open("json_file", "r") as f:
#     data = json.load(f)
#
# user_to_repos = {}
# for record in data:
#     user = record["response"]["data"]["number"]
#     print(user)
#     repo = record["repo"]["name"]
#     if user not in user_to_repos:
#         user_to_repos[user] = set()
#     user_to_repos[user].add(repo)
# print(len(user_to_repos), "records")


# time_now = datetime.datetime.now()
# current_time_day = time_now.day
# current_time_month = time_now.month
# print(time_now)
# print(current_time_day)
# print(current_time_month)

# for i in spisok:
#     str(i)
#     if name in spisok[0]:
#         print('good')
#     else:
#         print('ff')

# elem_text = 'Универсальный передаточный документ (УПД)'
# current_file = ''
# listdir = os.listdir(f"{os.getcwd()}\\files_for_tsts")
# if not listdir:
#     time.sleep(2)
# else:
#     current_file = listdir[0]
#
# if elem_text in current_file or 'Реквизиты ООО _Возовоз_' in current_file:
#     os.remove(f"{os.getcwd()}\\files_for_tsts\\{current_file}")
#     time.sleep(1)
#     pass
# else:
#     # Попробуем подождать и снова посмотреть в папку
#     time.sleep(10)
#     listdir = os.listdir(f"{os.getcwd()}\\files_for_tsts")
#     if not listdir:
#         print('Файл не загружен')
#     else:
#         current_file = listdir[0]
#     if elem_text in current_file:
#         os.remove(f"{os.getcwd()}\\files_for_tsts\\{current_file}")
#     else:
#         print('!!!')
#         # send_message_tg(f"{description}\nФайл не загружен: \"{elem_text}\"", token, chat_id)
#
# name1 = 'Niko'
# name2 = 'Mike'
#
# with open('request_for_transportation/names.txt', 'w') as f:
#     f.write(name1)
#     f.write(f'\n{name2}')
#
# file_data = open('request_for_transportation/names.txt', 'r')
# a = file_data.readline()
# b = file_data.readline()
#
# print(f'{a}{b}')

# corteg = 'https://xn--80aagbzadang7a5ahod.xn--p1ai/documents/'
#
# url_diligans = "https://tcdiligans.ru/documents"
# url_timelogistik = "https://timelogistik.ru/documents"
# url_t_technology = "https://t-technology.ru/documents"
# url_severtrans = "https://severtrans-spb.ru/documents"
# url_ugtrans = "https://ugtrans-tk.ru/documents"
# url_logtavrii = "https://xn--80aagbzadang7a5ahod.xn--p1ai/documents"


# add_individual_phone_bel = f"77{str(random.randint(100, 999))}7777"
# print(add_individual_phone_bel)
#
#
# rep = "+375 (77) 777-77-77"
# rep2 = rep.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
# print(rep2)

# domain = "dev"
#
# url_contractors_dev = f"https://vozovoz.{domain}/personal/contractors/"
#
# text = '07:00'
# text_1 = '07:00'.split(':')
# a = text[0]
#
# print(int(a))
# from datetime import datetime, timedelta
#
#
# def add_up_the_time(time_a, time_b):
#
#     # Определяем начальное время
#     start_time = datetime.strptime(time_a, "%H:%M").time()
#
#     # Определяем временной интервал, который хотим прибавить
#     add_hours = time_b
#
#     # Создаём объект timedelta
#     delta = timedelta(hours=add_hours)
#
#     # Сложение времени и временного интервала
#     result_time = (datetime.combine(datetime.min, start_time) + delta).time()
#
#     # Преобразуем результат обратно в строку
#     result_time_str = result_time.strftime("%H:%M")
#
#     print(result_time_str)
#
#
# add_up_the_time("17:50", 5)


def time_to_int(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes


a = "07:30"
result = time_to_int(a)
print(result)  # Вывод: 450



