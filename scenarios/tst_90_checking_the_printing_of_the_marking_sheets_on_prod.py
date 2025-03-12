from Business_Actions import *
from Methods import *
from pages.list_of_orders_page import *


def get_documents_of_order(type_doc, order_guid, format_m_list=None):
    """Отправим запросы на печать определенного документа по заказу"""

    json_request_document = {}
    url_request_post_document_url = "https://api.vozovoz.ru/v2/document/get"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    if type_doc in ("blank", "utd"):
        json_request_document = {
            "docType": f"{type_doc}",
            "orderGuid": f"{order_guid}"
        }

    elif type_doc in ("markingList", "barCode", "manipulationSign"):
        json_request_document = {
            "docType": f"{type_doc}",
            "format": f"{format_m_list}",
            "orderGuid": f"{order_guid}"
        }

    # Запрос на печать доков по заказу (метод POST)
    response_post = requests.post(url_request_post_document_url, json=json_request_document, headers=headers)

    # Json в формате словаря
    json_dict = response_post.json()

    # Достанем url документа, чтобы далее проверить доступность ссылки
    url_of_documents = json_dict['documentUrl']

    # Отправим запрос по ссылке
    response = requests.get(url_of_documents, headers=headers)
    if response.status_code == 404:
        err = f"Файл недоступен: {type_doc}"
        send_message_tg(err, token, chat_id)
        raise Exception


def check_printing_of_documents_for_order_on_prod(params):
    main_description = "Тест №90 - Проверка печати документов у заказов"
    status_and_name_tst = {}
    authorization_lk(params, url_base_ru, individual_phone_2_full, passw2)

    try:
        """1. Проверка печати документов, если статус 'Заявка'"""
        def checking_printing_of_documents_for_order_with_request_status():
            description = "Проверка печати документов, если статус 'Заявка'"

            try:
                """Переходим на страницу заказов"""
                set_page(params, url_order_list_ru)
                wait_page(params, url_order_list_ru)
                price_to_load(params)

                """Найдем заказы со статусом - Заявка"""
                find_el(params, btn_advanced_search_button_on_orders_page.xpath)
                click(params)

                find_el(params, input_select_the_status_on_orders_page.xpath)
                click(params)

                find_el(params, checkbox_select_the_request_status_on_orders_page.xpath)
                click(params)

                find_el(params, input_select_the_status_on_orders_page.xpath)
                click(params)

                find_el(params, btn_apply_button_in_advanced_search_popup_on_orders_page.xpath)
                click(params)

                # Подождем, пока исчезнут скелетоны
                invisibility_of_element(params, skeleton_of_order_on_orders_page.xpath)

                # Перейдем в заказ статусом Заявка
                find_el(params, elm_order_card_in_the_order_list_page.xpath)
                click(params)
                price_to_load(params)

                number_order_guid = extract_part_url(params)  # Получим часть url - orderGuid

                """Отправляем отдельные запросы на печать документов по заказу, передавая необходимый тип документа"""
                # Бланк заказа
                get_documents_of_order("blank", number_order_guid)

                # Маркировочный лист
                get_documents_of_order("markingList", number_order_guid, "A4")
                get_documents_of_order("markingList", number_order_guid, "A5")
                get_documents_of_order("markingList", number_order_guid, "A6")

                # Штрих-код
                get_documents_of_order("barCode", number_order_guid, "A6")
                get_documents_of_order("barCode", number_order_guid, "75x120")
                get_documents_of_order("barCode", number_order_guid, "56x40")
                get_documents_of_order("barCode", number_order_guid, "50x80")

                # Манипуляционные знаки
                get_documents_of_order("manipulationSign", number_order_guid, "FragileGoods")
                get_documents_of_order("manipulationSign", number_order_guid, "KeepUpright")
                get_documents_of_order("manipulationSign", number_order_guid, "ProtectFromMoisture")
                get_documents_of_order("manipulationSign", number_order_guid, "DoNotRoll")
                get_documents_of_order("manipulationSign", number_order_guid, "DoNotUseForkliftHandler")

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        """2. Проверка печати документов, если статус 'Выдан'"""
        def checking_printing_of_documents_for_order_with_issued_status():
            description = "Проверка печати документов, если статус 'Выдан'"

            try:
                """Переходим на страницу заказов"""
                set_page(params, url_order_list_ru)
                wait_page(params, url_order_list_ru)
                params.refresh()
                price_to_load(params)

                """Найдем заказы со статусом - Принят"""
                find_el(params, btn_advanced_search_button_on_orders_page.xpath)
                click(params)

                find_el(params, input_select_the_status_on_orders_page.xpath)
                click(params)

                find_el(params, checkbox_select_the_issued_status_on_orders_page.xpath)
                click(params)

                find_el(params, input_select_the_status_on_orders_page.xpath)
                click(params)

                find_el(params, btn_apply_button_in_advanced_search_popup_on_orders_page.xpath)
                click(params)

                # Подождем, пока исчезнут скелетоны
                invisibility_of_element(params, skeleton_of_order_on_orders_page.xpath)

                # Перейдем в заказ статусом Заявка
                find_el(params, elm_order_card_in_the_order_list_page.xpath)
                click(params)
                price_to_load(params)

                number_order_guid = extract_part_url(params)  # Получим часть url - orderGuid

                """Отправляем отдельные запросы на печать документов по заказу, передавая необходимый тип документа"""
                get_documents_of_order("utd", number_order_guid)  # Бланк заказа

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        status_and_name_tst = checking_printing_of_documents_for_order_with_request_status()
        status_and_name_tst = checking_printing_of_documents_for_order_with_issued_status()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()


