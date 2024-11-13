import time
from Business_Actions import *
from Methods import *
from pages.list_of_orders_page import *
from pages.contractors_page import *

def checking_input_search_number_order(params):
    main_description = "Тест №78 - Проверка поиска заказа в поле поиска на странице Заказы"
    status_and_name_tst = {}

    try:
        """Авторизовываемся и переходим на страницу контрагентов"""
        authorization_lk(params, url_base_org)
        wait_page(params, url_base_org_LK)

        """1. Поиск существующего номера заказа - цифры"""
        def check_input_search_number_order_enter_vozovoz_number():
            description = "Поиск существующего номера заказа (в данном примере - статус \"Выдан\")"

            try:
                find_el(params, input_number_of_order_on_orders_page.xpath)
                click(params)

                # Поиск по числовому номеру компании Возовоз
                send_keys(params, individual_order)
                send_keys(params, Keys.ENTER, False)  # False, чтобы не стереть введенный ранее номер заказа

                time.sleep(5)  # Переделать
                enable_loader(params, 15)

                # Проверим корректно ли отображается данный номер в элементе поиска поля
                check_text_attribute(params, text_number_of_order_on_orders_page.xpath, individual_order)

                # Проверим есть ли данная карточка заказа в списке заказов и перейдем в неё
                find_el(params, f"//div[contains(text(), '{individual_order}')]")
                click(params)

                find_el(params, text_number_order_after_create.xpath)

                # Вернемся назад в список заказов
                find_el(params, btn_return_to_list_of_orders_on_orders_page.xpath)
                click(params)

                enable_loader(params, 15)

                find_el(params, input_number_of_order_on_orders_page.xpath)
                click(params)

                # Поиск по числовому номеру компании Возовоз заказа №2
                send_keys(params, individual_order_2)
                send_keys(params, Keys.ENTER, False)  # False, чтобы не стереть введенный ранее номер заказа

                time.sleep(5)  # Переделать
                enable_loader(params, 15)

                # Проверим корректно ли отображается данный номер в элементе поиска поля
                check_text_attribute(params, text_number_of_order_2_on_orders_page.xpath, individual_order_2)

                # Закроем все поисковые запросы
                find_el(params, btn_close_in_element_searching_number_of_order_on_orders_page.xpath)
                click(params)

                enable_loader(params, 15)
                find_el(params, btn_close_in_element_searching_number_of_order_on_orders_page.xpath)
                click(params)

                enable_loader(params, 15)

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

            except Exception as e:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        """2. Поиск существующего заказа по пользовательскому номеру заказа"""
        def check_input_search_number_order_enter_user_number():
            description = "Поиск существующего заказа по пользовательскому номеру заказа"

            try:
                find_el(params, input_number_of_order_on_orders_page.xpath)
                click(params)

                # Поиск по пользовательскому номеру заказа
                send_keys(params, individual_order_with_text)
                send_keys(params, Keys.ENTER, False)  # False, чтобы не стереть введенный ранее номер заказа

                time.sleep(5)  # Переделать
                enable_loader(params, 15)

                # Проверим корректно ли отображается данный номер в элементе поиска поля
                check_text_attribute(params, text_number_of_order_on_orders_page.xpath, individual_order_with_text)

                # Проверим есть ли данная карточка заказа в списке заказов
                find_el(params, f"//div[contains(text(), '{individual_order_with_text}')]")
                click(params)

                find_el(params, text_number_order_after_create.xpath)

                # Вернемся назад в список заказов
                find_el(params, btn_return_to_list_of_orders_on_orders_page.xpath)
                click(params)

                enable_loader(params, 15)

                # Закроем поисковой запрос
                find_el(params, btn_close_in_element_searching_number_of_order_on_orders_page.xpath)
                click(params)

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

        """3. Негативные проверки (несуществующий заказ, заказ другого КА...)"""
        def check_input_with_invalid_data_of_number_order():
            description = "Негативные проверки (несуществующий заказ, заказ другого КА...)"

            try:
                """Поиск по несуществующему номеру в компании"""
                find_el(params, input_number_of_order_on_orders_page.xpath)
                click(params)

                send_keys(params, invalid_individual_order)
                send_keys(params, Keys.ENTER, False)  # False, чтобы не стереть введенный ранее номер заказа

                time.sleep(5)  # Переделать
                enable_loader(params, 15)

                # Проверим, отображается ли уведомление о том, что к заказу нет доступа
                find_el(params, link_if_entering_an_invalid_number_of_order_on_orders_page.xpath)

                # Перейдем по ссылке "Контрагенты" в уведомлении
                click(params)
                url_contain_url(params, url_contractors_org)
                find_el(params, list_of_ka_on_the_contractor_page.xpath)

                # Вернемся назад в список заказов
                set_page(params, url_base_org_LK)
                wait_page(params, url_base_org_LK)

                enable_loader(params, 15)

                """Поиск по номеру заказа другого КА, к которому нет доступа"""
                find_el(params, input_number_of_order_on_orders_page.xpath)
                click(params)

                send_keys(params, individual_order_3)
                send_keys(params, Keys.ENTER, False)  # False, чтобы не стереть введенный ранее номер заказа

                time.sleep(5)  # Переделать
                enable_loader(params, 15)

                # Проверим, отображается ли уведомление о том, что к заказу нет доступа
                find_el(params, link_if_entering_an_invalid_number_of_order_on_orders_page.xpath)

                # Закроем поисковой запрос
                find_el(params, btn_close_in_element_searching_number_of_order_on_orders_page.xpath)
                click(params)

                """Поиск по части номера заказа"""
                find_el(params, input_number_of_order_on_orders_page.xpath)
                click(params)

                send_keys(params, individual_order_part)
                send_keys(params, Keys.ENTER, False)  # False, чтобы не стереть введенный ранее номер заказа

                time.sleep(5)  # Переделать
                enable_loader(params, 15)

                # Проверим, отображается ли уведомление о том, что к заказу нет доступа
                find_el(params, link_if_entering_an_invalid_number_of_order_on_orders_page.xpath)

                # Закроем поисковой запрос
                find_el(params, btn_close_in_element_searching_number_of_order_on_orders_page.xpath)
                click(params)

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

        status_and_name_tst = check_input_search_number_order_enter_vozovoz_number()
        status_and_name_tst = check_input_search_number_order_enter_user_number()
        status_and_name_tst = check_input_with_invalid_data_of_number_order()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

