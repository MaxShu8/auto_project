import time
from Business_Actions import *
from Methods import *
from pages.order_create_page import *
from pages.list_of_orders_page import *
from pages.order_details import *
from pages.add_to_template_popup import *
from pages.template_page import *

def tst_102_checking_order_addition_to_the_template(params):
    main_description = "Тест №102 - проверка добавления заказа в шаблон"
    status_and_name_tst = {}

    try:
        authorization_lk(params, url_base_org, individual_phone_full, passw)
        """1. Проверка добавления заказа в шаблон"""
        def checking_order_addition_to_the_template_phys_ka():
            description = "Проверка данных в шаблоне добавленного заказа Т-->Т, физ.лицо - физ.лицо"
            packages = ["Мешок 55×105", "Коробка 40×20×20", "Прозрачная плёнка", "Паллетный борт", "Упаковка в сейф-пакет"]

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
                check_text_attribute(params, btn_dispatch_terminal.xpath, "active")  # Проверим, включена ли кнопка Терминал

                """Заполняем блок Направление - Прибытие"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[2])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)
                check_text_attribute(params, btn_destination_terminal.xpath, "active")  # Проверим, включена ли кнопка Терминал

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
                find_el(params, input_value_places.xpath)
                send_keys(params, "8")
                price_to_load(params)

                find_el(params, input_value_weight.xpath)
                click(params)  # клик нужен, чтобы убрать фокус с предыдущего поля
                send_keys(params, "123")
                price_to_load(params)

                find_el(params, input_value_volume.xpath)
                click(params)  # клик нужен, чтобы убрать фокус с предыдущего поля
                send_keys(params, "1", False)
                price_to_load(params)

                # Заполняем "Максимальные габариты одного места"
                find_el(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                send_keys(params, "1.15")
                find_el(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                send_keys(params, "0.75")
                find_el(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                send_keys(params, "1.16")
                find_el(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                send_keys(params, "11")

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
                data_length_max_place = get_the_data_from_element(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_width_max_place = get_the_data_from_element(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_height_max_place = get_the_data_from_element(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_weight_max_place = get_the_data_from_element(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_category = get_the_data_from_element(params, choice_sort_subcategory_toys_in_calculation_and_ordering_page.xpath)
                data_insurance = get_the_data_from_element(params, inp_amount_field_in_the_insurance_in_create_order_form.xpath, 1)
                data_your_transportation_number = get_the_data_from_element(params, inp_field_is_your_transportation_number_in_create_order_form.xpath, 1)

                """Заполняем блок Доп.услуги"""
                find_el(params, checkbox_scan_of_the_delivery_invoice_in_the_add_on_block_services_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_return_the_accompanying_documents_in_the_add_on_block_services_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_disassembly_of_packaging_upon_delivery_to_the_address_on_block_services_create_order_page.xpath)
                click(params)
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
                set_counteragent_data(params, "sender", "individual", individual_fio, individual_phone)
                set_counteragent_data(params, "recipient", "individual", individual_fio_2, individual_phone_2)

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

                """Сверим данные в детализации заказа"""
                check_text_attribute(params, data_individual_number_of_order_in_details_page.xpath, data_your_transportation_number)

                # Данные блока "Отправка"
                check_text_attribute(params, data_dispatch_us_point_terminal_address_in_details_page.xpath, data_dispatch_city)
                check_text_attribute(params, data_dispatch_us_point_terminal_address_in_details_page.xpath, data_dispatch_terminal)
                check_text_attribute(params, data_dispatch_us_point_terminal_address_in_details_page.xpath, data_dispatch_address_terminal)
                check_text_attribute(params, data_dispatch_date_of_order_in_details_page.xpath, data_date_send_terminal)
                check_text_attribute(params, data_dispatch_time_of_delivery_in_details_page.xpath, data_time_send_terminal)

                # Данные блока "Прибытие"
                check_text_attribute(params, data_destination_us_point_terminal_address_in_details_page.xpath, data_destination_city)
                check_text_attribute(params, data_destination_us_point_terminal_address_in_details_page.xpath, data_destination_terminal)
                check_text_attribute(params, data_destination_us_point_terminal_address_in_details_page.xpath, data_destination_address_terminal)
                check_text_attribute(params, data_destination_date_of_order_in_details_page.xpath, data_date_arrival_terminal)
                check_text_attribute(params, data_destination_time_of_delivery_in_details_page.xpath, data_time_arrival_terminal)

                # Данные блока "Груз" - Общие габариты
                check_text_attribute(params, data_volume_in_the_total_dimensions_of_the_cargo_in_details_page.xpath, data_volume, False, True, "text")
                check_text_attribute(params, data_weight_in_the_total_dimensions_of_the_cargo_in_details_page.xpath, data_weight, False, True, "text")
                check_text_attribute(params, data_places_in_the_total_dimensions_of_the_cargo_in_details_page.xpath, f"{str(int(data_places) + 2)}", "text")

                # Данные блока "Груз" - Максимальные габариты одного места
                check_text_attribute(params, data_length_in_the_maximum_seat_dimensions_in_details_page.xpath, data_length_max_place, False, True, "text")
                check_text_attribute(params, data_width_in_the_maximum_seat_dimensions_in_details_page.xpath, data_width_max_place, False, True, "text")
                check_text_attribute(params, data_height_in_the_maximum_seat_dimensions_in_details_page.xpath, data_height_max_place, False, True, "text")
                check_text_attribute(params, data_weight_in_the_maximum_seat_dimensions_in_details_page.xpath, data_weight_max_place, False, True, "text")

                # Данные блока "Груз" - Категория груза
                check_text_attribute(params, data_cargo_category_of_the_cargo_block_in_details_page.xpath, data_category)

                # Данные блока "Груз" - Упаковка груза (достанем список упаковок и проверим, что они добавлены в детализацию заказа)
                list_of_packages_details = get_the_data_from_block_of_elements(params, data_cargo_package_in_the_cargo_block_in_details_page.xpath)
                exist_elements_of_list_in_list(list_of_packages_details, packages)

                # Данные блока "Груз" - Страхование груза
                check_text_attribute(params, data_cargo_insurance_in_the_cargo_block_in_details_page.xpath, data_insurance)

                # Данные блока "Доп.услуги"
                check_text_attribute(params, data_scan_of_the_delivery_invoice_in_details_page.xpath, data_scan_of_the_delivery_invoice)
                check_text_attribute(params, data_accompanying_documents_in_details_page.xpath, data_return_the_accompanying_documents)
                # check_text_attribute(params, data_accompanying_documents_in_details_page.xpath, data_return_the_accompanying_documents)

                # Данные блока "Участники"
                check_text_attribute(params, data_fio_sender_in_details_page.xpath, data_fio_ind_sender)
                check_text_attribute(params, data_phone_sender_in_details_page.xpath, data_phone_ind_sender)
                check_text_attribute(params, data_fio_recipient_in_details_page.xpath, data_fio_ind_recipient)
                check_text_attribute(params, data_phone_recipient_in_details_page.xpath, data_phone_ind_recipient)
                check_text_attribute(params, data_signature_of_the_payer_at_the_sender_in_details_page.xpath, data_recipient)

                # Добавляем данный заказ в шаблон
                find_el(params, btn_add_to_template_on_in_details_page.xpath)
                click(params)

                find_el(params, txt_add_to_template_on_the_add_to_template_popup.xpath)
                find_el(params, inp_enter_the_name_in_template_popup.xpath)
                send_keys(params, individual_fio)

                find_el(params, btn_select_all_in_template_popup.xpath)
                click(params)
                find_el(params, btn_add_and_go_to_template_in_template_popup.xpath)
                click(params)

                """Проверяем переданные данные в шаблон"""
                # БЛОК НАПРАВЛЕНИЕ (Отправка/Прибытие)
                # Для установки города, чтобы не валился тест
                choice_us_item_from_drop_down_list_in_dispatch_in_template_page_xxx.change_xpath(cities[0])
                find_el(params, choice_us_item_from_drop_down_list_in_dispatch_in_template_page_xxx.xpath)

                choice_us_item_from_drop_down_list_in_dispatch_in_template_page_xxx.reset_xpath()
                ###

                check_text_attribute(params, input_dispatch_city_in_create_order_page.xpath, data_dispatch_city)
                check_text_attribute(params, input_from_terminal_in_create_order_page.xpath, data_dispatch_address_terminal)
                check_text_attribute(params, btn_dispatch_terminal.xpath, "active")

                check_text_attribute(params, input_destination_city_in_create_order_page.xpath, data_destination_city)
                check_text_attribute(params, input_to_terminal_in_create_order_page.xpath, data_destination_address_terminal)
                check_text_attribute(params, btn_destination_terminal.xpath, "active")

                # БЛОК ГРУЗ
                check_text_attribute(params, input_value_volume_in_order_create_page.xpath,
                                     data_volume, False, True, "value")
                check_text_attribute(params, input_value_weight_in_order_create_page.xpath,
                                     data_weight, False, True, "value")
                check_text_attribute(params, input_value_places_in_order_create_page.xpath,
                                     f"{str(int(data_places) + 2)}", "value")

                # Данные блока "Груз" - Максимальные габариты одного места
                check_text_attribute(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath,
                                     data_length_max_place, False, True, "value")
                check_text_attribute(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath,
                                     data_width_max_place, False, True, "value")
                check_text_attribute(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath,
                                     data_height_max_place, False, True, "value")
                check_text_attribute(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath,
                                     data_weight_max_place, False, True, "value")

                check_text_attribute(params, data_selected_cargo_category_in_create_order_page.xpath, "Игрушки")

                # Упаковка
                packages_in_templates = get_the_data_from_block_of_elements(params, data_packing_information_template_page.xpath, 1)
                exist_elements_of_list_in_list(packages_in_templates, packages)

                # Страхование
                check_text_attribute(params, btn_insurance_field_in_the_create_order_form.xpath, "Страхование груза")
                check_text_attribute(params, inp_amount_field_in_the_insurance_in_create_order_form.xpath, value_insurance)

                # Ваш номер перевозки
                check_text_attribute(params, inp_field_is_your_transportation_number_in_template_page.xpath, individual_order_with_text)

                # БЛОК ПЛАТЕЛЬЩИК
                check_text_attribute(params, btn_recipient_in_the_payer_block_in_create_order_form.xpath, "Получатель")

                # БЛОК УЧАСТНИКИ (Отправитель/Получатель)
                check_text_attribute(params, btn_type_ind_sender.xpath, "active")
                check_text_attribute(params, input_fio_ind_sender.xpath, individual_fio)
                check_text_attribute(params, input_phone_ind_sender.xpath, individual_phone_with_symbols)

                check_text_attribute(params, btn_type_ind_recipient.xpath, "active")
                check_text_attribute(params, input_fio_ind_recipient.xpath, individual_fio_2)
                check_text_attribute(params, input_phone_ind_recipient.xpath, individual_phone_with_symbols_2)

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

        def checking_order_addition_to_the_template_company_ka():
            description = "Проверка данных в шаблоне добавленного заказа А-->П, юр.лицо - юр.лицо"
            packages = ["Мешок 55×105", "Коробка 40×20×20", "Прозрачная плёнка", "Защитная жесткая упаковка", "Упаковка в сейф-пакет"]

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

                find_el(params, btn_dispatch_address.xpath)
                click(params)
                price_to_load(params)

                find_el(params, input_dispatch_address.xpath)
                click(params)
                send_keys(params, addresses[0])
                price_to_load(params)

                check_text_attribute(params, btn_dispatch_address.xpath, "active")  # Проверим, включена ли кнопка Адрес

                """Заполняем блок Направление - Прибытие"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[2])

                find_el(params, btn_destination_pvz.xpath)
                click(params)
                price_to_load(params)
                check_text_attribute(params, btn_destination_pvz.xpath, "active")  # Проверим, включена ли кнопка ПВЗ
                find_el(params, input_destination_pvz_in_create_order_page.xpath)
                send_keys(params, "Сиреневый бульвар 4 к3")

                # Выберем пункт ПВЗ из выпадающего списка
                choice_pvz_point_in_destination_in_create_order_page.change_xpath("Сиреневый бульвар 4 к3")
                find_el(params, choice_pvz_point_in_destination_in_create_order_page.xpath)
                click(params)

                choice_pvz_point_in_destination_in_create_order_page.reset_xpath()

                # Вытащим данные из Отправки
                data_dispatch_city = get_the_data_from_element(params, input_dispatch_city.xpath, 1)
                data_dispatch_type = get_the_data_from_element(params, btn_dispatch_address.xpath)
                data_dispatch_address = get_the_data_from_element(params, input_dispatch_address_in_create_order_page.xpath, 1)
                data_date_send_address = get_the_data_from_element(params, btn_active_date_in_the_send_in_the_calendar.xpath)
                data_date_send_address = extract_numbers(data_date_send_address)
                data_time_send_terminal = get_the_data_from_element(params, input_time_from_dispatch_terminal_in_create_order_page.xpath)

                # Вытащим данные из Прибытия
                data_destination_city = get_the_data_from_element(params, input_destination_city.xpath, 1)
                data_destination_type = get_the_data_from_element(params, btn_destination_address.xpath)
                data_destination_address_pvz = get_the_data_from_element(params, input_destination_pvz_in_create_order_page.xpath, 1)
                data_date_arrival_terminal = get_the_data_from_element(params, btn_active_date_in_the_arrival_in_the_calendar.xpath)
                data_date_arrival_terminal = extract_numbers(data_date_arrival_terminal)
                data_time_arrival_terminal = get_the_data_from_element(params, input_time_from_destination_in_create_order_page.xpath)

                """Заполняем блок Груз - вкладка (Габариты)"""
                # Заполняем "Общие габариты"
                find_el(params, input_value_places.xpath)
                send_keys(params, "8")
                price_to_load(params)

                find_el(params, input_value_weight.xpath)
                click(params)  # клик нужен, чтобы убрать фокус с предыдущего поля
                send_keys(params, "123")
                price_to_load(params)

                find_el(params, input_value_volume.xpath)
                click(params)  # клик нужен, чтобы убрать фокус с предыдущего поля
                send_keys(params, "1", False)
                price_to_load(params)

                # Заполняем "Максимальные габариты одного места"
                find_el(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                send_keys(params, "1.15")
                find_el(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                send_keys(params, "0.75")
                find_el(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                send_keys(params, "1.16")
                find_el(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath)
                send_keys(params, "11")

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
                data_length_max_place = get_the_data_from_element(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_width_max_place = get_the_data_from_element(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_height_max_place = get_the_data_from_element(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_weight_max_place = get_the_data_from_element(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath, 1)
                data_category = get_the_data_from_element(params, choice_sort_subcategory_toys_in_calculation_and_ordering_page.xpath)
                data_insurance = get_the_data_from_element(params, inp_amount_field_in_the_insurance_in_create_order_form.xpath, 1)
                data_your_transportation_number = get_the_data_from_element(params, inp_field_is_your_transportation_number_in_create_order_form.xpath, 1)

                """Заполняем блок Доп.услуги"""
                find_el(params, checkbox_scan_of_the_delivery_invoice_in_the_add_on_block_services_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_return_the_accompanying_documents_in_the_add_on_block_services_create_order_page.xpath)
                click(params)
                find_el(params, checkbox_disassembly_of_packaging_upon_delivery_to_the_address_on_block_services_create_order_page.xpath)
                click(params)
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
                set_counteragent_data(params, "sender", "individual", individual_fio, individual_phone)
                set_counteragent_data(params, "recipient", "individual", individual_fio_2, individual_phone_2)

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

                """Сверим данные в детализации заказа"""
                check_text_attribute(params, data_individual_number_of_order_in_details_page.xpath, data_your_transportation_number)

                # Данные блока "Отправка"
                check_text_attribute(params, data_dispatch_us_point_terminal_address_in_details_page.xpath, data_dispatch_city)
                check_text_attribute(params, data_dispatch_us_point_terminal_address_in_details_page.xpath, data_dispatch_type)
                check_text_attribute(params, data_dispatch_us_point_terminal_address_in_details_page.xpath, data_dispatch_address)
                check_text_attribute(params, data_dispatch_date_of_order_in_details_page.xpath, data_date_send_address)
                check_text_attribute(params, data_dispatch_time_of_delivery_in_details_page.xpath, data_time_send_terminal)

                # Данные блока "Прибытие"
                check_text_attribute(params, data_destination_us_point_terminal_address_in_details_page.xpath, data_destination_city)
                check_text_attribute(params, data_destination_us_point_terminal_address_in_details_page.xpath, data_destination_type)
                check_text_attribute(params, data_destination_us_point_terminal_address_in_details_page.xpath, data_destination_address_pvz)
                check_text_attribute(params, data_destination_date_of_order_in_details_page.xpath, data_date_arrival_terminal)
                check_text_attribute(params, data_destination_time_of_delivery_in_details_page.xpath, data_time_arrival_terminal)

                # Данные блока "Груз" - Общие габариты
                check_text_attribute(params, data_volume_in_the_total_dimensions_of_the_cargo_in_details_page.xpath, data_volume, False, True, "text")
                check_text_attribute(params, data_weight_in_the_total_dimensions_of_the_cargo_in_details_page.xpath, data_weight, False, True, "text")
                check_text_attribute(params, data_places_in_the_total_dimensions_of_the_cargo_in_details_page.xpath, f"{str(int(data_places) + 2)}", "text")

                # Данные блока "Груз" - Максимальные габариты одного места
                check_text_attribute(params, data_length_in_the_maximum_seat_dimensions_in_details_page.xpath, data_length_max_place, False, True, "text")
                check_text_attribute(params, data_width_in_the_maximum_seat_dimensions_in_details_page.xpath, data_width_max_place, False, True, "text")
                check_text_attribute(params, data_height_in_the_maximum_seat_dimensions_in_details_page.xpath, data_height_max_place, False, True, "text")
                check_text_attribute(params, data_weight_in_the_maximum_seat_dimensions_in_details_page.xpath, data_weight_max_place, False, True, "text")

                # Данные блока "Груз" - Категория груза
                check_text_attribute(params, data_cargo_category_of_the_cargo_block_in_details_page.xpath, data_category)

                # Данные блока "Груз" - Упаковка груза (достанем список упаковок и проверим, что они добавлены в детализацию заказа)
                list_of_packages_details = get_the_data_from_block_of_elements(params, data_cargo_package_in_the_cargo_block_in_details_page.xpath)
                exist_elements_of_list_in_list(list_of_packages_details, packages)

                # Данные блока "Груз" - Страхование груза
                check_text_attribute(params, data_cargo_insurance_in_the_cargo_block_in_details_page.xpath, data_insurance)

                # Данные блока "Доп.услуги"
                check_text_attribute(params, data_scan_of_the_delivery_invoice_in_details_page.xpath, data_scan_of_the_delivery_invoice)
                check_text_attribute(params, data_accompanying_documents_in_details_page.xpath, data_return_the_accompanying_documents)
                # check_text_attribute(params, data_accompanying_documents_in_details_page.xpath, data_return_the_accompanying_documents)

                # Данные блока "Участники"
                check_text_attribute(params, data_fio_sender_in_details_page.xpath, data_fio_ind_sender)
                check_text_attribute(params, data_phone_sender_in_details_page.xpath, data_phone_ind_sender)
                check_text_attribute(params, data_fio_recipient_in_details_page.xpath, data_fio_ind_recipient)
                check_text_attribute(params, data_phone_recipient_in_details_page.xpath, data_phone_ind_recipient)
                check_text_attribute(params, data_signature_of_the_payer_at_the_sender_in_details_page.xpath, data_recipient)

                # Добавляем данный заказ в шаблон
                find_el(params, btn_add_to_template_on_in_details_page.xpath)
                click(params)

                find_el(params, txt_add_to_template_on_the_add_to_template_popup.xpath)
                find_el(params, inp_enter_the_name_in_template_popup.xpath)
                send_keys(params, individual_fio)

                find_el(params, btn_select_all_in_template_popup.xpath)
                click(params)
                find_el(params, btn_add_and_go_to_template_in_template_popup.xpath)
                click(params)

                """Проверяем переданные данные в шаблон"""
                # БЛОК НАПРАВЛЕНИЕ (Отправка/Прибытие)
                check_text_attribute(params, input_dispatch_city_in_create_order_page.xpath, data_dispatch_city)
                check_text_attribute(params, input_from_terminal_in_create_order_page.xpath, data_dispatch_address)
                check_text_attribute(params, btn_dispatch_terminal.xpath, "active")

                check_text_attribute(params, input_destination_city_in_create_order_page.xpath, data_destination_city)
                check_text_attribute(params, input_to_terminal_in_create_order_page.xpath, data_destination_address_pvz)
                check_text_attribute(params, btn_destination_terminal.xpath, "active")

                # БЛОК ГРУЗ
                check_text_attribute(params, input_value_volume_in_order_create_page.xpath,
                                     data_volume, False, True, "value")
                check_text_attribute(params, input_value_weight_in_order_create_page.xpath,
                                     data_weight, False, True, "value")
                check_text_attribute(params, input_value_places_in_order_create_page.xpath,
                                     f"{str(int(data_places) + 2)}", "value")

                # Данные блока "Груз" - Максимальные габариты одного места
                check_text_attribute(params, inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath,
                                     data_length_max_place, False, True, "value")
                check_text_attribute(params, inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath,
                                     data_width_max_place, False, True, "value")
                check_text_attribute(params, inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath,
                                     data_height_max_place, False, True, "value")
                check_text_attribute(params, inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page.xpath,
                                     data_weight_max_place, False, True, "value")

                check_text_attribute(params, data_selected_cargo_category_in_create_order_page.xpath, "Игрушки")

                # Упаковка
                packages_in_templates = get_the_data_from_block_of_elements(params, data_packing_information_template_page.xpath, 1)
                exist_elements_of_list_in_list(packages_in_templates, packages)

                # Страхование
                check_text_attribute(params, btn_insurance_field_in_the_create_order_form.xpath, "Страхование груза")
                check_text_attribute(params, inp_amount_field_in_the_insurance_in_create_order_form.xpath, value_insurance)

                # Ваш номер перевозки
                check_text_attribute(params, inp_field_is_your_transportation_number_in_template_page.xpath, individual_order_with_text)

                # БЛОК ПЛАТЕЛЬЩИК
                check_text_attribute(params, btn_recipient_in_the_payer_block_in_create_order_form.xpath, "Получатель")

                # БЛОК УЧАСТНИКИ (Отправитель/Получатель)
                check_text_attribute(params, btn_type_ind_sender.xpath, "active")
                check_text_attribute(params, input_fio_ind_sender.xpath, individual_fio)
                check_text_attribute(params, input_phone_ind_sender.xpath, individual_phone_with_symbols)

                check_text_attribute(params, btn_type_ind_recipient.xpath, "active")
                check_text_attribute(params, input_fio_ind_recipient.xpath, individual_fio_2)
                check_text_attribute(params, input_phone_ind_recipient.xpath, individual_phone_with_symbols_2)

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

        status_and_name_tst = checking_order_addition_to_the_template_phys_ka()
        # status_and_name_tst = checking_order_addition_to_the_template_company_ka()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

