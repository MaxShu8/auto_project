import time

from Business_Actions import *
from Methods import *
from pages.contacts_page import *
from pages.list_of_orders_page import *
from pages.contractors_page import *

def sending_feedback_forms(params):
    main_description = "Тест №22 - Отправка форм обратной связи, претензии, оригиналов док-ов"
    status_and_name_tst = {}

    try:
        """1. Проверка отправки дефолтной формы обратной связи"""
        def send_feedback_form_default():
            description = "Проверка отправки дефолтной формы обратной связи"

            try:
                """Переходим на страницу контактов"""
                set_page(params, url_contacts_org)
                wait_page(params, url_contacts_org)

                """Кликаем на 'Я ваш клиент - есть вопрос'"""
                find_el(params, btn_i_am_your_client_documents_page.xpath)
                click(params)

                find_el(params, txt_popup_i_am_your_client_popup_feedback.xpath)

                """Заполняем форму обратной связи"""
                # Заполняем 'Номер заказа'
                find_el(params, input_number_of_order_popup_feedback.xpath)
                click(params)
                send_keys(params, order_mini_calc)

                # Заполняем 'Ваше имя'
                find_el(params, input_your_name_popup_feedback.xpath)
                click(params)
                send_keys(params, individual_fio)

                # Заполняем 'Ваш телефон'
                find_el(params, input_your_phone_number_popup_feedback.xpath)
                click(params)
                send_keys(params, individual_phone)

                # Заполняем 'Сообщение'
                find_el(params, input_message_popup_feedback.xpath)
                click(params)
                send_keys(params, test_message)

                """Клик на кнопку 'Отправить' на форме обратной связи"""
                find_el(params, btn_send_feedback_form_popup_feedback.xpath)
                click(params)

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

        """2. Проверка отправки претензии"""
        def send_feedback_form_claim():
            description = "Проверка отправки претензии"

            try:
                """Переходим на страницу контактов"""
                set_page(params, url_contacts_org)
                wait_page(params, url_contacts_org)

                """Кликаем на 'Я ваш клиент - есть вопрос'"""
                find_el(params, btn_i_am_your_client_documents_page.xpath)
                click(params)
                find_el(params, txt_popup_i_am_your_client_popup_feedback.xpath)

                """Выбираем тип обращения - Претензия"""
                find_el(params, field_type_of_appeal_popup_feedback.xpath)
                click(params)

                find_el(params, choice_claim_in_type_appeal_field_popup_feedback.xpath)
                click(params)

                find_el(params, text_popup_claim_in_popup_feedback.xpath)

                """Заполняем форму претензии"""
                # Заполняем 'Номер заказа'
                find_el(params, input_number_of_order_popup_feedback.xpath)
                click(params)
                send_keys(params, order_mini_calc)

                # Заполняем 'E-mail'
                find_el(params, input_email_popup_feedback.xpath)
                click(params)
                send_keys(params, individual_email)

                # Заполняем 'БИК'
                find_el(params, input_bik_number_popup_feedback.xpath)
                click(params)
                send_keys(params, individual_bik)

                # Заполняем 'Расчетный счет'
                find_el(params, input_payment_account_number_popup_feedback.xpath)
                click(params)
                send_keys(params, individual_payment_account)

                # Заполняем 'Суть претензии'
                find_el(params, input_the_essence_of_the_claim_popup_feedback.xpath)
                click(params)
                send_keys(params, test_message)

                upload_file(params, btn_upload_file_popup_feedback.xpath)

                """Клик на кнопку 'Cоздать претензию' на форме обратной связи"""
                find_el(params, btn_send_claim_popup_feedback.xpath)
                click(params)

                time.sleep(1)  # Нужно для появления элемента с ошибкой на странице, чтобы далее скачать страницу

                page_content = params.page_source
                something_went_wrong = "bottom error"

                if something_went_wrong in page_content:
                    check_text_attribute(params, text_notification_the_claim_has_been_registered.xpath, 'уже есть незакрытая претензия')
                else:
                    check_text_attribute(params, text_notification_the_claim_has_been_registered.xpath, 'претензия зарегистрирована')

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

        """3. Проверка отправки оригиналов документов - вкладка по грузу"""
        def request_for_original_documents_on_the_cargo():
            description = "Проверка отправки оригиналов документов"

            try:
                """Переходим на страницу контактов"""
                set_page(params, url_contacts_org)
                wait_page(params, url_contacts_org)

                """Кликаем на 'Я ваш клиент - есть вопрос'"""
                find_el(params, btn_i_am_your_client_documents_page.xpath)
                click(params)
                find_el(params, txt_popup_i_am_your_client_popup_feedback.xpath)

                """Выбираем тип обращения - запрос оригиналов документов"""
                find_el(params, field_type_of_appeal_popup_feedback.xpath)
                click(params)

                find_el(params, choice_original_documents_in_type_appeal_field_popup_feedback.xpath)
                click(params)

                find_el(params, text_popup_original_documents_in_popup_feedback.xpath)

                """Заполняем форму запроса оригиналов документов - вкладка по грузу"""
                # Выбираем вкладку 'По грузу'
                find_el(params, tab_by_cargo_original_documents_popup_feedback.xpath)
                click(params)

                # Заполняем 'Номер заказа'
                find_el(params, input_number_of_order_popup_feedback.xpath)
                click(params)
                send_keys(params, company_order_number)

                # Заполняем 'Номер телефона из заказа'
                find_el(params, input_phone_number_from_the_order_popup_feedback.xpath)
                click(params)
                send_keys(params, company_phone_number)

                # Заполняем 'E-mail'
                find_el(params, input_email_popup_feedback.xpath)  # сначала введем не ту почту, чтобы проверить, что данные не улетят к третьим лицам
                click(params, True)
                send_keys(params, individual_email)

                """Клик на кнопку 'Запросить' в попапе 'Запрос оригиналов документов'"""
                find_el(params, btn_request_original_documents_popup_feedback.xpath)
                click(params, True)  # пропустим отлов ошибки в данном методе

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params)

                # Закрываем ошибку
                find_el(params, btn_close_error_popup_feedback.xpath)
                click(params)

                # Заполняем 'E-mail'
                find_el(params, input_email_popup_feedback.xpath)  # заполним корректную почту
                click(params)
                send_keys(params, company_email_number)

                """Клик на кнопку 'Запросить' в попапе 'Запрос оригиналов документов'"""
                find_el(params, btn_request_original_documents_popup_feedback.xpath)
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params)

                # Ищем уведомление о том, что запрос отправлен
                find_el(params, popup_request_sending_success_popup_feedback.xpath)

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

        """4. Проверка отправки оригиналов документов - вкладка акт сверки"""
        def request_for_original_documents_reconciliation_report():
            description = "Проверка отправки актов сверки"

            try:
                """Переходим на страницу контактов"""
                set_page(params, url_contacts_org)
                wait_page(params, url_contacts_org)

                """Кликаем на 'Я ваш клиент - есть вопрос'"""
                find_el(params, btn_i_am_your_client_documents_page.xpath)
                click(params)
                find_el(params, txt_popup_i_am_your_client_popup_feedback.xpath)

                """Выбираем тип обращения - запрос оригиналов документов"""
                find_el(params, field_type_of_appeal_popup_feedback.xpath)
                click(params)

                find_el(params, choice_original_documents_in_type_appeal_field_popup_feedback.xpath)
                click(params)

                find_el(params, text_popup_original_documents_in_popup_feedback.xpath)

                """Заполняем форму запроса оригиналов документов - вкладка акт сверки"""
                # Выбираем вкладку 'Акт сверки'
                find_el(params, tab_reconciliation_report_original_documents_popup_feedback.xpath)
                click(params)

                # Заполняем 'ИНН компании'
                find_el(params, input_inn_company_popup_feedback.xpath)
                click(params)
                send_keys(params, company_inn_number)

                # Выбираем компанию из списка
                find_el(params, choice_first_company_in_list_popup_feedback.xpath)
                click(params)

                # Заполняем 'E-mail'
                find_el(params, input_email_popup_feedback.xpath)  # сначала введем не ту почту, чтобы проверить, что данные не улетят к третьим лицам
                click(params)
                send_keys(params, individual_email)

                """Клик на кнопку 'Запросить' в попапе 'Запрос оригиналов документов'"""
                find_el(params, btn_request_original_documents_popup_feedback.xpath)
                click(params, True)  # пропустим отлов ошибки в данном методе

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params)

                # Закрываем ошибку
                find_el(params, btn_close_error_popup_feedback.xpath)
                click(params)

                # Заполняем 'E-mail'
                find_el(params, input_email_popup_feedback.xpath)  # заполним корректную почту
                click(params)
                send_keys(params, company_email_number)

                """Клик на кнопку 'Запросить' в попапе 'Запрос оригиналов документов'"""
                find_el(params, btn_request_original_documents_popup_feedback.xpath)
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params)

                # Ищем уведомление о том, что запрос отправлен
                find_el(params, popup_request_sending_success_popup_feedback.xpath)

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

        status_and_name_tst = send_feedback_form_default()
        status_and_name_tst = send_feedback_form_claim()
        status_and_name_tst = request_for_original_documents_on_the_cargo()
        status_and_name_tst = request_for_original_documents_reconciliation_report()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

