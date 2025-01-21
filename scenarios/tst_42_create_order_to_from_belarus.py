from Business_Actions import *
from Methods import *
from pages.order_create_page import *


def create_order_from_to_belarus(params):
    main_description = "Тест №42 - Создание заказа из/в Беларусь"
    status_and_name_tst = {}

    try:
        authorization_lk(params, url_base_org, individual_phone_full, passw)

        """1. Проверка создания заявки из Беларуси в Россию"""
        def tst_create_order_from_belarus_to_russia():
            description = "Проверка создания заявки из Беларуси в Россию"

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities_another_countries[0])

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[4])

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

                """Нажимаем на кнопку 'Подтвердить' в попапе"""
                find_el(params, txt_currency_confirmation_header_in_the_currency_confirmation_popup.xpath)
                find_el(params, btn_confirm_in_the_currency_confirmation_popup.xpath)
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

        """2. Проверка создания заявки из России в Беларусь"""
        def tst_create_order_from_russia_to_belarus():
            description = "Проверка создания заявки из России в Беларусь"

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[1])

                find_el(params, btn_dispatch_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_dispatch_address.xpath)
                click(params)
                send_keys(params, addresses[2])

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities_another_countries[0])

                find_el(params, btn_destination_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_destination_address.xpath)
                click(params)
                send_keys(params, addresses[0])

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)

                # Выберем у КА страну Россию
                find_el(params, btn_country_selection_flag_corp_recipient.xpath)
                click(params)
                find_el(params, btn_country_selection_flag_ru_corp_recipient.xpath)
                click(params)

                set_counteragent_data(params, 'recipient', 'corporation', company_inn_number)

                """Смена валюты с бел руб на руб"""
                find_el(params, btn_currency_change_button_in_the_cost_block.xpath)
                click(params)

                find_el(params, btn_currency_change_ru_in_the_cost_block.xpath)
                click(params)
                price_to_load(params)

                """Нажимаем на кнопку 'Оформить'"""
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Нажимаем на кнопку 'Подтвердить' в попапе"""
                find_el(params, txt_currency_confirmation_header_in_the_currency_confirmation_popup.xpath)
                find_el(params, btn_confirm_in_the_currency_confirmation_popup.xpath)
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

        """3. Проверка создания заявки из Беларуси в Беларусь"""
        def tst_create_order_from_belarus_to_belarus():
            description = "Проверка создания заявки из Беларуси в Беларусь"

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities_another_countries[3])

                find_el(params, btn_dispatch_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_dispatch_address.xpath)
                click(params)
                send_keys(params, addresses[0])

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities_another_countries[0])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)

                # Выберем у КА страну Россию
                find_el(params, btn_country_selection_flag_corp_recipient.xpath)
                click(params)
                find_el(params, btn_country_selection_flag_ru_corp_recipient.xpath)
                click(params)

                set_counteragent_data(params, 'recipient', 'corporation', company_inn_number)

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

        status_and_name_tst = tst_create_order_from_belarus_to_russia()
        status_and_name_tst = tst_create_order_from_russia_to_belarus()
        status_and_name_tst = tst_create_order_from_belarus_to_belarus()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

