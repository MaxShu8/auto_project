from Business_Actions import *
from Methods import *
from pages import order_create_page


def checking_the_date_selection_from_feed_and_calendar(params):
    main_description = 'Тест №46 - Проверка выбора дат при оформлении заказа'
    status_and_name_tst = {}

    authorization_lk(params, url_base_org, individual_phone_full, passw)

    try:
        """1. Проверка выбора даты в ленте"""
        def checking_the_date_selection_from_feed():
            description = "Проверка выбора даты в ленте"

            #  Берем рандомно два неповторяющихся города из списка
            dispatch_city, destination_city = choice_cities(cities)

            try:
                # Переходим на страницу оформления заказа
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                # Заполняем 'Отправка'
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, dispatch_city)

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                # Заполняем 'Прибытие'
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, destination_city)

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Выбираем даты в Отправка/Прибытие"""
                # Сохраняем текущую дату и выбираем другую незадизэйбленную дату в Отправка
                find_el(params, choice_the_active_date_in_the_sending_feed_in_create_order_page.xpath)
                a = get_the_data_from_element(params, choice_the_active_date_in_the_sending_feed_in_create_order_page.xpath)
                default_date_dispatch = extract_numbers(a)

                find_el(params, choice_the_another_date_in_the_sending_feed_in_create_order_page.xpath)
                click(params)
                price_to_load(params)

                # Убедимся, что дата отправки задизэйблена или отсутствует в прибытии
                # choice_the_another_date_in_the_arrival_feed_in_create_order_page_x.change_xpath(default_date_dispatch)
                #
                # if check_text_attribute(params, choice_the_another_date_in_the_arrival_feed_in_create_order_page_x.xpath, 'disabled', True) is True:
                #
                # else:
                #     pass
                #
                # choice_the_another_date_in_the_arrival_feed_in_create_order_page_x.reset_xpath()

                # П
                # if check_text_attribute(params, choice_the_another_date_in_the_arrival_feed_in_create_order_page_x.xpath, default_date_dispatch, True) is True:
                #     find_el(params, choice_the_another_date_in_the_arrival_feed_in_create_order_page_x.xpath)
                #     click(params)
                #     price_to_load(params)

                # else:
                #     find_el(params, choice_the_another_date_in_the_arrival_feed_in_create_order_page.xpath)
                #     click(params)
                #     price_to_load(params)

                # Сохраняем текущую дату, проверяем что дата отправки задизэйблена и выбираем другую незадизэйбленную дату в Прибытие
                find_el(params, choice_the_active_date_in_the_arrival_feed_in_create_order_page.xpath)
                a = get_the_data_from_element(params, choice_the_active_date_in_the_arrival_feed_in_create_order_page.xpath)
                default_date_destination = extract_numbers(a)

                # Проверяем, если дата с какой-либо опцией то выбираем ее
                if check_text_attribute(params, choice_the_another_date_in_the_arrival_feed_in_create_order_page.xpath, 'discount', True) is True:
                    find_el(params, choice_the_another_date_with_status_in_the_arrival_feed_in_create_order_page.xpath)
                    click(params)
                    price_to_load(params)

                else:
                    find_el(params, choice_the_another_date_in_the_arrival_feed_in_create_order_page.xpath)
                    click(params)
                    price_to_load(params)

                # Вернем даты назад - сначала Прибытие
                choice_the_another_date_in_the_arrival_feed_in_create_order_page_x.change_xpath(default_date_destination)
                find_el(params, choice_the_another_date_in_the_arrival_feed_in_create_order_page_x.xpath)
                click(params)

                choice_the_another_date_in_the_arrival_feed_in_create_order_page_x.reset_xpath()

                # Вернем даты назад - Отправка
                choice_the_another_date_in_the_sending_feed_in_create_order_page_x.change_xpath(default_date_dispatch)
                find_el(params, choice_the_another_date_in_the_sending_feed_in_create_order_page_x.xpath)
                click(params)

                choice_the_another_date_in_the_sending_feed_in_create_order_page_x.reset_xpath()

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

        """2. Проверка выбора даты в календаре"""
        def checking_the_date_selection_from_calendar():
            description = "Проверка выбора даты в календаре"

            #  Берем рандомно два неповторяющихся города из списка
            dispatch_city, destination_city = choice_cities(cities)

            try:
                # Переходим на страницу оформления заказа
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                # Заполняем 'Отправка'
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, dispatch_city)

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                # Заполняем 'Прибытие'
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, destination_city)

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Выбираем календарь и даты в Отправка/Прибытие"""
                # Сохраняем текущую дату и выбираем другую незадизэйбленную дату в Отправка
                find_el(params, btn_calendar_in_dispatch_block.xpath)
                click(params)
                find_el(params, text_in_calendar_in_dispatch_block.xpath)

                find_el(params, btn_in_calendar_day_selected_dispatch_block.xpath)
                a = get_the_data_from_element(params, btn_in_calendar_day_selected_dispatch_block.xpath)
                default_date_dispatch = extract_numbers(a)

                find_el(params, btn_in_calendar_day_to_choice_dispatch_block.xpath)
                click(params)
                price_to_load(params)

                # Сохраняем текущую дату и выбираем другую незадизэйбленную дату в Прибытие
                find_el(params, btn_calendar_in_destination_block.xpath)
                click(params)
                find_el(params, text_in_calendar_in_destination_block.xpath)

                find_el(params, btn_in_calendar_day_selected_destination_block.xpath)
                a = get_the_data_from_element(params, btn_in_calendar_day_selected_destination_block.xpath)
                default_date_destination = extract_numbers(a)

                # Проверяем, если дата с какой-либо опцией то выбираем ее
                if check_text_attribute(params, btn_in_calendar_day_to_choice_destination_block.xpath, 'discount', True) is True:
                    find_el(params, btn_in_calendar_day_to_choice_with_status_destination_block.xpath)
                    click(params)
                    price_to_load(params)

                else:
                    find_el(params, btn_in_calendar_day_to_choice_destination_block.xpath)
                    click(params)
                    price_to_load(params)

                # Вернем даты назад - сначала Прибытие
                choice_the_another_date_in_the_destination_calendar_in_create_order_page_x.change_xpath(default_date_destination)
                find_el(params, choice_the_another_date_in_the_destination_calendar_in_create_order_page_x.xpath)
                click(params)

                choice_the_another_date_in_the_destination_calendar_in_create_order_page_x.reset_xpath()

                # Вернем даты назад - Отправка
                choice_the_another_date_in_the_dispatch_calendar_in_create_order_page_x.change_xpath(default_date_dispatch)
                find_el(params, choice_the_another_date_in_the_dispatch_calendar_in_create_order_page_x.xpath)
                click(params)

                choice_the_another_date_in_the_dispatch_calendar_in_create_order_page_x.reset_xpath()

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

        status_and_name_tst = checking_the_date_selection_from_feed()
        status_and_name_tst = checking_the_date_selection_from_calendar()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

