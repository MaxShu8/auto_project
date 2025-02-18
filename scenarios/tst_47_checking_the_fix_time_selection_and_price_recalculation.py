from Business_Actions import *
from Methods import *
from pages import order_create_page


def get_data_of_date_order(dispatch, destination, active_date, type_cargo_pickup):
    """Запросим доступные даты для расчета заказа"""

    part_a_of_url = "https://api.vozovoz.org/v3/order/timetable?dispatch%5BlocationGuid%5D=e90f19de-0128-11e5-80c7-00155d903d03&dispatch%5Bdate%5D="

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
            if i['type'] == 'fixed':
                return i['from'], i['to']
            else:
                return i['intervalHour']


def checking_choice_of_fix_time_in_order(params):
    main_description = "Тест №47 - Проверка выбора фиксированного времени при оформлении заказа"
    status_and_name_tst = {}

    authorization_lk(params, url_base_org, individual_phone_full, passw)

    try:
        """1. Проверка выбора фиксированного времени и отображения услуги в блоке Стоимость"""
        def checking_the_fixed_time_selection_in_from_and_to():
            description = "Проверка выбора фиксированного времени и отображения услуги в блоке Стоимость"

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

                # Получаем интервал для фиксированного забора из запроса
                interval_from, interval_to = get_data_of_date_order(cities[0], cities[2], choice_date, 'fixed')

                # Достаем временные интервалы по фиксу
                interval_from = extract_time_from_block_direction(interval_from)
                interval_to = extract_time_from_block_direction(interval_to)

                """Выбираем фиксированное время в Отправка и Прибытие"""
                find_el(params, checkbox_fixed_time_dispatch_in_create_order_page.xpath)
                click(params)
                price_to_load(params)

                find_el(params, checkbox_fixed_time_destination_in_create_order_page.xpath)
                click(params)
                price_to_load(params)

                # Проверяем услуги в блоке "Стоимость"
                find_el(params, text_fixed_time_service_from_in_the_cost_block.xpath)
                find_el(params, text_fixed_time_service_to_in_the_cost_block.xpath)

                """Убираем фиксированное время в Отправка и Прибытие"""
                find_el(params, checkbox_fixed_time_dispatch_in_create_order_page.xpath)
                click(params)
                price_to_load(params)

                find_el(params, checkbox_fixed_time_destination_in_create_order_page.xpath)
                click(params)
                price_to_load(params)

                # Проверяем отсутствие услуг фиксированного времени в блоке "Стоимость"
                invisibility_of_element(params, text_fixed_time_service_from_in_the_cost_block.xpath)
                invisibility_of_element(params, text_fixed_time_service_to_in_the_cost_block.xpath)

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst, interval_from, interval_to

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        """2. Проверка установки/снятия фикс времени, исходя из диапазона"""
        def checking_the_interval_fixed_time_selection(time_a, time_b):
            description = "Проверка установки/снятия фикс времени, исходя из диапазона"

            try:
                """Выбираем одинаковое время в С и ДО"""
                find_el(params, input_time_from_dispatch_in_create_order_page.xpath)
                click(params)

                btn_choice_default_time_in_dropdown_dispatch_x.change_xpath(time_a)  # Выбираем нижний интервал
                find_el(params, btn_choice_default_time_in_dropdown_dispatch_x.xpath)
                click(params)
                price_to_load(params)

                btn_choice_default_time_in_dropdown_dispatch_x.reset_xpath()

                find_el(params, input_time_to_dispatch_in_create_order_page.xpath)
                click(params)

                btn_choice_default_time_in_dropdown_dispatch_x.change_xpath(time_a)  # Выбираем нижний интервал
                find_el(params, btn_choice_default_time_in_dropdown_dispatch_x.xpath)
                click(params)
                price_to_load(params)

                btn_choice_default_time_in_dropdown_dispatch_x.reset_xpath()

                # Проверяем услуги в блоке "Стоимость"
                find_el(params, text_fixed_time_service_from_in_the_cost_block.xpath)

                """Выбираем время в ДО в интервале фикса"""
                no_fix = add_up_the_time(time_a, 4.5)

                find_el(params, input_time_to_dispatch_in_create_order_page.xpath)
                click(params)

                btn_choice_default_time_in_dropdown_dispatch_x.change_xpath(no_fix)  # Выбираем интервал, где должен быть фикс
                find_el(params, btn_choice_default_time_in_dropdown_dispatch_x.xpath)
                click(params)
                price_to_load(params)

                btn_choice_default_time_in_dropdown_dispatch_x.reset_xpath()

                # Проверяем услуги в блоке "Стоимость"
                find_el(params, text_fixed_time_service_from_in_the_cost_block.xpath)

                """Выбираем время в ДО в интервале дневного, чтобы фикс исчез"""
                no_fix = add_up_the_time(time_a, 5)

                find_el(params, input_time_to_dispatch_in_create_order_page.xpath)
                click(params)

                btn_choice_default_time_in_dropdown_dispatch_x.change_xpath(no_fix)  # Выбираем интервал где должен быть фикс
                find_el(params, btn_choice_default_time_in_dropdown_dispatch_x.xpath)
                click(params)
                price_to_load(params)

                btn_choice_default_time_in_dropdown_dispatch_x.reset_xpath()

                # Проверяем отсутствие услуг фиксированного времени в блоке "Стоимость"
                invisibility_of_element(params, text_fixed_time_service_from_in_the_cost_block.xpath)
                invisibility_of_element(params, text_fixed_time_service_to_in_the_cost_block.xpath)

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

        status_and_name_tst, time_from, time_to = checking_the_fixed_time_selection_in_from_and_to()
        status_and_name_tst = checking_the_interval_fixed_time_selection(time_from, time_to)

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()


