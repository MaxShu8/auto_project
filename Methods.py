import time

from selenium.common import WebDriverException, InvalidSelectorException, TimeoutException

from Settings import *
import site_objects
from site_objects import *
import various_data
from various_data import *


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
        if offer in page_content:
            WebDriverWait(params, 20).until(ec.element_to_be_clickable((By.XPATH, btn_offer_card_image_lk.xpath))).click()
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

    except InvalidSelectorException as e:
        err = f'\nСуть ошибки: указан некорректный адрес элемента\nМетод: find_element\nЭлемент: {site_object}\n{e}'
        raise InvalidSelectorException(send_message_tg(err, token, chat_id))

    except WebDriverException as e:
        err = f'\nОшибка: WebDriverException\nМетод: find_element\nЭлемент: {site_object}\n{e}'
        raise WebDriverException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = f'\nОшибка: неопознанная\nМетод: find_element\nЭлемент: {site_object}\n{e}'
        raise Exception(send_message_tg(err, token, chat_id))

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
        params.current_element = WebDriverWait(params, element_time_out).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        params.find_elements(By.XPATH, site_object)

    except WebDriverException as e:
        err = f"\nОшибка: {e}\nМетод: wait_invisibility_element"
        raise WebDriverException(send_message_tg(err, token, chat_id))

    except Exception as e:
        err = f"\nНеизвестная ошибка\nМетод: wait_invisibility_element"
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


def check_text_attribute(params, xpath, value):
    try:
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
        if value in including_class:
            pass
        elif value in including_name:
            pass
        elif value in including_value:
            pass
        elif value in including_text:
            pass
        else:
            raise Exception

    except Exception as e:
        err = f"Тело атрибута не соответствует ожидаемому\n{e}"
        raise Exception(send_message_tg(err, token, chat_id))

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


# Загрузка файла
def upload_file(params, xpath):

    try:
        upload_filed = params.find_element(By.XPATH, xpath)
        upload_filed.send_keys(f"{os.getcwd()}\\files_for_tsts\\pdf_file_for_test.pdf")

    except Exception as e:
        err = f"Файл не загрузился\n{e}"
        raise Exception(err)


def get_the_text(params, xpath):
    a = WebDriverWait(params, element_time_out, 1).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    a.find_element(By.XPATH, xpath)

    including_text = a.text  # выгружает текст
    return including_text

