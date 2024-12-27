from Business_Actions import *
from Methods import *
from pages.list_of_orders_page import *
from pages.order_details import *


def cancellation_of_order(params):
    main_description = "Тест №87 - Отмена заказа в списке заказов и в детализации"
    status_and_name_tst = {}

    #  Берем рандомно два неповторяющихся города из списка
    dispatch_city, destination_city = choice_cities(cities)

    try:
        """1. Проверка отмены заявки в списке заказов"""
        def cancellation_of_create_order_in_list_of_orders():
            description = "Проверка отмены заявки в списке заказов"

            try:
                authorization_lk(params, url_base_org, individual_phone_full, passw)

                """Оформим стандартный заказ"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                # Заполняем "Отправка"
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, dispatch_city)

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                # Заполняем "Прибытие"
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, destination_city)

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                # Заполняем кол-во мест
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                # Заполняем участников
                set_counteragent_data(params, "sender", "individual", individual_fio, individual_phone)
                set_counteragent_data(params, "recipient", "individual", individual_fio, individual_phone)

                # Нажимаем на кнопку "Оформить"
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера 1-ого заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)
                data_number_of_order = get_the_data_from_element(params, text_number_order_after_create.xpath)
                data_number_of_order = extract_numbers(data_number_of_order)

                # Создадим заказ на основании, чтобы отменить его другой кнопкой
                find_el(params, btn_create_based_on_in_details_page.xpath)
                click(params)

                switch_to_next_or_previous_tab(params)
                url_contain_url(params, url_base_org_order_create)
                price_to_load(params)

                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера 2-ого заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)
                data_number_of_order_2 = get_the_data_from_element(params, text_number_order_after_create.xpath)
                data_number_of_order_2 = extract_numbers(data_number_of_order_2)

                """Переход на страницу Заказы, чтобы отменить заказ №2"""
                set_page(params, url_base_org_LK)
                wait_page(params, url_base_org_LK)

                # Подставим номер заказа в xpath и найдем созданный заказ в списке заказов
                text_order_number_in_the_order_block_on_orders_page_2.change_xpath(data_number_of_order_2)
                find_el(params, text_order_number_in_the_order_block_on_orders_page_2.xpath)

                # Подставим номер заказа в xpath, который относится к блоку нужного заказа, чтобы у него нажать кнопку "Отменить заказ"
                btn_cancel_order_button_in_the_order_list_page.change_xpath(data_number_of_order_2)
                find_el(params, btn_cancel_order_button_in_the_order_list_page.xpath)
                click(params)

                # Попап Отмена заказа
                find_el(params, text_cancellation_of_the_order_in_the_popup_of_the_order.xpath)
                find_el(params, input_reason_for_cancellation_field_in_the_popup_cancellation.xpath)
                send_keys(params, test_message)

                find_el(params, btn_send_in_the_popup_cancellation.xpath)
                click(params)

                """Отменяем заказ №1"""
                switch_to_next_or_previous_tab(params, False)
                url_contain_url(params, url_base_org_personal_order)

                find_el(params, btn_cancel_order_on_in_details_page.xpath)
                click(params)

                # Попап Отмена заказа
                find_el(params, text_cancellation_of_the_order_in_the_popup_of_the_order.xpath)
                find_el(params, input_reason_for_cancellation_field_in_the_popup_cancellation.xpath)
                send_keys(params, test_message)

                find_el(params, btn_send_in_the_popup_cancellation.xpath)
                click(params)

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst, data_number_of_order, data_number_of_order_2

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        """2. Поиск отмененных заявок в списке заказов"""
        def search_for_a_cancelled_order(number_1, number_2):
            description = "Проверка отмены заявки в списке заказов"
            set_page(params, url_base_org_LK)
            wait_page(params, url_base_org_LK)

            try:
                """Найдем отмененный заказ"""
                find_el(params, input_number_of_order_on_orders_page.xpath)
                click(params)
                send_keys(params, number_1)
                send_keys(params, Keys.ENTER, False)  # False, чтобы не стереть введенный ранее номер заказа

                time.sleep(5)  # Переделать
                enable_loader(params, 15)

                find_el(params, input_number_of_order_on_orders_page.xpath)
                click(params)
                send_keys(params, number_2)
                send_keys(params, Keys.ENTER, False)  # False, чтобы не стереть введенный ранее номер заказа

                time.sleep(5)  # Переделать
                enable_loader(params, 15)

                # Проверим есть ли данные карточка заказов в списке заказов со статусом "Отменен"
                text_order_status_in_the_order_block_on_orders_page_x.change_xpath(number_1)
                find_el(params, text_order_status_in_the_order_block_on_orders_page_x.xpath)

                text_order_status_in_the_order_block_on_orders_page_x.reset_xpath()
                text_order_status_in_the_order_block_on_orders_page_x.change_xpath(number_2)
                find_el(params, text_order_status_in_the_order_block_on_orders_page_x.xpath)

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

        status_and_name_tst, data_number_of_order, data_number_of_order_2 = cancellation_of_create_order_in_list_of_orders()
        status_and_name_tst = search_for_a_cancelled_order(data_number_of_order, data_number_of_order_2)

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()


