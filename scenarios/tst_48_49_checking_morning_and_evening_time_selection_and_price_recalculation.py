from Business_Actions import *
from Methods import *
from pages import order_create_page


def get_data_of_date_order(dispatch, destination, active_date, type_cargo_pickup):
    """Запросим доступные даты для расчета заказа"""

    part_a_of_url = "https://api.vozovoz.org/v3/order/timetable?dispatch%5BlocationGuid%5D=e90f19de-0128-11e5-80c7-00155d903d03&dispatch%5Bdate%5D="
    # part_time_of_url = f"{current_date.strftime('%Y-%m-')}"
    part_day_of_url = active_date
    part_b_of_url = "&destination%5BlocationGuid%5D=e90f1820-0128-11e5-80c7-00155d903d03&destination%5BpickupPointGuid%5D=dcfebc2f-03ac-11ef-9cdd-ac1f6b4782c3"
    base_url_api = part_a_of_url + part_day_of_url + part_b_of_url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    # Запрос данных о датах (метод GET)
    response_get = requests.get(base_url_api, headers=headers)

    # Json в формате словаря
    json_dict = response_get.json()

    # Достанем все, что находится в dispatch, а именно следующую дату отбытия
    data_of_dates = list(json_dict['dispatch'])
    next_date_data = data_of_dates[1]

    period = next_date_data['period']

    # Получим интервал для необходимо типа забора
    for i in period:
        if i['type'] == type_cargo_pickup:
            return i['intervalHour']


def checking_choice_of_morning_and_evening_time_in_order(params):
    main_description = "Тест №48-49 - Проверка выбора утреннего и вечернего времени при оформлении заказа"
    status_and_name_tst = {}

    authorization_lk(params, url_base_org, individual_phone_full, passw)

    try:
        """1. Проверка выбора утреннего времени"""
        def checking_the_morning_time_selection():
            description = "Проверка выбора утреннего времени"

            try:
                # Переходим на страницу оформления заказа
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                # Заполняем 'Отправка'
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, input_dispatch_address.xpath)
                click(params)
                send_keys(params, addresses[0])

                # Заполняем 'Прибытие'
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[2])

                find_el(params, btn_destination_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_destination_address.xpath)
                click(params)
                send_keys(params, addresses[1])

                # Выбираем следующую незадизэйбленную дату в Отправка
                find_el(params, choice_the_another_date_in_the_sending_feed_in_create_order_page.xpath)
                click(params)
                price_to_load(params)
                choice_date = get_the_data_from_element(params, choice_the_active_date_in_the_sending_feed_in_create_order_page.xpath, 3)

                # Получаем интервал для утреннего забора из запроса
                interval_morning = get_data_of_date_order(cities[0], cities[2], choice_date, 'morning')

                """Выбираем утреннее время"""
                find_el(params, input_time_from_dispatch_in_create_order_page.xpath)
                click(params)

                # Найдем заодно последнее время в диапазоне утра
                find_el(params, btn_choice_last_morning_time_in_dropdown_dispatch.xpath)
                time_morning_last = get_the_data_from_element(params, btn_choice_last_morning_time_in_dropdown_dispatch.xpath)

                # Выберем первое утреннее время
                find_el(params, btn_choice_morning_time_in_dropdown_dispatch.xpath)
                time_morning_first = get_the_data_from_element(params, btn_choice_morning_time_in_dropdown_dispatch.xpath)

                click(params)

                find_el(params, input_time_to_dispatch_in_create_order_page.xpath)
                click(params)

                result_time = add_up_the_time(time_morning_first, interval_morning)

                # Меняем xpath и подставляем сумму выбранного времени "С" + интервал, чтобы выбрать время, исходя из интервала
                btn_choice_default_time_in_dropdown_dispatch_x.change_xpath(result_time)
                find_el(params, btn_choice_default_time_in_dropdown_dispatch_x.xpath)
                click(params)
                price_to_load(params)
                btn_choice_default_time_in_dropdown_dispatch_x.reset_xpath()

                # Проверяем услуги в блоке "Стоимость"
                find_el(params, text_morning_pick_up_service_in_the_cost_block.xpath)

                """Отдельно проверим интервалы в утреннего времени"""
                find_el(params, input_time_to_dispatch_in_create_order_page.xpath)
                click(params)

                difference_in_the_morning_interval = add_up_the_time(time_morning_last, time_morning_first, False)  # Получим разницу утреннего интервала - 01:30
                border_with_morning_interval = add_up_the_time(result_time, difference_in_the_morning_interval)

                btn_choice_default_time_in_dropdown_dispatch_x.change_xpath(border_with_morning_interval)
                find_el(params, btn_choice_default_time_in_dropdown_dispatch_x.xpath)
                click(params)
                price_to_load(params)
                btn_choice_default_time_in_dropdown_dispatch_x.reset_xpath()

                # Проверяем услугу утреннее время в блоке "Стоимость"
                find_el(params, text_morning_pick_up_service_in_the_cost_block.xpath)

                """Отдельно проверим интервал вне утреннего времени"""
                find_el(params, input_time_to_dispatch_in_create_order_page.xpath)
                click(params)

                border_without_morning_interval = add_up_the_time(border_with_morning_interval, "00:30")

                btn_choice_default_time_in_dropdown_dispatch_x.change_xpath(border_without_morning_interval)
                find_el(params, btn_choice_default_time_in_dropdown_dispatch_x.xpath)
                click(params)
                price_to_load(params)
                btn_choice_default_time_in_dropdown_dispatch_x.reset_xpath()

                # Проверяем отсутствие услуг утреннего времени в блоке "Стоимость"
                invisibility_of_element(params, text_morning_pick_up_service_in_the_cost_block.xpath)

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

        """2. Проверка выбора вечернего времени"""
        def checking_the_evening_time_selection():
            description = "Проверка выбора вечернего времени"

            try:
                # Переходим на страницу оформления заказа
                set_page(params, url_base_org_order_create)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                # Заполняем 'Отправка'
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, input_dispatch_address.xpath)
                click(params)
                send_keys(params, addresses[0])

                # Заполняем 'Прибытие'
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[2])

                find_el(params, btn_destination_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_destination_address.xpath)
                click(params)
                send_keys(params, addresses[1])

                # Выбираем следующую незадизэйбленную дату в Отправка
                find_el(params, choice_the_another_date_in_the_sending_feed_in_create_order_page.xpath)
                click(params)
                price_to_load(params)
                choice_date = get_the_data_from_element(params, choice_the_active_date_in_the_sending_feed_in_create_order_page.xpath, 3)

                interval_evening = get_data_of_date_order(cities[0], cities[2], choice_date, 'evening')

                """Выбираем вечернее время"""
                # Кликаем в поле время "до"
                find_el(params, input_time_to_dispatch_in_create_order_page.xpath)
                click(params)

                # Находим вечернее время (последнее)
                find_el(params, btn_choice_evening_time_in_dropdown_dispatch.xpath)
                time_from = get_the_data_from_element(params, btn_choice_evening_time_in_dropdown_dispatch.xpath)
                click(params)

                # Кликаем в поле время "с"
                find_el(params, input_time_from_dispatch_in_create_order_page.xpath)
                click(params)

                result_time = add_up_the_time(time_from, interval_evening, False)

                # Меняем xpath и подставляем разницу выбранного времени "до" - интервал, чтобы выбрать время, исходя из интервала
                btn_choice_default_time_in_dropdown_dispatch_x.change_xpath(result_time)
                find_el(params, btn_choice_default_time_in_dropdown_dispatch_x.xpath)
                click(params)
                price_to_load(params)
                btn_choice_default_time_in_dropdown_dispatch_x.reset_xpath()

                # Проверяем услуги в блоке "Стоимость"
                find_el(params, text_evening_pick_up_service_in_the_cost_block.xpath)

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

        status_and_name_tst = checking_the_morning_time_selection()
        status_and_name_tst = checking_the_evening_time_selection()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()


