from Business_Actions import *
from Methods import *
from pages import order_create_page


def checking_the_date_selection_from_feed_and_calendar(params):
    main_description = 'Тест №46 - Проверка выбора дат при оформлении заказа'
    status_and_name_tst = {}

    #  Берем рандомно два неповторяющихся города из списка
    dispatch_city, destination_city = choice_cities(cities)

    try:
        """1. Проверка выбора даты в ленте"""
        def checking_the_date_selection_from_feed():
            description = "Проверка выбора даты в ленте"

            try:
                authorization_lk(params, url_base_org, individual_phone_full, passw)

                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, dispatch_city)

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, destination_city)

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Сохраняем текущую дату и выбираем другую незадизэйбленную дату в Отправка"""
                find_el(params, choice_the_active_date_in_the_arrival_feed_in_create_order_page.xpath)
                a = get_the_data_from_element(params, choice_the_active_date_in_the_arrival_feed_in_create_order_page.xpath)
                number_of_date = extract_numbers(a)




                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'corporation', company_inn_number)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio)

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

        status_and_name_tst = checking_the_date_selection_from_feed()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()





