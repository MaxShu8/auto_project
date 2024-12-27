from Business_Actions import *
from Methods import *

def check_data_transfer_from_mini_calculator(params):
    main_description = 'Тест №15 - Проверка переноса данных c мини-калькулятора'
    status_and_name_tst = {}

    # Берем рандомно два неповторяющихся города из списка
    dispatch_city, destination_city = choice_cities(cities)

    # Возьмем рандомные значения веса и объема
    volume = various_data.value_volume
    weight = various_data.value_weight

    try:
        """1. Проверка переноса населенных пунктов"""
        def checking_the_transfer_of_settlements():
            description = "Проверка переноса населенных пунктов"

            try:
                # Главная страница
                set_page(params, url_base_org)
                wait_page(params, url_base_org)
                price_to_load(params)

                # Ищем поле Откуда и устанавливаем там город
                find_el(params, input_from_mini.xpath)
                click(params)
                set_dispatch_city(params, dispatch_city)

                price_to_load(params)

                check_text_attribute(params, input_from_mini.xpath, dispatch_city)

                # Ищем кнопку от терминала и кликаем
                find_el(params, btn_from_terminal.xpath)
                click(params)

                price_to_load(params)

                check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')

                # Ищем поле Куда и устанавливаем там город
                find_el(params, input_to_mini.xpath)
                click(params)
                set_destination_city(params, city_kz)

                price_to_load(params)

                # Ищем кнопку до терминала и кликаем
                find_el(params, btn_to_terminal.xpath)
                click(params)

                price_to_load(params)

                check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')

                # Вводим данные объема и веса
                find_el(params, input_value_volume.xpath)
                click(params)
                send_keys(params, volume)
                price_to_load(params)

                find_el(params, inp_weight_mini_calc.xpath)
                click(params)
                send_keys(params, weight)
                price_to_load(params)

                # Ищем кнопку "Рассчитать" и кликаем
                find_el(params, btn_calculate_mini_calc.xpath)
                click(params)
                find_el(params, text_placing_an_order.xpath)
                price_to_load(params)

                # Сверяем указанные ранее города
                check_text_attribute(params, input_dispatch_city.xpath, dispatch_city)
                check_text_attribute(params, input_destination_city.xpath, city_kz)

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

        """2. Проверка переноса объема и веса"""
        def checking_volume_and_weight_transfer():
            description = "Проверка переноса объема и веса"

            try:
                # Сверяем указанные объем и вес
                find_el(params, input_value_volume.xpath)  # проскролим к полю
                check_text_attribute(params, input_value_volume.xpath, volume)

                find_el(params, input_value_weight.xpath)
                check_text_attribute(params, input_value_weight.xpath, weight)

                description = "Проверка переноса валюты (например, тенге)"

                # Сверяем указанную валюту
                check_text_attribute(params, price_in_block_price.xpath, 'тенге')

                description = "Проверка переноса (от/до терминала, адреса, ПВЗ)"

                # Проверим выбраны ли кнопки "Терминал", которые выбрали ранее
                check_text_attribute(params, btn_dispatch_terminal_check_status.xpath, 'active')
                check_text_attribute(params, btn_destination_terminal_check_status.xpath, 'active')

                # Вернемся на главную
                set_page(params, url_base_org)
                wait_page(params, url_base_org)
                price_to_load(params)

                # Ищем кнопку до адреса и кликаем
                find_el(params, btn_to_address.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_to_address.xpath, 'active')

                # Ищем кнопку "Рассчитать" и кликаем
                find_el(params, btn_calculate_mini_calc.xpath)
                click(params)
                find_el(params, text_placing_an_order.xpath)
                price_to_load(params)

                # Проверим выбраны ли кнопки "Терминал" -> "Адрес", которые выбрали ранее
                check_text_attribute(params, btn_dispatch_terminal_check_status.xpath, 'active')
                check_text_attribute(params, btn_destination_address_check_status.xpath, 'active')

                # Вернемся на главную
                set_page(params, url_base_org)
                wait_page(params, url_base_org)
                price_to_load(params)

                # Ищем кнопку от адреса и кликаем
                find_el(params, btn_from_address.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_address.xpath, 'active')

                # Ищем кнопку до ПВЗ и кликаем
                find_el(params, btn_to_pvz.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_to_pvz.xpath, 'active')

                # Ищем кнопку "Рассчитать" и кликаем
                find_el(params, btn_calculate_mini_calc.xpath)
                click(params)
                find_el(params, text_placing_an_order.xpath)
                price_to_load(params)

                # Проверим выбраны ли кнопки "Адрес" -> "ПВЗ", которые выбрали ранее
                check_text_attribute(params, btn_dispatch_address_check_status.xpath, 'active')
                check_text_attribute(params, btn_destination_pvz.xpath, 'active')

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

        status_and_name_tst = checking_the_transfer_of_settlements()
        status_and_name_tst = checking_volume_and_weight_transfer()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()
