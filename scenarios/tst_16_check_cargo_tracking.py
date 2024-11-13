from Business_Actions import *
from Methods import *

def check_cargo_tracking(params):
    main_description = "Тест №16 - Проверка отслеживания груза"
    status_and_name_tst = {}

    try:
        """1. Проверка отслеживания груза (смоук тест)"""
        def cargo_tracking_check_smoke_test():
            description = "Проверка отслеживания груза (смоук тест)"

            try:
                # Страница отслеживания заказа
                set_page(params, url_order_manage_org)
                wait_page(params, url_order_manage_org)

                # Ищем поле "Введите номер заказа" и вводим номер заказа
                find_el(params, inp_number_of_order_manage_page.xpath)
                click(params)
                send_keys(params, order_mini_calc)

                check_text_attribute(params, inp_number_of_order_manage_page.xpath, order_mini_calc)

                # Нажимаем на кнопку "Отследить"
                find_el(params, btn_track_order_manage_page.xpath)
                click(params)

                # Найдем номер заказа в заголовке
                find_el(params, txt_number_order_manage_page.xpath)

                # Нажимаем на кнопку "Отследить"
                find_el(params, btn_track_order_manage_page.xpath)
                click(params)

                # Вводим в поле номер телефона из заказа
                find_el(params, inp_number_of_phone_from_order_manage_page.xpath)
                click(params)

                # Проверим заодно ввод некорректного номера не из заказа
                send_keys(params, incorrect_phone)
                find_el(params, btn_confirm_phone_manage_page.xpath)
                click(params)

                check_text_attribute(params, txt_error_input_confirm_phone_manage_page.xpath, 'Номер телефона не соответствует заказу')

                # Продолжим позитивный кейс
                find_el(params, inp_number_of_phone_from_order_manage_page.xpath)
                click(params)
                send_keys(params, individual_phone)
                find_el(params, btn_confirm_phone_manage_page.xpath)
                click(params)

                # Переходим в просмотр заказа и проверяем номер
                find_el(params, txt_number_order_in_detailing_manage_page.xpath)
                check_text_attribute(params, txt_number_order_in_detailing_manage_page.xpath, order_mini_calc)

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

        """2. Проверка отслеживания груза - пустое поле груза + некорректный номер груза (негативные тесты)"""
        def cargo_tracking_check_empty_cargo_field_incorrect_cargo_number_negative_tsts():
            try:
                description = "Проверка отслеживания груза - пустое поле груза (негативный тест)"

                # Страница отслеживания заказа
                set_page(params, url_order_manage_org)
                wait_page(params, url_order_manage_org)

                # Нажимаем на кнопку "Отследить" в хедере
                find_el(params, btn_track_button.xpath)
                click(params)

                # Ищем поле "Введите номер заказа" и ничего не вводя кликаем кнопку "Отследить"
                find_el(params, inp_number_of_order_manage_page.xpath)
                click(params)
                find_el(params, btn_track_order_manage_page.xpath)
                click(params)

                find_el(params, txt_error_input_number_order_manage_page.xpath)
                check_text_attribute(params, txt_error_input_number_order_manage_page.xpath, 'Поле обязательно для заполнения')

                description = "Проверка отслеживания груза - некорректный номер груза (негативный тест)"

                # Ищем поле "Введите номер заказа" и вводим некорректный номер заказа "абвabc" и "#$%%"
                find_el(params, inp_number_of_order_manage_page.xpath)
                click(params)
                send_keys(params, invalid_number_order_3)
                send_keys(params, invalid_number_order_4)
                find_el(params, btn_track_order_manage_page.xpath)
                click(params)

                # Появляется ошибка валидации, проверяем ее содержимое
                find_el(params, txt_error_input_number_order_manage_page.xpath)
                check_text_attribute(params, txt_error_input_number_order_manage_page.xpath, 'Поле обязательно для заполнения')

                # Ищем поле "Введите номер заказа" и вводим некорректный номер заказа "123"
                find_el(params, inp_number_of_order_manage_page.xpath)
                click(params)
                send_keys(params, invalid_number_order_1)
                find_el(params, btn_track_order_manage_page.xpath)
                click(params)

                # Появляется ошибка валидации, проверяем ее содержимое
                find_el(params, txt_error_input_number_order_manage_page.xpath)
                check_text_attribute(params, txt_error_input_number_order_manage_page.xpath, 'Длина должна быть 9 символов')

                # Ищем поле "Введите номер заказа" и вводим несуществующий номер заказа "888888888"
                find_el(params, inp_number_of_order_manage_page.xpath)
                click(params)
                send_keys(params, invalid_number_order_2)
                find_el(params, btn_track_order_manage_page.xpath)
                click(params, True)  # передадим аргумент "skip_check", чтобы ошибка, которая вылетает не вызывала исключение

                # Проверим появление ошибки "проверьте номер заказа"
                find_el(params, error_toast_main_page.xpath)

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

        status_and_name_tst = cargo_tracking_check_smoke_test()
        status_and_name_tst = cargo_tracking_check_empty_cargo_field_incorrect_cargo_number_negative_tsts()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()
