import time
from Settings import *
from Methods import *
from various_data import *


"""Проверка цены в мини-калькуляторе"""
def check_price(params, currency):   # добавить проверку в функцию, что цена больше нуля
    time_out = element_time_out

    try:
        WebDriverWait(params, time_out).until(ec.visibility_of_element_located((By.XPATH, f"//div[@class='vz-calculator-price-cost']/strong[contains(text(), '{currency}')]")))

        # дополнительно проверим активную
        if currency == currency_ber or currency == currency_kzt:
            WebDriverWait(params, time_out).until(ec.visibility_of_element_located((By.XPATH, f"//span[@class='vz-radiogroup-item-title'][contains(text(), '{currency}')]/parent::div[contains(@class, 'active')]/span[contains(@class, 'item-radio')]")))
        else:
            pass

    except Exception as e:
        err = f"\nВылюта не соответствует {currency}\nМетод: check_price\n{e}"
        raise Exception(send_message_tg(err, token, chat_id))


"""Установка города отправления в оформлении заказа"""
def set_dispatch_city(params, dispatch_city):

    time.sleep(1)  # для раскрытия списка - позже переделать
    send_keys(params, Keys.CONTROL + "a")
    send_keys(params, Keys.BACK_SPACE)
    send_keys(params, dispatch_city)
    # a, b = choice_cities(cities)
    # send_keys(params, a)
    time.sleep(3)  # переделать прогрузку списка

    # find_el(params, list_input_dispatch.xpath)
    find_el(params, f"//div[contains(@class, 'vz-new-autocomplete-list vz-scroll vz-new-autocomplete-list')]//div[contains(@class, 'vz-new-autocomplete-list-item active')]//div[contains(text(), '{dispatch_city}')]/..")
    click(params)
    price_to_load(params)


"""Установка города получения в оформлении заказа"""
def set_destination_city(params, destination_city):

    time.sleep(1)  # для раскрытия списка - позже переделать
    send_keys(params, Keys.CONTROL + "a")
    send_keys(params, Keys.BACK_SPACE)
    send_keys(params, destination_city)
    # a, b = choice_cities(cities)
    # send_keys(params, b)
    time.sleep(3)  # переделать прогрузку списка

    # find_el(params, list_input_destination.xpath)
    find_el(params, f"//div[contains(@class, 'vz-new-autocomplete-list vz-scroll vz-new-autocomplete-list')]//div[contains(@class, 'vz-new-autocomplete-list-item active')]//div[contains(text(), '{destination_city}')]/..")
    click(params)
    price_to_load(params)


def set_dispatch_city_mini_calc(params, dispatch_city):

    send_keys(params, Keys.CONTROL + "a")
    send_keys(params, Keys.BACK_SPACE)
    send_keys(params, dispatch_city)

    time.sleep(3)  # переделать прогрузку списка
    find_el(params, list_from_mini.xpath)
    find_el(params, first_value_in_list_from.xpath)
    click(params)


def set_destination_city_mini_calc(params, destination_city):

    send_keys(params, Keys.CONTROL + "a")
    send_keys(params, Keys.BACK_SPACE)
    send_keys(params, destination_city)
    time.sleep(3)  # переделать прогрузку списка
    find_el(params, list_to_mini.xpath)
    find_el(params, first_value_in_list_to.xpath)
    click(params)


"""Установка мест"""
def set_places(params):

    places = str(random.randint(1, 99))

    send_keys(params, Keys.CONTROL + "a")
    send_keys(params, Keys.BACK_SPACE)
    send_keys(params, places)

    return places


"""Установка веса"""
def set_weight(params):
    weight = str(random.randint(1, 999))

    send_keys(params, Keys.CONTROL + "a")
    send_keys(params, Keys.BACK_SPACE)
    send_keys(params, weight)

    return weight


"""Установка объема"""
def set_volume(params):
    volume = str(round((random.random() * 10), 2))

    send_keys(params, Keys.CONTROL + "a")
    send_keys(params, Keys.BACK_SPACE)
    send_keys(params, volume)

    return volume


"""Установка контрагента"""
def set_counteragent_data(params, role, type_ka, fio, phone):

    btn_type = None
    input_fio = None
    input_phone = None
    input_additional_phone = None
    input_email = None
    checkbox_send = None

    if role == 'sender':
        if type_ka == 'individual':
            btn_type = btn_type_ind_sender.xpath
            input_fio = input_fio_ind_sender.xpath
            input_phone = input_phone_ind_sender.xpath
            input_additional_phone = input_add_phone_ind_sender.xpath
            input_email = input_email_ind_sender.xpath
            checkbox_send = checkbox_send_code_ind_sender.xpath

        elif type_ka == 'corporation':
            btn_type = btn_type_corp.xpath
            input_phone = input_name_corp.xpath
            input_additional_phone = input_phone_corp .xpath

    elif role == 'recipient':
        if type_ka == 'individual':
            btn_type = btn_type_ind_recipient.xpath
            input_fio = input_fio_ind_recipient.xpath
            input_phone = input_phone_ind_recipient.xpath
            input_additional_phone = input_add_phone_ind_recipient.xpath
            input_email = input_email_ind_recipient.xpath
            checkbox_send = checkbox_send_code_ind_recipient.xpath

        elif type_ka == 'corporation':
            btn_type = btn_type_corp.xpath
            input_phone = input_name_corp.xpath
            input_additional_phone = input_phone_corp.xpath

    # Нажимаем на кнопку "Физ.лицо"
    move_to_element(params, btn_type)
    find_el(params, btn_type)
    click(params)

    # Вводим в поле "ФИО"
    find_el(params, input_fio)
    send_keys(params, fio)

    find_el(params, input_phone)
    send_keys(params, phone)


"""Проверка наличия необходимого города в списке"""  # Не использую - нужно доделать
def check_city_in_list(params, city):
    time_out = element_time_out

    try:
        WebDriverWait(params, time_out).until(ec.visibility_of_element_located((By.XPATH, f"//div[@class='vz-calculator-price-cost']/strong[contains(text(), '{city}')]")))

    except Exception as e:
        err = f"\nГород не соответствует {city}\nМетод: check_city_in_list"
        raise Exception(send_message_tg(err, token, chat_id))


"""Работа с аукционом"""
def set_bid(params, bid):

    send_keys(params, Keys.CONTROL + "a")
    send_keys(params, Keys.BACK_SPACE)
    send_keys(params, bid + random.randint(1, 100))


def get_attribute_bid(params, num_auc):

    try:
        WebDriverWait(params, 15).until(ec.visibility_of_element_located((By.XPATH, f"//tr[contains(@class, 'tr-values vs-table--tr auction-data-column tr-table-state')][{num_auc}]/td[@class='td vs-table--td'][9]/span/span")))
        i = params.find_element(By.XPATH, f"//tr[contains(@class, 'tr-values vs-table--tr auction-data-column tr-table-state')][{num_auc}]/td[@class='td vs-table--td'][9]/span/span")

        time.sleep(1)
        html = params.execute_script('return arguments[0].outerHTML;', i)

        num = ''

        for char in html:
            if char.isdigit():
                num += char
            else:
                pass

        if num == '':
            num += '0'

        return int(num)

    except Exception as e:
        err = f"\nМетод: get_attribute_bid\n{e}"
        raise Exception(send_message_tg(err, token, chat_id))


def result_bid(params):
    if find_el(params, text_bid_set.xpath):
        pass
    else:
        pass


def choice_cities(cities):

    city1 = random.choice(cities)
    city2 = random.choice(cities)
    if city2 == city1:
        cities.remove(city1)
        city2 = random.choice(cities)
        cities.append(city1)
    else:
        pass

    return city1, city2


def close_popups(params):

    if find_el(params, btn_close_popup_rate_your_order.xpath) is True:
        find_el(params, btn_close_popup_rate_your_order.xpath)
        click(params)
    else:
        pass


"""Функция для мониторинга"""
def check_try(success, failed, monitoring_type=0):
    path = "E:\\Vozovoz\\AutoPtoject"  # Нужно для вызова из планировщика заданий windows, т.к. оттуда выбирается дефолтная папка
    os.chdir(path)
    result_all = ''

    if not os.path.isdir("monitoring_docs"):
        os.mkdir(os.getcwd() + '\\monitoring_docs')
    if not os.path.exists('monitoring_docs/success_download_files.txt'):
        with open('monitoring_docs/success_download_files.txt', 'w') as f:
            f.write('0')
    if not os.path.exists('monitoring_docs/failed_download_files.txt'):
        with open('monitoring_docs/failed_download_files.txt', 'w') as f:
            f.write('0')
    if not os.path.exists('monitoring_docs/fall_payment.txt'):
        with open('monitoring_docs/fall_payment.txt', 'w') as f:
            f.write('0')
    if not os.path.exists('monitoring_docs/success_download_files_partners.txt'):
        with open('monitoring_docs/success_download_files_partners.txt', 'w') as f:
            f.write('0')
    if not os.path.exists('monitoring_docs/failed_download_files_partners.txt'):
        with open('monitoring_docs/failed_download_files_partners.txt', 'w') as f:
            f.write('0')

    time_now = datetime.datetime.now()
    current_time_hour = time_now.hour

    if monitoring_type == 0:
        file_data_success = open('monitoring_docs/success_download_files.txt', 'r')
        read_file = file_data_success.read()  # записываем данные файла в переменную
        result_success = str(int(read_file) + success)

        with open('monitoring_docs/success_download_files.txt', 'w') as f:
            f.write(result_success)

        file_data_failed = open('monitoring_docs/failed_download_files.txt', 'r')
        read_file = file_data_failed.read()  # записываем данные файла в переменную
        result_failed = str(int(read_file) + failed)

        with open('monitoring_docs/failed_download_files.txt', 'w') as f:
            f.write(result_failed)

        result_all = str(int(result_success) + int(result_failed))  # результат для мониторинга загрузки файлов

    elif monitoring_type == 1:
        file_data_success = open('monitoring_docs/success_download_files_partners.txt', 'r')
        read_file = file_data_success.read()  # записываем данные файла в переменную
        result_success = str(int(read_file) + success)

        with open('monitoring_docs/success_download_files_partners.txt', 'w') as f:
            f.write(result_success)

        file_data_failed = open('monitoring_docs/failed_download_files_partners.txt', 'r')
        read_file = file_data_failed.read()  # записываем данные файла в переменную
        result_failed = str(int(read_file) + failed)

        with open('monitoring_docs/failed_download_files_partners.txt', 'w') as f:
            f.write(result_failed)

    elif monitoring_type == 2:
        """Оплата"""
        data_fall_payment = open('monitoring_docs/fall_payment.txt', 'r')
        read_file = data_fall_payment.read()  # записываем данные файла в переменную
        fall_payment = str(int(read_file) + failed)

        with open('monitoring_docs/fall_payment.txt', 'w') as f:
            f.write(fall_payment)

    # Формируем статистику в определенный час
    if current_time_hour == 10:

        if monitoring_type == 0:
            msg = f"📋 Результат проверок доступности файлов!\n🔹Всего проверок (PROD сайт) - {result_all}/в сут.:"

            # Проверим есть ли failed на текущий момент
            if failed == 0:
                msg += f"\n✅ Все файлы доступны!\n"
            else:
                msg += f"\n❌ Некоторые файлы недоступны!\n"

            # Откроем файлы по партнерским сайтам
            open_txt_partners_s = open('monitoring_docs/success_download_files_partners.txt', 'r')
            txt_partners_s = open_txt_partners_s.read()
            open_txt_partners_f = open('monitoring_docs/failed_download_files_partners.txt', 'r')
            txt_partners_f = open_txt_partners_f.read()

            msg += f"\n🔹Всего проверок (PARTNERS сайты) - {int(txt_partners_s) + int(txt_partners_f)}/в сут.:"
            if txt_partners_f == '0':
                msg += f"\n✅ Все файлы доступны!"
            else:
                msg += f"\n❌ Некоторые файлы недоступны!"

            send_message_tg(msg, token_vozovoz_bot, chat_id_prod)
            # send_message_tg(msg, token, chat_id_predprod)

            with open('monitoring_docs/success_download_files.txt', 'w') as f:
                f.write('0')
            with open('monitoring_docs/failed_download_files.txt', 'w') as f:
                f.write('0')
            with open('monitoring_docs/success_download_files_partners.txt', 'w') as f:
                f.write('0')
            with open('monitoring_docs/failed_download_files_partners.txt', 'w') as f:
                f.write('0')
            with open('monitoring_docs/fall_payment.txt', 'w') as f:
                f.write('0')
        else:
            pass
    else:
        pass



