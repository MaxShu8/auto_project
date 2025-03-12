from Business_Actions import *
from Methods import *
from pages.order_details import *


def check_create_order_based_on_exist_order(params):
    main_description = 'Тест №88 - Создание заказа на основании существующего заказа'
    status_and_name_tst = {}

    #  Берем рандомно два неповторяющихся города из списка
    dispatch_city, destination_city = choice_cities(cities)

    try:
        """1. Создание заказа на основании существующего заказа: Терминал-->Терминал (Физ.лицо-Физ.лицо)"""
        def create_order_based_on_order_terminal_terminal_ind_ind():
            authorization_lk(params, url_base_org, individual_phone_full, passw)

            description = "Проверка данных в заказе, созданном на основании: терминал-->терминал, физ.лицо - физ.лицо"
            packages = ['Мешок 55×105', 'Коробка 40×20×20', 'Прозрачная плёнка', 'Паллетный борт',
                        'Упаковка в сейф-пакет']

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем блок Направление - Отправка"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)
                check_text_attribute(params, btn_dispatch_terminal.xpath, 'active')  # Проверим, включена ли кнопка Терминал

                """Заполняем блок Направление - Прибытие"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[1])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)
                check_text_attribute(params, btn_destination_terminal.xpath, 'active')  # Проверим, включена ли кнопка Терминал

                # Вытащим данные из Отправки
                data_dispatch_city = get_the_data_from_element(params, input_dispatch_city.xpath, 1)
                data_dispatch_terminal = get_the_data_from_element(params, btn_dispatch_terminal.xpath)
                data_dispatch_address_terminal = get_the_data_from_element(params, input_from_terminal_in_create_order_page.xpath)
                data_date_send_terminal = get_the_data_from_element(params, btn_active_date_in_the_send_in_the_calendar.xpath)
                data_date_send_terminal = extract_numbers(data_date_send_terminal)
                data_time_send_terminal = get_the_data_from_element(params, input_time_from_dispatch_terminal_in_create_order_page.xpath)

                # Вытащим данные из Прибытия
                data_destination_city = get_the_data_from_element(params, input_destination_city.xpath, 1)
                data_destination_terminal = get_the_data_from_element(params, btn_destination_terminal.xpath)
                data_destination_address_terminal = get_the_data_from_element(params, input_to_terminal_in_create_order_page.xpath)
                data_date_arrival_terminal = get_the_data_from_element(params, btn_active_date_in_the_arrival_in_the_calendar.xpath)
                data_date_arrival_terminal = extract_numbers(data_date_arrival_terminal)
                data_time_arrival_terminal = get_the_data_from_element(params, input_time_from_destination_in_create_order_page.xpath)

                """Заполняем блок Груз - вкладка (Габариты)"""
                # Заполняем "Общие габариты"
                find_el(params, input_value_places_in_order_create_page.xpath)
                set_places(params)
                price_to_load(params)

                find_el(params, input_value_weight_in_order_create_page.xpath)
                click(params)  # клик нужен, чтобы убрать фокус с предыдущего поля
                set_weight(params)
                price_to_load(params)

                find_el(params, input_value_volume_in_order_create_page.xpath)
                click(params)  # клик нужен, чтобы убрать фокус с предыдущего поля
                set_volume(params)
                price_to_load(params)

                # Заполняем "Максимальные габариты одного места"
                # find_el(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                # send_keys(params, '0.21')
                # find_el(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                # send_keys(params, '0.22')
                # find_el(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                # send_keys(params, '0.23')
                # find_el(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                # send_keys(params, '11')

                # Выбираем категорию "Игрушки"
                find_el(params, inp_cargo_category_in_calculation_and_ordering_page.xpath)
                click(params)
                find_el(params, choice_sort_subcategory_toys_in_calculation_and_ordering_page.xpath)
                click(params)
                find_el(params, choice_sort_category_toys_in_calculation_and_ordering_page.xpath)
                click(params)
                price_to_load(params)

                # Добавляем упаковку
                find_el(params, btn_add_button_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_pallet_board_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_additional_packaging_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_boxes_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_bags_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_safe_package_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, btn_apply_in_the_package_view_modal_create_order_page.xpath)
                click(params)
                price_to_load(params)

                # Достанем список упаковок и проверим, что они добавлены при оформлении заказа
                list_of_packages = get_the_data_from_block_of_elements(params, list_block_with_packaging_elements_in_create_order_page.xpath, 1)
                exist_elements_of_list_in_list(list_of_packages, packages)

                # Устанавливаем страхование
                find_el(params, btn_insurance_field_in_the_create_order_form.xpath)
                click(params)
                find_el(params, btn_choosing_cargo_insurance_in_insurance_block_in_create_order_form.xpath)
                click(params)
                price_to_load(params)
                find_el(params, inp_amount_field_in_the_insurance_in_create_order_form.xpath)
                send_keys(params, value_insurance)

                # Устанавливаем "Ваш номер перевозки"
                find_el(params, inp_field_is_your_transportation_number_in_create_order_form.xpath)
                send_keys(params, individual_order_with_text)

                # Вытащим данные из блока "Груз"
                data_places = get_the_data_from_element(params, input_value_places.xpath, 1)
                data_weight = get_the_data_from_element(params, input_value_weight.xpath, 1)
                data_volume = get_the_data_from_element(params, input_value_volume.xpath, 1)
                # data_length_max_place = get_the_data_from_element(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                # data_width_max_place = get_the_data_from_element(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                # data_height_max_place = get_the_data_from_element(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                # data_weight_max_place = get_the_data_from_element(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_category = get_the_data_from_element(params, choice_sort_subcategory_toys_in_calculation_and_ordering_page.xpath)
                data_insurance = get_the_data_from_element(params, inp_amount_field_in_the_insurance_in_create_order_form.xpath, 1)
                data_your_transportation_number = get_the_data_from_element(params, inp_field_is_your_transportation_number_in_create_order_form.xpath, 1)

                """Заполняем блок Доп.услуги"""
                find_el(params, checkbox_scan_of_the_delivery_invoice_in_the_add_on_block_services_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_return_the_accompanying_documents_in_the_add_on_block_services_create_order_page.xpath)
                click(params)
                # find_el(params, checkbox_disassembly_of_packaging_upon_delivery_to_the_address_on_block_services_create_order_page.xpath)
                # click(params)
                find_el(params, btn_terminal_in_the_additional_services_section_in_create_order_form.xpath)
                click(params)

                # Вытащим данные из блока "Доп.услуги"
                data_scan_of_the_delivery_invoice = get_the_data_from_element(params, checkbox_scan_of_the_delivery_invoice_in_the_add_on_block_services_create_order_page.xpath)
                data_return_the_accompanying_documents = get_the_data_from_element(params, checkbox_return_the_accompanying_documents_in_the_add_on_block_services_create_order_page.xpath)
                # data_disassembly_of_packaging_upon = get_the_data_from_element(params, checkbox_disassembly_of_packaging_upon_delivery_to_the_address_on_block_services_create_order_page.xpath)

                """Заполняем блок Плательщик"""
                find_el(params, btn_recipient_in_the_payer_block_in_create_order_form.xpath)
                click(params)

                # Вытащим данные из блока "Плательщик"
                data_recipient = get_the_data_from_element(params, btn_recipient_in_the_payer_block_in_create_order_form.xpath)

                """Заполняем блок Участники (физ.лицо-физ.лицо)"""
                # Заполняем участников
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio_2, individual_phone_2)

                # Вытащим данные из блока "Участники"
                data_fio_ind_sender = get_the_data_from_element(params, input_fio_ind_sender.xpath, 1)
                data_phone_ind_sender = get_the_data_from_element(params, input_phone_ind_sender.xpath, 1)
                data_phone_ind_sender = extract_numbers(data_phone_ind_sender)
                data_fio_ind_recipient = get_the_data_from_element(params, input_fio_ind_recipient.xpath, 1)
                data_phone_ind_recipient = get_the_data_from_element(params, input_phone_ind_recipient.xpath, 1)
                data_phone_ind_recipient = extract_numbers(data_phone_ind_recipient)

                # Нажимаем на кнопку "Оформить"
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)
                price_to_load(params)

                """Создание заказа на основании"""
                find_el(params, btn_create_based_on_in_details_page.xpath)
                click(params)

                url_contain_url(params, url_base_org_order_create)
                switch_to_next_or_previous_tab(params)
                price_to_load(params)

                """Сверим данные в новом заказе"""
                # Данные блока "Отправка"
                find_el(params, txt_order_in_calculation_and_ordering_page.xpath)
                check_text_attribute(params, input_dispatch_city.xpath, data_dispatch_city)
                check_text_attribute(params, btn_dispatch_terminal.xpath, "active")
                check_text_attribute(params, input_from_terminal_in_create_order_page.xpath, data_dispatch_address_terminal)
                check_text_attribute(params, choice_the_active_date_in_the_sending_feed_in_create_order_page.xpath, data_date_send_terminal)
                check_text_attribute(params, input_time_from_dispatch_terminal_in_create_order_page.xpath, data_time_send_terminal)

                # Данные блока "Прибытие"
                check_text_attribute(params, input_destination_city.xpath, data_destination_city)
                check_text_attribute(params, btn_destination_terminal.xpath, "active")
                check_text_attribute(params, input_to_terminal_in_create_order_page.xpath, data_destination_address_terminal)
                check_text_attribute(params, choice_the_active_date_in_the_arrival_feed_in_create_order_page.xpath, data_date_arrival_terminal)
                check_text_attribute(params, input_time_from_destination_in_create_order_page.xpath, data_time_arrival_terminal)

                # Данные блока "Груз" - Общие габариты
                check_text_attribute(params, input_value_volume_in_order_create_page.xpath, data_volume, False, True)
                check_text_attribute(params, input_value_weight_in_order_create_page.xpath, data_weight, False, True)
                check_text_attribute(params, input_value_places_in_order_create_page.xpath, f"{str(int(data_places) + 2)}")

                # Данные блока "Груз" - Максимальные габариты одного места
                # check_text_attribute(params, data_length_in_the_maximum_seat_dimensions_in_details_page.xpath, data_length_max_place)
                # check_text_attribute(params, data_width_in_the_maximum_seat_dimensions_in_details_page.xpath, data_width_max_place)
                # check_text_attribute(params, data_height_in_the_maximum_seat_dimensions_in_details_page.xpath, data_height_max_place)
                # check_text_attribute(params, data_weight_in_the_maximum_seat_dimensions_in_details_page.xpath, data_weight_max_place)

                # Данные блока "Груз" - Категория груза
                check_text_attribute(params, data_selected_cargo_category_in_create_order_page.xpath, data_category)

                # Данные блока "Груз" - Упаковка груза (достанем список упаковок и проверим, что они добавлены в детализацию заказа)
                list_of_packages_details = get_the_data_from_block_of_elements(params, data_cargo_package_in_the_cargo_block_in_create_order_page.xpath, 1)
                exist_elements_of_list_in_list(list_of_packages_details, packages)

                # Данные блока "Груз" - Страхование груза
                check_text_attribute(params, inp_amount_field_in_the_insurance_in_create_order_form.xpath, data_insurance)

                # Данные блока "Доп.услуги"
                check_text_attribute(params, check_checkbox_scan_of_the_delivery_invoice_in_the_add_on_block_services_create_order_page.xpath, "checked")
                check_text_attribute(params, check_checkbox_return_the_accompanying_documents_in_the_add_on_block_services_create_order_page.xpath, "checked")
                # check_text_attribute(params, check_checkbox_disassembly_of_packaging_upon_delivery_to_the_address_on_block_services_create_order_page.xpath, "checked")

                # Данные блока "Плательщик"
                check_text_attribute(params, check_btn_recipient_in_the_payer_block_in_create_order_form.xpath, "active")

                # Данные блока "Участники"
                check_text_attribute(params, btn_type_ind_sender.xpath, "active")
                check_text_attribute(params, btn_type_ind_recipient.xpath, "active")
                check_text_attribute(params, input_fio_ind_sender.xpath, data_fio_ind_sender)
                check_text_attribute(params, input_phone_ind_sender.xpath, '+7 (999) 022-00-38')
                check_text_attribute(params, input_fio_ind_recipient.xpath, data_fio_ind_recipient)
                check_text_attribute(params, input_phone_ind_recipient.xpath, '+7 (981) 784-26-24')

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

        """2. Создание заказа на основании существующего заказа: Адрес-->ПВЗ (Юр.лицо-Физ.лицо)"""
        def create_order_based_on_order_address_pvz_comp_ind():
            authorization_lk(params, url_base_org, individual_phone_full, passw)
            description = "Создание заказа на основании существующего заказа"

            description = "Проверка данных в заказе, созданном на основании: адрес-->ПВЗ, юр.лицо - физ.лицо"
            packages = ['Мешок 55×105', 'Коробка 40×20×20', 'Прозрачная плёнка', 'Паллетный борт',
                        'Упаковка в сейф-пакет']

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем блок Направление - Отправка"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)
                check_text_attribute(params, btn_dispatch_terminal.xpath,
                                     'active')  # Проверим, включена ли кнопка Терминал

                """Заполняем блок Направление - Прибытие"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[1])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)
                check_text_attribute(params, btn_destination_terminal.xpath,
                                     'active')  # Проверим, включена ли кнопка Терминал

                # Вытащим данные из Отправки
                data_dispatch_city = get_the_data_from_element(params, input_dispatch_city.xpath, 1)
                data_dispatch_terminal = get_the_data_from_element(params, btn_dispatch_terminal.xpath)
                data_dispatch_address_terminal = get_the_data_from_element(params,
                                                                           input_from_terminal_in_create_order_page.xpath)
                data_date_send_terminal = get_the_data_from_element(params,
                                                                    btn_active_date_in_the_send_in_the_calendar.xpath)
                data_date_send_terminal = extract_numbers(data_date_send_terminal)
                data_time_send_terminal = get_the_data_from_element(params,
                                                                    input_time_from_dispatch_terminal_in_create_order_page.xpath)

                # Вытащим данные из Прибытия
                data_destination_city = get_the_data_from_element(params, input_destination_city.xpath, 1)
                data_destination_terminal = get_the_data_from_element(params, btn_destination_terminal.xpath)
                data_destination_address_terminal = get_the_data_from_element(params,
                                                                              input_to_terminal_in_create_order_page.xpath)
                data_date_arrival_terminal = get_the_data_from_element(params,
                                                                       btn_active_date_in_the_arrival_in_the_calendar.xpath)
                data_date_arrival_terminal = extract_numbers(data_date_arrival_terminal)
                data_time_arrival_terminal = get_the_data_from_element(params,
                                                                       input_time_from_destination_in_create_order_page.xpath)

                """Заполняем блок Груз - вкладка (Габариты)"""
                # Заполняем "Общие габариты"
                find_el(params, input_value_places_in_order_create_page.xpath)
                set_places(params)
                price_to_load(params)

                find_el(params, input_value_weight_in_order_create_page.xpath)
                click(params)  # клик нужен, чтобы убрать фокус с предыдущего поля
                set_weight(params)
                price_to_load(params)

                find_el(params, input_value_volume_in_order_create_page.xpath)
                click(params)  # клик нужен, чтобы убрать фокус с предыдущего поля
                set_volume(params)
                price_to_load(params)

                # Заполняем "Максимальные габариты одного места"
                # find_el(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                # send_keys(params, '0.21')
                # find_el(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                # send_keys(params, '0.22')
                # find_el(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                # send_keys(params, '0.23')
                # find_el(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                # send_keys(params, '11')

                # Выбираем категорию "Игрушки"
                find_el(params, inp_cargo_category_in_calculation_and_ordering_page.xpath)
                click(params)
                find_el(params, choice_sort_subcategory_toys_in_calculation_and_ordering_page.xpath)
                click(params)
                find_el(params, choice_sort_category_toys_in_calculation_and_ordering_page.xpath)
                click(params)
                price_to_load(params)

                # Добавляем упаковку
                find_el(params, btn_add_button_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_pallet_board_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_additional_packaging_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_boxes_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_bags_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_safe_package_in_the_modal_type_of_packaging_create_order_page.xpath)
                click(params)
                find_el(params, btn_apply_in_the_package_view_modal_create_order_page.xpath)
                click(params)
                price_to_load(params)

                # Достанем список упаковок и проверим, что они добавлены при оформлении заказа
                list_of_packages = get_the_data_from_block_of_elements(params,
                                                                       list_block_with_packaging_elements_in_create_order_page.xpath,
                                                                       1)
                exist_elements_of_list_in_list(list_of_packages, packages)

                # Устанавливаем страхование
                find_el(params, btn_insurance_field_in_the_create_order_form.xpath)
                click(params)
                find_el(params, btn_choosing_cargo_insurance_in_insurance_block_in_create_order_form.xpath)
                click(params)
                price_to_load(params)
                find_el(params, inp_amount_field_in_the_insurance_in_create_order_form.xpath)
                send_keys(params, value_insurance)

                # Устанавливаем "Ваш номер перевозки"
                find_el(params, inp_field_is_your_transportation_number_in_create_order_form.xpath)
                send_keys(params, individual_order_with_text)

                # Вытащим данные из блока "Груз"
                data_places = get_the_data_from_element(params, input_value_places.xpath, 1)
                data_weight = get_the_data_from_element(params, input_value_weight.xpath, 1)
                data_volume = get_the_data_from_element(params, input_value_volume.xpath, 1)
                # data_length_max_place = get_the_data_from_element(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                # data_width_max_place = get_the_data_from_element(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                # data_height_max_place = get_the_data_from_element(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                # data_weight_max_place = get_the_data_from_element(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_category = get_the_data_from_element(params,
                                                          choice_sort_subcategory_toys_in_calculation_and_ordering_page.xpath)
                data_insurance = get_the_data_from_element(params,
                                                           inp_amount_field_in_the_insurance_in_create_order_form.xpath,
                                                           1)
                data_your_transportation_number = get_the_data_from_element(params,
                                                                            inp_field_is_your_transportation_number_in_create_order_form.xpath,
                                                                            1)

                """Заполняем блок Доп.услуги"""
                find_el(params,
                        checkbox_scan_of_the_delivery_invoice_in_the_add_on_block_services_create_order_page.xpath)
                click(params)
                find_el(params,
                        checkbox_return_the_accompanying_documents_in_the_add_on_block_services_create_order_page.xpath)
                click(params)
                # find_el(params, checkbox_disassembly_of_packaging_upon_delivery_to_the_address_on_block_services_create_order_page.xpath)
                # click(params)
                find_el(params, btn_terminal_in_the_additional_services_section_in_create_order_form.xpath)
                click(params)

                # Вытащим данные из блока "Доп.услуги"
                data_scan_of_the_delivery_invoice = get_the_data_from_element(params,
                                                                              checkbox_scan_of_the_delivery_invoice_in_the_add_on_block_services_create_order_page.xpath)
                data_return_the_accompanying_documents = get_the_data_from_element(params,
                                                                                   checkbox_return_the_accompanying_documents_in_the_add_on_block_services_create_order_page.xpath)
                # data_disassembly_of_packaging_upon = get_the_data_from_element(params, checkbox_disassembly_of_packaging_upon_delivery_to_the_address_on_block_services_create_order_page.xpath)

                """Заполняем блок Плательщик"""
                find_el(params, btn_recipient_in_the_payer_block_in_create_order_form.xpath)
                click(params)

                # Вытащим данные из блока "Плательщик"
                data_recipient = get_the_data_from_element(params,
                                                           btn_recipient_in_the_payer_block_in_create_order_form.xpath)

                """Заполняем блок Участники (физ.лицо-физ.лицо)"""
                # Заполняем участников
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio_2, individual_phone_2)

                # Вытащим данные из блока "Участники"
                data_fio_ind_sender = get_the_data_from_element(params, input_fio_ind_sender.xpath, 1)
                data_phone_ind_sender = get_the_data_from_element(params, input_phone_ind_sender.xpath, 1)
                data_phone_ind_sender = extract_numbers(data_phone_ind_sender)
                data_fio_ind_recipient = get_the_data_from_element(params, input_fio_ind_recipient.xpath, 1)
                data_phone_ind_recipient = get_the_data_from_element(params, input_phone_ind_recipient.xpath, 1)
                data_phone_ind_recipient = extract_numbers(data_phone_ind_recipient)

                # Нажимаем на кнопку "Оформить"
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)
                price_to_load(params)

                """Создание заказа на основании"""
                find_el(params, btn_create_based_on_in_details_page.xpath)
                click(params)

                url_contain_url(params, url_base_org_order_create)
                switch_to_next_or_previous_tab(params)
                price_to_load(params)

                """Сверим данные в новом заказе"""
                # Данные блока "Отправка"
                find_el(params, txt_order_in_calculation_and_ordering_page.xpath)
                check_text_attribute(params, input_dispatch_city.xpath, data_dispatch_city)
                check_text_attribute(params, btn_dispatch_terminal.xpath, "active")
                check_text_attribute(params, input_from_terminal_in_create_order_page.xpath,
                                     data_dispatch_address_terminal)
                check_text_attribute(params, choice_the_active_date_in_the_sending_feed_in_create_order_page.xpath,
                                     data_date_send_terminal)
                check_text_attribute(params, input_time_from_dispatch_terminal_in_create_order_page.xpath,
                                     data_time_send_terminal)

                # Данные блока "Прибытие"
                check_text_attribute(params, input_destination_city.xpath, data_destination_city)
                check_text_attribute(params, btn_destination_terminal.xpath, "active")
                check_text_attribute(params, input_to_terminal_in_create_order_page.xpath,
                                     data_destination_address_terminal)
                check_text_attribute(params, choice_the_active_date_in_the_arrival_feed_in_create_order_page.xpath,
                                     data_date_arrival_terminal)
                check_text_attribute(params, input_time_from_destination_in_create_order_page.xpath,
                                     data_time_arrival_terminal)

                # Данные блока "Груз" - Общие габариты
                check_text_attribute(params, input_value_volume_in_order_create_page.xpath, data_volume, False, True)
                check_text_attribute(params, input_value_weight_in_order_create_page.xpath, data_weight, False, True)
                check_text_attribute(params, input_value_places_in_order_create_page.xpath,
                                     f"{str(int(data_places) + 2)}")

                # Данные блока "Груз" - Максимальные габариты одного места
                # check_text_attribute(params, data_length_in_the_maximum_seat_dimensions_in_details_page.xpath, data_length_max_place)
                # check_text_attribute(params, data_width_in_the_maximum_seat_dimensions_in_details_page.xpath, data_width_max_place)
                # check_text_attribute(params, data_height_in_the_maximum_seat_dimensions_in_details_page.xpath, data_height_max_place)
                # check_text_attribute(params, data_weight_in_the_maximum_seat_dimensions_in_details_page.xpath, data_weight_max_place)

                # Данные блока "Груз" - Категория груза
                check_text_attribute(params, data_selected_cargo_category_in_create_order_page.xpath, data_category)

                # Данные блока "Груз" - Упаковка груза (достанем список упаковок и проверим, что они добавлены в детализацию заказа)
                list_of_packages_details = get_the_data_from_block_of_elements(params,
                                                                               data_cargo_package_in_the_cargo_block_in_create_order_page.xpath,
                                                                               1)
                exist_elements_of_list_in_list(list_of_packages_details, packages)

                # Данные блока "Груз" - Страхование груза
                check_text_attribute(params, inp_amount_field_in_the_insurance_in_create_order_form.xpath,
                                     data_insurance)

                # Данные блока "Доп.услуги"
                check_text_attribute(params,
                                     check_checkbox_scan_of_the_delivery_invoice_in_the_add_on_block_services_create_order_page.xpath,
                                     "checked")
                check_text_attribute(params,
                                     check_checkbox_return_the_accompanying_documents_in_the_add_on_block_services_create_order_page.xpath,
                                     "checked")
                # check_text_attribute(params, check_checkbox_disassembly_of_packaging_upon_delivery_to_the_address_on_block_services_create_order_page.xpath, "checked")

                # Данные блока "Плательщик"
                check_text_attribute(params, check_btn_recipient_in_the_payer_block_in_create_order_form.xpath,
                                     "active")

                # Данные блока "Участники"
                check_text_attribute(params, btn_type_ind_sender.xpath, "active")
                check_text_attribute(params, btn_type_ind_recipient.xpath, "active")
                check_text_attribute(params, input_fio_ind_sender.xpath, data_fio_ind_sender)
                check_text_attribute(params, input_phone_ind_sender.xpath, '+7 (999) 022-00-38')
                check_text_attribute(params, input_fio_ind_recipient.xpath, data_fio_ind_recipient)
                check_text_attribute(params, input_phone_ind_recipient.xpath, '+7 (981) 784-26-24')

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

        status_and_name_tst = create_order_based_on_order_terminal_terminal_ind_ind()
        # status_and_name_tst = create_order_based_on_order_address_pvz_comp_ind()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()
