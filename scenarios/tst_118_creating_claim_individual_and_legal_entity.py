import time
from Business_Actions import *
from Methods import *
from pages.contractors_page import *
from pages.contacts_page import *
from pages.list_of_orders_page import *


def creating_claim_individual_and_legal_entity_in_the_ka_card(params):
    main_description = "Тест №118 - создание претензии у КА (ФИЗ. лицо и ЮР.лицо)"
    status_and_name_tst = {}

    try:
        authorization_lk(params, url_base_org, individual_phone_full, passw)
        """1. Создание претензии у КА (ФИЗ.лицо)"""
        def creating_claim_individual_ka_card():
            description = "Создание претензии у КА (ФИЗ.лицо)"

            try:
                # """Переходим на страницу заказов во вкладку Неоплаченные"""
                # find_el(params, tab_unpaid_in_the_list_of_orders_on_orders_page.xpath)
                # click(params)
                #
                # enable_element(params, skeleton_of_order_on_orders_page.xpath)

                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                # Ищем необходимого КА и переходим в него
                find_el(params, f"//span[@title='{individual_phone_full}']")
                click(params)

                find_el(params, btn_add_claim_on_the_contractors_main_page.xpath)
                click(params)

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

                # Проверим, создалась ли претензия
                # if check_text_attribute(params, text_notification_the_claim_has_been_registered.xpath, 'претензия зарегистрирована', True) is True:
                #     pass
                # else:
                #     click(params)

                check_text_attribute(params, text_notification_the_claim_has_been_registered.xpath, 'претензия зарегистрирована')
                a = get_the_text(params, text_notification_the_claim_has_been_registered.xpath)
                number_of_claim = extract_numbers(a)

                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                # Ищем необходимого КА и переходим в него
                find_el(params, f"//span[@title='{individual_phone_full}']")
                click(params)

                find_el(params, btn_show_collapse_counterparty_claims_on_card_contractor.xpath)
                click(params)
                enable_loader(params)

                # Сверяем данные созданной претензии (номер претензии и номер заказа в претензии)
                check_text_attribute(params, text_the_claim_number_in_the_created_claim.xpath, number_of_claim)
                check_text_attribute(params, text_the_order_number_in_the_created_claim.xpath, order_mini_calc)

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

        status_and_name_tst = creating_claim_individual_ka_card()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

