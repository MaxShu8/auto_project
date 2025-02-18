import time

from selenium.common import WebDriverException, InvalidSelectorException, TimeoutException

from Settings import *
import site_objects
from site_objects import *
import various_data
from various_data import *
from pages.order_create_page import *
from datetime import datetime, timedelta


current_element = None
site_object = ''
num = int()


def set_page(params, url_page):
    err = ''
    page_load_timeout = various_data.page_load_timeout

    try:
        params.get(url_page)
        url_cur = params.current_url

        assert url_cur == url_page, 'Открыта не та страница'

        page_content = params.page_source
        offer = "offer-card-image"
        something_went_wrong = "error-page"

        if offer in page_content:
            WebDriverWait(params, 20).until(ec.element_to_be_clickable((By.XPATH, btn_offer_card_image_lk.xpath))).click()
        else:
            pass

        if something_went_wrong in page_content:
            params.refresh()
        else:
            pass

    except TimeoutException as e:
        err = f'\nСтраница не установилась за {page_load_timeout} сек.\nМетод: set_page\nURL: {url_page}\n{e}'
        raise TimeoutException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = (f'\nСтраница не загрузилась из-за неизвестной ошибки\nМетод: set_page\nURL: {url_page}\nПроизошла ошибка'
               f' при загрузке страницы\n{e}')
        raise Exception(send_message_tg(err, token, chat_id))


"""Ожидание загрузки страницы"""
def wait_page(params, url_page):
    err = ''
    page_load_timeout = various_data.page_load_timeout

    try:

        WebDriverWait(params, page_load_timeout).until(ec.url_to_be(url_page))
        url_cur = params.current_url

        if url_cur != url_page:
            params.refresh()

        # для ожидания загрузки мини-калькулятора, иначе кнопка ЛК некликабельна (далее отдельно нужен метод загрузки калькулятора)
        if url_cur == site_objects.url_base_dev or url_cur == site_objects.url_base_org:
            price_to_load(params)

        if url_base_org_personal_order in params.current_url:
            price_to_load(params)

        if url_cur == url_order_manage_org:
            time.sleep(1)

    except Exception as e:
        err = f'\nСтраница не установилась за {page_load_timeout} сек.\nМетод: wait_page\nURL: {url_page}\n{e}'
        raise Exception(send_message_tg(err, token, chat_id))


"""Поиск элемента"""
def find_el(params, xpath, *args):

    global site_object
    site_object = xpath
    element_time_out = various_data.element_time_out

    try:
        move_to_element(params, xpath)
        params.implicitly_wait(5)
        params.current_element = WebDriverWait(params, element_time_out, 1).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        params.current_element.find_element(By.XPATH, site_object)

    # except InvalidSelectorException as e:
    #     err = f'\nСуть ошибки: указан некорректный адрес элемента\nМетод: find_element\nЭлемент: {site_object}\n{e}'
    #     raise InvalidSelectorException(send_message_tg(err, token, chat_id))
    #
    # except WebDriverException as e:
    #     err = f'\nОшибка: WebDriverException\nМетод: find_element\nЭлемент: {site_object}\n{e}'
    #     raise WebDriverException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = f'\nОшибка: неопознанная\nМетод: find_element\nЭлемент: {site_object}\n{e}'
        raise Exception(err)

    return params.current_element, site_object


def wait_tobe_clickable(params, xpath):

    time_out = various_data.element_time_out

    try:
        WebDriverWait(params, time_out).until(ec.element_to_be_clickable((By.XPATH, xpath)))

    except TimeoutException as e:
        err = f'\nОшибка: элемент не готов к нажатию\nМетод: wait_to_be_clickable\nЭлемент: {site_object}\n{e}'
        raise TimeoutException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = f'\nОшибка: элемент не готов к нажатию\nМетод: wait_to_be_clickable\nЭлемент: {site_object}\n{e}'
        raise Exception(send_message_tg(err, token, chat_id))
    # return a

def wait_to_be_clickable(params):
    wait_tobe_clickable(params, site_object)


def click_element(params, element, *args):
    err = ''

    try:
        wait_to_be_clickable(params)
        element.click()

    except WebDriverException as e:
        err = f"\nОшибка: указан некорректный xPath элемента\nМетод: click_element\nЭлемент: {element}\n{e}"
        raise WebDriverException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = f"\nНеизвестная ошибка\nМетод: click_element\nЭлемент: {element}\n{e}"
        raise Exception(send_message_tg(err, token, chat_id))


def click(params, skip_check=False):  # имеется необязательный аргумент skip_check
    click_element(params, params.current_element)
    if skip_check is True:
        pass
    else:
        check_error_toast(params)


def send_keys(params, keys, clean_before=True):  # опция по дефолту, чтобы очищать поля ввода, но если это не нужно, то...
    err = ''

    try:
        if clean_before is True:
            params.current_element.send_keys(Keys.CONTROL + "a")
            params.current_element.send_keys(Keys.BACK_SPACE)
        params.current_element.send_keys(keys)

    except WebDriverException as e:
        err = f"\nОшибка: {e}\nМетод: send_keys"
        raise WebDriverException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = f"\nНеизвестная ошибка\nМетод: send_keys"
        raise Exception(send_message_tg(err, token, chat_id))


def move_to_element(params, xpath):
    btn = params.find_element(By.XPATH, xpath)
    ActionChains(params).move_to_element(btn).perform()


def price_to_load(params):
    err = ''
    time_out = various_data.element_time_out

    try:
        if params.current_url == url_base_dev or params.current_url == url_base_org or params.current_url == url_base_ru:
            WebDriverWait(params, time_out).until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Откуда')]/ancestor::div[@class='vz-input']/div")))
            WebDriverWait(params, time_out).until(ec.text_to_be_present_in_element_attribute(('xpath', "//div[@class='vz-loader']"), attribute_='style', text_='display: none;'))
            WebDriverWait(params, time_out).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='vz-calculator-price-cost']")))

            # проверим, есть ли ошибка после исчезновения лоадера
            check_error_toast(params)

        elif url_base_dev in params.current_url or url_base_org in params.current_url or url_base_ru in params.current_url:
            WebDriverWait(params, time_out).until(ec.text_to_be_present_in_element_attribute(('xpath', "//div[@class='vz-loader']"), attribute_='style', text_='display: none;'))

            # проверим, есть ли ошибка после исчезновения лоадера
            check_error_toast(params)

        else:
            try:
                # ждем, когда исчезнет лоадер загрузки стоимости
                WebDriverWait(params, time_out).until(ec.text_to_be_present_in_element_attribute(('xpath', "//div[@class='vz-loader viewOnly']"), attribute_='style', text_='display: none;'))

                # проверим, есть ли ошибка после исчезновения лоадера
                check_error_toast(params)

            except TimeoutException:
                params.refresh()
                wait_page(params, params.current_url)

                # проверим, есть ли тоаст о продолжении оформления заказа
                page_content = params.page_source
                info_toast = 'vz-toast show bottom info'

                if info_toast in page_content:
                    find_el(params, btn_continue_in_toast.xpath)
                    click(params)
                    WebDriverWait(params, time_out).until(ec.text_to_be_present_in_element_attribute(('xpath', "//div[@class='vz-loader viewOnly']"), attribute_='style', text_='display: none;'))
                else:
                    WebDriverWait(params, time_out).until(ec.text_to_be_present_in_element_attribute(('xpath', "//div[@class='vz-loader viewOnly']"), attribute_='style', text_='display: none;'))
                    find_el(params, btn_dispatch_terminal.xpath)
                    click(params)
                    WebDriverWait(params, time_out).until(ec.text_to_be_present_in_element_attribute(('xpath', "//div[@class='vz-loader viewOnly']"), attribute_='style', text_='display: none;'))
                    find_el(params, btn_destination_terminal.xpath)
                    click(params)
                    WebDriverWait(params, time_out).until(ec.text_to_be_present_in_element_attribute(('xpath', "//div[@class='vz-loader viewOnly']"), attribute_='style', text_='display: none;'))
                    pass

            except Exception:
                WebDriverWait(params, time_out).until(ec.text_to_be_present_in_element_attribute(('xpath', "//div[@class='vz-loader viewOnly']"), attribute_='style', text_='display: none;'))
                pass

    except TimeoutException:
        pass

    except WebDriverException as e:
        err = f"Метод: price_to_load\nОшибка: Долгий ответ на запрос get-price (блок 'Стоимость' при оформлении заказа)\ntime_out: {element_time_out}сек.\n{e}"
        raise WebDriverException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = f"Метод: price_to_load\nОшибка: Что-то произошло при расчете цены\n{e}"
        raise Exception(send_message_tg(err, token, chat_id))


def find_els(params, xpath):
    time_out = various_data.element_time_out

    try:
        params.implicitly_wait(5)
        # return WebDriverWait(params, element_time_out).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        a = WebDriverWait(params, element_time_out).until(ec.presence_of_all_elements_located((By.XPATH, xpath)))

        return a
        # a = params.find_elements(By.XPATH, site_object)
        #  a

    except WebDriverException as e:
        err = f"\nОшибка: {e}\nМетод: wait_invisibility_element"
        raise WebDriverException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = f"\nНеизвестная ошибка\nМетод: wait_invisibility_element"
        raise Exception(send_message_tg(err, token, chat_id))


def invisibility_of_element(params, xpath):

    try:
        params.implicitly_wait(5)
        WebDriverWait(params, element_time_out).until(ec.invisibility_of_element_located((By.XPATH, xpath)))

    except WebDriverException as e:
        err = f"\nОшибка: {e}\nМетод: invisibility_of_element"
        raise WebDriverException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = f"\nНеизвестная ошибка\nМетод: invisibility_of_element"
        raise Exception(send_message_tg(err, token, chat_id))


def url_contain_url(params, url):

    try:
        if url not in params.current_url:
            WebDriverWait(params, page_load_timeout).until(ec.url_to_be(params.current_url))
        else:
            pass
        time.sleep(3)

    except TimeoutException as e:
        send_photo_tg(params, token, chat_id, desc='url_contain_url')
        send_message_tg(e, token, chat_id)
        err_short = f"🟡TimeOut Exception: {element_time_out}сек. - после нажатия на 'Оформить' заказ"
        raise TimeoutException(send_message_tg(err_short, token, group_id_predprod))

    except Exception as e:
        err = f"Метод: url_contain_url\nОшибка: url не содержит в себе нужный url\n{e}"
        raise Exception(err)
    return params.current_url


def find_number_order(params):
    try:
        a = WebDriverWait(params, element_time_out, 1).until(ec.visibility_of_element_located((By.XPATH, text_number_order_after_create.xpath)))
        a.find_element(By.XPATH, text_number_order_after_create.xpath)

    except TimeoutException:
        send_photo_tg(params, token, chat_id, desc='find_number_order')
        err_short = f"🟡TimeOut Exception: {element_time_out}сек. - после нажатия на 'Оформить' заказ"
        send_message_tg(err_short, token, group_id_predprod)

    except WebDriverException:
        send_photo_tg(params, token, chat_id, desc='find_number_order')
        err_short = f"🟡TimeOut Exception: {element_time_out}сек. - после нажатия на 'Оформить' заказ"
        send_message_tg(err_short, token, group_id_predprod)

    except Exception:
        send_photo_tg(params, token, chat_id, desc='find_number_order')
        err_short = f"🟡TimeOut Exception: {element_time_out}сек. - после нажатия на 'Оформить' заказ"
        send_message_tg(err_short, token, group_id_predprod)


def check_text_attribute(params, xpath, value, pass_exception=False, check_range=False):
    """"""
    try:
        move_to_element(params, xpath)
        a = WebDriverWait(params, element_time_out, 1).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        a.find_element(By.XPATH, xpath)

        including_class = a.get_attribute('class')  # выгружает название класса
        including_name = a.get_attribute('name')
        including_value = a.get_attribute('value')
        including_text = a.text  # выгружает текст

        # Сделаем избежание вызова исключения в случае, если на каком-то этапе выпало None
        if including_class is None:
            including_class = 'None'
        if including_name is None:
            including_name = 'None'
        if including_value is None:
            including_value = 'None'
        if including_text is None:
            including_text = 'None'

        # Проверка указанного значения по включению в атрибуты, текст
        if check_range is False:
            if value in including_class:
                pass
            elif value in including_name:
                pass
            elif value in including_value:
                pass
            elif value in including_text:
                pass
            else:
                if pass_exception is True:
                    return False
                else:
                    raise Exception
        else:
            list_figures = []
            new_value = float(value)
            list_figures.append(new_value)
            list_figures.append(int(new_value))
            list_figures.append(round((new_value - 0.01), 2))
            list_figures.append(round((new_value + 0.01), 2))
            list_figures.append(round((new_value - 0.1), 1))
            list_figures.append(round((new_value + 0.1), 1))

            if any(str(item) in including_text for item in list_figures):
                pass
            else:
                if pass_exception is True:
                    return False
                else:
                    raise Exception

    except Exception:
        err = f"Значение атрибута: {value} - не соответствует ожидаемому"
        raise Exception(err)


def check_error_toast(params):
    time.sleep(0.5)
    page_content = params.page_source
    error = 'vz-toast show bottom error'

    if error in page_content:
        raise Exception
    else:
        pass


def switch_to_next_or_previous_tab(params, next_tab=True):   # Если необходимо перейти на самую первую вкладку, то передаем False
    # list_of_tabs = params.window_handles
    if next_tab is False:
        previous_tab = params.window_handles[0]
        tab = params.switch_to.window(previous_tab)
    else:
        next_tab = params.window_handles[-1]  # последняя открытая вкладка
        tab = params.switch_to.window(next_tab)
    return tab


def enable_loader(params, timeout=30):
    try:
        WebDriverWait(params, timeout).until(ec.text_to_be_present_in_element_attribute(('xpath', "//div[@class='vz-loader']"), attribute_='style', text_='display: none;'))
        if params.current_url == url_contractors_org or url_contractors_org in params.current_url or params.current_url == url_contractors_dev or params.current_url == url_contractors_ru:
            WebDriverWait(params, timeout).until(ec.invisibility_of_element(('xpath', "//div[@class='vz-dialog-card-content']//div[@class='vz-loader']")))
    except Exception:
        pass


def enable_skeleton(params, timeout=30):
    try:
        if url_base_org_personal_order in params.current_url or url_base_dev_personal_order in params.current_url:
            WebDriverWait(params, timeout).until(ec.invisibility_of_element(("xpath", "//div[@class='w-20 mr-auto']/div[contains(@class, 'vz-skeleton vz-skeleton-animated')]")))

    except Exception:
        pass


# Загрузка файла
def upload_file(params, xpath):

    try:
        upload_filed = params.find_element(By.XPATH, xpath)
        upload_filed.send_keys(f"{os.getcwd()}\\files_for_tsts\\pdf_file_for_test.pdf")

    except Exception as e:
        err = f"Файл не загрузился\n{e}"
        raise Exception(err)


def get_the_data_from_element(params, xpath, what_to_get=0):
    """По дефолту возвращает текст элемента, но если передать: 1 - возвращает value элемента
    2 - класс элемента"""

    a = WebDriverWait(params, element_time_out, 1).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    if what_to_get == 1:
        including_value = a.get_attribute('value')
        return including_value
    elif what_to_get == 2:
        including_class = a.get_attribute('class')
        return including_class
    elif what_to_get == 3:
        including_data = a.get_attribute('data-date')
        return including_data
    else:
        a.find_element(By.XPATH, xpath)
        including_text = a.text  # выгружает текст
        return including_text


def get_the_data_from_block_of_elements(params, xpath, what_to_get=0):
    """"""
    list_of_data = []
    a = WebDriverWait(params, element_time_out, 1).until(ec.presence_of_all_elements_located((By.XPATH, xpath)))

    for element in a:
        if what_to_get == 1:
            including_value = element.get_attribute('value')
            list_of_data.append(including_value)

        elif what_to_get == 2:
            including_class = element.get_attribute('class')
            list_of_data.append(including_class)
        else:
            element.find_element(By.XPATH, xpath)
            including_text = element.text  # выгружает текст
            list_of_data.append(including_text)

    return list_of_data


def extract_numbers(string_value):
    """Функция возвращает числа из строкового значения."""

    current_number = ""
    counter = 0

    for char in string_value:
        if char.isdigit() and counter < 11:
            current_number += char
            counter += 1

    return current_number


def waiting_for_the_order_to_be_visible_to_the_user(params, number):
    """Ожидание появления заказа у другого КА."""

    page_content = params.page_source
    order = number
    counter = 0

    while order not in page_content:
        params.refresh()
        time.sleep(8)
        page_content = params.page_source
        counter += 1
        if counter > 10:
            break

def enable_element(params, xpath, timeout=30):
    try:
        WebDriverWait(params, timeout).until(ec.invisibility_of_element(("xpath", xpath)))

    except Exception:
        pass


def exist_elements_of_list_in_list(list_a, list_b):
    """Проверка включения всех элементов списка a в списке b"""
    try:
        result = all(any(package in item for item in list_a) for package in list_b)
        if result is True:
            pass
        else:
            err = "Отсутствуют совпадения двух списков"
            raise Exception(err)

    except Exception:
        pass


def extract_time_from_block_direction(value):
    """Принимает значение времени в формате 2025-02-12T07:00:00 и возвращает время в формате 07:00"""

    time_num = value.split('T')
    a = (time_num[1])[:5]
    return a

# Убрать после прогона тестов!
# def extract_time_from_block_direction(value):
#     """Принимает значение времени в формате '07:00' и возвращает часы в int"""
#
#     time_num = value.split(':')
#     a = int(time_num[0])
#     return a


def add_up_the_time(time_a, time_b, summation=True):
    """Сложение(для утреннего времени) или вычитание(для вечернего)"""

    # Определяем начальное время
    start_time = datetime.strptime(time_a, "%H:%M").time()

    if type(time_b) is not int:
        time_b = time_to_int(time_b)

    # Создаём объект timedelta
    delta = timedelta(hours=time_b)
    delta_add = timedelta(hours=0, minutes=30)

    # Сложение/вычитание времени и временного интервала
    if summation is True:
        result_time = (datetime.combine(datetime.min, start_time) + delta).time()

        # Преобразуем результат обратно в строку
        result_time_str = result_time.strftime("%H:%M")

        return result_time_str

    else:
        result_time = (datetime.combine(datetime.min, start_time) - delta).time()

        # Преобразуем результат обратно в строку
        result_time_str = result_time.strftime("%H:%M")

        return result_time_str


def time_to_int(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours + minutes/60



