from Business_Actions import *
from Methods import *


def create_order_terminal_address(params):
    main_description = "Тест №37 - Создание заказа: Терминал --> Адрес, Адрес --> Терминал"
    status_and_name_tst = {}

    try:
        authorization_lk(params, url_base_org, individual_phone_full, passw)

        """1. Проверка создания заявки из терминала до адреса"""
        def tst_create_order_terminal_address():
            description = "Проверка создания заявки из терминала до адреса"

            try:

                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[1])

                find_el(params, btn_destination_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_destination_address.xpath)
                click(params)
                send_keys(params, addresses[2])

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio, individual_phone)

                """Нажимаем на кнопку 'Оформить'"""
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)

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

        """2. Проверка создания заявки от адреса до терминала"""
        def tst_create_order_address_terminal():
            description = "Проверка создания заявки от адреса до терминала"

            try:

                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, btn_dispatch_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_dispatch_address.xpath)
                click(params)
                send_keys(params, addresses[1])

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[8])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio, individual_phone)

                """Нажимаем на кнопку 'Оформить'"""
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)

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

        """3. Проверка создания заявки от адреса до адреса"""
        def tst_create_order_address_address():
            description = "Проверка создания заявки от адреса до адреса"

            try:

                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, btn_dispatch_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_dispatch_address.xpath)
                click(params)
                send_keys(params, addresses[1])

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[1])

                find_el(params, btn_destination_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_destination_address.xpath)
                click(params)
                send_keys(params, addresses[2])

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio, individual_phone)

                """Нажимаем на кнопку 'Оформить'"""
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)

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

        status_and_name_tst = tst_create_order_terminal_address()
        status_and_name_tst = tst_create_order_address_terminal()
        status_and_name_tst = tst_create_order_address_address()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

