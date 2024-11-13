import json
import datetime
import os
import time

import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
import Methods
import site_objects
import various_data
from various_data import *

# Запуск драйвера
def driver_start():
    driver = None

    try:
        chrome_options = webdriver.ChromeOptions()

        # Добавим фоновый режим
        # chrome_options.add_argument('--headless')
        # Добавим режим инкогнито
        # chrome_options.add_argument('--incognito')

        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-cache')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # chrome_options.add_argument('--incognito')

        prefs = {"download.default_directory": f"{os.getcwd()}\\downloads"}

        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=chrome_options)  # service=ChromeService(ChromeDriverManager().install()),

        # # Прикрутим драйвер-менеджер для автообновления драйвера
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.implicitly_wait(5)

    except Exception as e:
        err = f"\nОшибка при установке драйвера:"
        send_message_tg(f'{err}\nПроизошла ошибка в тесте\n{e}', token, chat_id)

    return driver


# отправка сообщений в телегу
def send_message_tg(msg, token, chat_id):

    headers = {'Content-Type': 'application/json'}
    body = json.dumps({
        "chat_id": chat_id,
        "text": msg,
        "disable_notification": False
    })

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, headers=headers, data=body)
    return msg

def send_photo_tg(params, token, chat_id,  desc=''):

    # Проверим, есть ли директория для скриншотов (если нет, то создадим)
    if not os.path.isdir("screenshots"):
        os.mkdir(os.getcwd() + '\\screenshots')

    # Придумаем имя скриншоту (подгоним к текущей дате создания)
    actual_date = datetime.datetime.now().strftime("%H.%M.%S %d.%m.%Y")

    # Заменим пробелы в описании теста на "_"
    # desc_corr_format = '_'.join(description.split())
    name_screenshot = f'error_{actual_date}.png'

    # Найдем и откроем скриншот в режиме чтения
    file_path = f'{os.getcwd()}\\screenshots\\{name_screenshot}'

    # Сделаем скриншот
    params.save_screenshot(file_path)
    img = open(file_path, 'rb')

    url = f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&show_caption_above_media=True&caption=🔴{desc}'
    requests.post(url, files={'photo': img})


# сбор статистики
def calc_partners_stat():
    current_hour = datetime.datetime

# Узнать chat_id
#TOKEN = "6951649128:AAHb3triQhmOw7omlTsVyN8waiTzurvvzjI"
#url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
#print(requests.get(url).json())


# def send_report(params, msg):
#
#     send_message_tg(msg)
#     #send_photo_tg()
#     params.close()
#     params.quit()


def authorization_lk(params, domain):

    try:
        # Загружаем страницу
        Methods.set_page(params, domain)
        Methods.wait_page(params, domain)
        Methods.price_to_load(params)

        # Авторизовываемся
        Methods.find_el(params, site_objects.btn_personal_area.xpath)
        Methods.click(params)
        Methods.find_el(params, site_objects.inp_login.xpath)
        Methods.send_keys(params, '79990220038')
        Methods.find_el(params, site_objects.btn_continue.xpath)
        Methods.click(params)
        Methods.find_el(params, site_objects.inp_password.xpath)
        Methods.send_keys(params, 'an2015906')
        Methods.find_el(params, site_objects.btn_login.xpath)
        Methods.click(params)

        Methods.find_el(params, site_objects.img_logo_lk.xpath)

    except Exception:
        pass


def success_request_for_transportation(serial_number):

    # Проверим, есть ли директория для файла (если нет, то создаем директорию и файл)
    if not os.path.isdir("request_for_transportation"):
        os.mkdir(os.getcwd() + '\\request_for_transportation')
    if not os.path.exists('request_for_transportation/request_for_transportation.txt'):
        with open('request_for_transportation/request_for_transportation.txt', 'w') as f:
            f.write('0')

    file_data_iteration = open('request_for_transportation/request_for_transportation.txt', 'r')
    read_file = file_data_iteration.read()  # записываем данные файла в переменную
    if read_file == '':
        read_file = 0
    result = str(int(read_file) + serial_number)

    with open('request_for_transportation/request_for_transportation.txt', 'w') as f:
        f.write(result)

    # Проверим возможность отправки ровно раз в час в телегу
    used_hour = recording_capability()
    if used_hour is True and result != '1':
        send_message_tg(f'🟢 Заявок за час: {result}', token, group_id_predprod)  # изменить на группу
        with open('request_for_transportation/request_for_transportation.txt', 'w') as f:
            f.write('0')

    return result


def recording_capability():

    # Проверим, есть ли директория для файла (если нет, то создаем директорию и файл)
    if not os.path.exists('request_for_transportation/used_hour.txt'):
        with open('request_for_transportation/used_hour.txt', 'w') as f:
            f.write('0')

    time_now = datetime.datetime.now()
    current_time_hour = time_now.hour
    capability = None

    used_hour = open('request_for_transportation/used_hour.txt', 'r')
    last_record_time = used_hour.read()  # записываем данные файла в переменную

    #  проверим, соответствует ли время в файле с текущим временем
    if current_time_hour in range(0, 25) and current_time_hour != int(last_record_time):
        capability = True

        now_hour = str(current_time_hour)
        with open('request_for_transportation/used_hour.txt', 'w') as f:
            f.write(now_hour)

    return capability


def record_timer(func, session):

    """Каждый раз запускаем новую сессию драйвера (с одной сессией разные тесты не работают)"""

    start = time.time()
    desc = func(session)  # ('Тест №61 - Проверка категории груза', {'Проверка выбора категории': False}, None, None)
    end = time.time()

    result = end - start
    # возврат описания теста и времени прохода
    return list(desc)[0], list(desc)[1], round(result, 2)


def tst_passed(status, description):

    """Тут идет простое распределение пройденных/непройденных тестов"""
    if status is True:
        status_passed = True
        return status_passed, description
    else:
        status_passed = False
        return status_passed, description



