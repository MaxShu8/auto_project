from Business_Actions import *
from Methods import *
from pages.main_page import *


def checking_loading_operations_service(params):
    main_description = "Тест №54 - проверка опции 'Погрузочные работы'"
    status_and_name_tst = {}

    try:
        """1. Проверка опции 'Погрузочные работы' груз до 5 кг"""
        def checking_loading_operations_service_load_up_to_5_kg():
            description = "Проверка опции 'Погрузочные работы' груз до 5 кг"

            set_page(params, url_base_org_order_create_public)
            wait_page(params, url_base_org_order_create_public)
            price_to_load(params)

            try:

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

                """Устанавливаем ПРР в отправке/прибытии"""
                find_el(params, checkbox_cargo_loading_on_block_services_create_order_page.xpath)
                click(params)
                check_text_attribute(params, checkbox_cargo_loading_on_block_services_create_order_page.xpath, "checked")  # Проверим включен ли чекбокс

                find_el(params, checkbox_cargo_unloading_on_block_services_create_order_page.xpath)
                click(params)
                check_text_attribute(params, checkbox_cargo_unloading_on_block_services_create_order_page.xpath, "checked")  # Проверим включен ли чекбокс

                """Проверяем наличие услуги и ее нулевую стоимость в блоке Стоимость"""
                price_to_load(params)

                find_el(params, text_service_loading_operations_in_the_cost_block.xpath)
                price_prr_from_str = get_the_data_from_element(params, price_service_loading_operations_in_the_cost_block.xpath)
                price_prr_from = extract_numbers(price_prr_from_str)
                compare_numbers(price_prr_from, "0")

                find_el(params, text_service_uploading_operations_in_the_cost_block.xpath)
                price_prr_to_str = get_the_data_from_element(params, price_service_uploading_operations_in_the_cost_block.xpath)
                price_prr_to = extract_numbers(price_prr_to_str)
                compare_numbers(price_prr_to, "0")

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

        """2. Проверка опции 'Погрузочные работы' груз до 5 кг"""
        def checking_loading_operations_service_load_from_to_5_kg():
            description = "Проверка опции 'Погрузочные работы' груз от 5 кг включительно"

            try:
                set_page(params, url_base_org_order_create_public)
                wait_page(params, url_base_org_order_create_public)
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

                """Заполняем кол-во мест и массу груза"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                find_el(params, input_value_weight.xpath)
                send_keys(params, "5.1")

                """Устанавливаем ПРР в отправке/прибытии"""
                find_el(params, checkbox_cargo_loading_on_block_services_create_order_page.xpath)
                click(params)
                check_text_attribute(params, checkbox_cargo_loading_on_block_services_create_order_page.xpath, "checked")  # Проверим включен ли чекбокс

                find_el(params, checkbox_cargo_unloading_on_block_services_create_order_page.xpath)
                click(params)
                check_text_attribute(params, checkbox_cargo_unloading_on_block_services_create_order_page.xpath, "checked")  # Проверим включен ли чекбокс

                """Проверяем наличие услуги и ее нулевую стоимость в блоке Стоимость"""
                price_to_load(params)

                find_el(params, text_service_loading_operations_in_the_cost_block.xpath)
                price_prr_from_str = get_the_data_from_element(params, price_service_loading_operations_in_the_cost_block.xpath)
                price_prr_from = extract_numbers(price_prr_from_str)
                compare_numbers(price_prr_from, "0", "more")

                find_el(params, text_service_uploading_operations_in_the_cost_block.xpath)
                price_prr_to_str = get_the_data_from_element(params, price_service_uploading_operations_in_the_cost_block.xpath)
                price_prr_to = extract_numbers(price_prr_to_str)
                compare_numbers(price_prr_to, "0", "more")

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

        """3. Проверка установки услуги при выборе Корреспонденции"""
        def checking_service_prr_when_selecting_correspondence():
            description = "Проверка установки услуги при выборе Корреспонденции"

            try:
                set_page(params, url_base_org_order_create_public)
                wait_page(params, url_base_org_order_create_public)
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

                """Заполняем кол-во мест и массу груза"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                find_el(params, input_value_weight.xpath)
                send_keys(params, "5.1")

                """Выключим чек-бокс груз и включим только Корреспонденцию"""
                find_el(params, checkbox_correspondence_in_cargo_block_in_order_create_page.xpath)
                click(params)
                check_text_attribute(params, checkbox_correspondence_in_cargo_block_in_order_create_page.xpath, "checked")

                find_el(params, checkbox_cargo_in_cargo_block_in_order_create_page.xpath)
                click(params)

                if check_text_attribute(params, checkbox_cargo_loading_on_block_services_create_order_page.xpath, "checked", True) is False:
                    pass
                else:
                    raise Exception

                """Устанавливаем ПРР в отправке/прибытии"""
                find_el(params, checkbox_cargo_loading_on_block_services_create_order_page.xpath)
                click(params)
                check_text_attribute(params, checkbox_cargo_loading_on_block_services_create_order_page.xpath, "checked")  # Проверим включен ли чекбокс

                find_el(params, checkbox_cargo_unloading_on_block_services_create_order_page.xpath)
                click(params)
                check_text_attribute(params, checkbox_cargo_unloading_on_block_services_create_order_page.xpath, "checked")  # Проверим включен ли чекбокс

                """Проверяем наличие услуги и ее нулевую стоимость в блоке Стоимость"""
                price_to_load(params)

                find_el(params, text_service_loading_operations_in_the_cost_block.xpath)
                price_prr_from_str = get_the_data_from_element(params, price_service_loading_operations_in_the_cost_block.xpath)
                price_prr_from = extract_numbers(price_prr_from_str)
                compare_numbers(price_prr_from, "0", "equal")

                find_el(params, text_service_uploading_operations_in_the_cost_block.xpath)
                price_prr_to_str = get_the_data_from_element(params, price_service_uploading_operations_in_the_cost_block.xpath)
                price_prr_to = extract_numbers(price_prr_to_str)
                compare_numbers(price_prr_to, "0", "equal")

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

        status_and_name_tst = checking_loading_operations_service_load_up_to_5_kg()
        status_and_name_tst = checking_loading_operations_service_load_from_to_5_kg()
        status_and_name_tst = checking_service_prr_when_selecting_correspondence()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

