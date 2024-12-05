import time
from Business_Actions import *
from Methods import *
from pages.contractors_page import *


def checking_the_addition_of_contacts_to_the_ka_card(params):
    main_description = "Тест №117 - Добавление/редактирование/удаление контактов к КА (ЮР.лицо)"
    status_and_name_tst = {}

    try:
        authorization_lk(params, url_base_org, individual_phone_full, passw)
        """1. Добавление контакта к КА (ЮР.лицо)"""
        def addition_of_contact_to_the_ka_card():
            description = "Добавление контактов к КА (ЮР.лицо)"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                find_el(params, btn_add_on_the_contractors_main_page.xpath)

                # Поиск необходимого КА
                find_el(params, f"//span[@title='{company_name2}']")
                click(params)

                find_el(params, btn_add_a_contact_on_the_card_contractor.xpath)
                click(params)

                # Заполнение карточки контакта
                find_el(params, inp_fio_on_the_popup_new_contact.xpath)
                send_keys(params, individual_fio)

                find_el(params, inp_phone_on_the_popup_new_contact.xpath)
                send_keys(params, individual_phone)

                find_el(params, inp_email_on_the_popup_new_contact.xpath)
                send_keys(params, individual_email)

                find_el(params, btn_add_a_contact_on_the_popup_card_contractor.xpath)
                click(params)

                # Развернем блок контактов
                find_el(params, btn_the_expand_contact_block_button_in_the_counterparty_card_contractor.xpath)
                click(params)

                # Проверка созданной карточки
                find_el(params, f"//span[text()='ФИО']/../span[text()='{individual_fio}']")
                find_el(params, f"//span[text()='Телефон']/../span[text()='7{individual_phone}']")
                find_el(params, f"//span[text()='Email']/../span[text()='{individual_email}']")

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

        """2. Добавление контактов другой страны к КА (ЮР.лицо)"""
        def addition_an_another_country_contact_to_the_ka_card():
            description = "Добавление контакта другой страны к КА (ЮР.лицо)"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                find_el(params, btn_add_on_the_contractors_main_page.xpath)

                # Поиск необходимого КА
                find_el(params, f"//span[@title='{company_name2}']")
                click(params)

                find_el(params, btn_add_a_contact_on_the_card_contractor.xpath)
                click(params)

                # Заполнение карточки контакта
                find_el(params, inp_fio_on_the_popup_new_contact.xpath)
                send_keys(params, add_test_name_ka)

                find_el(params, inp_phone_on_the_popup_new_contact.xpath)
                send_keys(params, add_individual_phone_kz, False)

                find_el(params, btn_add_a_contact_on_the_popup_card_contractor.xpath)
                click(params)

                # Развернем блок контактов
                find_el(params, btn_the_expand_contact_block_button_in_the_counterparty_card_contractor.xpath)
                click(params)

                # Проверка созданной карточки
                find_el(params, f"//span[text()='ФИО']/../span[text()='{add_test_name_ka}']")
                find_el(params, f"//span[text()='Телефон']/../span[text()='7{add_individual_phone_kz}']")

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

        """3. Редактирование контакта у КА (ЮР.лицо)"""
        def editing_a_contact_in_the_ka_card():
            description = "Редактирование контакта у КА (ЮР.лицо)"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                find_el(params, btn_add_on_the_contractors_main_page.xpath)

                # Поиск необходимого КА
                find_el(params, f"//span[@title='{company_name2}']")
                click(params)

                # Развернем блок контактов
                find_el(params, btn_the_expand_contact_block_button_in_the_counterparty_card_contractor.xpath)
                click(params)

                # Редактирование карточки контакта
                current_fio = get_the_text(params, text_fio_contact_on_the_card_contractor.xpath)
                current_phone = get_the_text(params, text_phone_contact_on_the_card_contractor.xpath)

                find_el(params, btn_editing_contact_on_the_card_contractor.xpath)
                click(params)

                # Ввод новых данных в карточку контакта
                find_el(params, inp_fio_on_the_popup_new_contact.xpath)
                send_keys(params, manager_name)

                find_el(params, inp_phone_on_the_popup_new_contact.xpath)
                send_keys(params, add_individual_phone_rf)

                find_el(params, inp_email_on_the_popup_new_contact.xpath)
                send_keys(params, company_email_number)

                # Проверим кнопку отмены редактирования
                find_el(params, btn_cancel_editing_contact_on_the_card_contractor.xpath)
                click(params)

                check_text_attribute(params, text_fio_contact_on_the_card_contractor.xpath, current_fio)
                check_text_attribute(params, text_phone_contact_on_the_card_contractor.xpath, current_phone)

                # Снова ввод новых данных в карточку контакта
                find_el(params, btn_editing_contact_on_the_card_contractor.xpath)
                click(params)

                find_el(params, inp_fio_on_the_popup_new_contact.xpath)
                send_keys(params, manager_name)

                find_el(params, inp_phone_on_the_popup_new_contact.xpath)
                send_keys(params, add_individual_phone_rf)

                find_el(params, inp_email_on_the_popup_new_contact.xpath)
                send_keys(params, company_email_number)

                find_el(params, btn_confirm_editing_contact_on_the_card_contractor.xpath)
                click(params)

                # Проверим корректную запись данных после подтверждения редактирования
                check_text_attribute(params, text_fio_contact_on_the_card_contractor.xpath, manager_name)
                check_text_attribute(params, text_phone_contact_on_the_card_contractor.xpath, add_individual_phone_rf)
                check_text_attribute(params, text_email_contact_on_the_card_contractor.xpath, company_email_number)

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

        """4. Удаление/не удаление контакта у КА (ЮР.лицо)"""
        def deleting_a_contact_in_the_ka_card():
            description = "Удаление/не удаление контакта у КА (ЮР.лицо)"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                find_el(params, btn_add_on_the_contractors_main_page.xpath)

                # Поиск необходимого КА
                find_el(params, f"//span[@title='{company_name2}']")
                click(params)

                # Развернем блок контактов и, заодно, запишем данные счетчика
                value_counter = get_the_text(params, text_the_contact_counter_in_the_contacts_with_counterparties_block.xpath)

                find_el(params, btn_the_expand_contact_block_button_in_the_counterparty_card_contractor.xpath)
                click(params)

                # Запишем данные контакта, чтобы в дальнейшем проверить его удаление/не удаление
                current_fio = get_the_text(params, text_fio_contact_on_the_card_contractor.xpath)
                current_phone = get_the_text(params, text_phone_contact_on_the_card_contractor.xpath)

                # Удаление карточки контакта (отмена удаления)
                find_el(params, btn_delete_contact_on_the_card_contractor.xpath)
                click(params)

                find_el(params, btn_cancel_delete_contact_on_the_popup_deleting_contact_on_card_contractor.xpath)
                click(params)

                """Проверка, что карточка не удалилась"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                find_el(params, btn_add_on_the_contractors_main_page.xpath)

                # Поиск необходимого КА
                find_el(params, f"//span[@title='{company_name2}']")
                click(params)

                # Развернем блок контактов
                find_el(params, btn_the_expand_contact_block_button_in_the_counterparty_card_contractor.xpath)
                click(params)

                # Проверим, что карточка не удалилась
                check_text_attribute(params, text_fio_contact_on_the_card_contractor.xpath, current_fio)
                check_text_attribute(params, text_phone_contact_on_the_card_contractor.xpath, current_phone)

                """Теперь удалим контакт"""
                find_el(params, btn_delete_contact_on_the_card_contractor.xpath)
                click(params)

                find_el(params, btn_delete_contact_on_the_popup_deleting_contact_on_card_contractor.xpath)
                click(params)

                # Проверим удаление контакта
                value_counter_1 = get_the_text(params, text_the_contact_counter_in_the_contacts_with_counterparties_block.xpath)

                if value_counter != value_counter_1:
                    pass
                else:
                    raise Exception

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

        """5. Негативные проверки при создании контакта у КА (ЮР.лицо)"""
        def negative_checks_for_creating_a_contact_in_the_ka_card():
            description = "Негативные проверки при создании контакта у КА (ЮР.лицо)"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                find_el(params, btn_add_on_the_contractors_main_page.xpath)

                # Поиск необходимого КА
                find_el(params, f"//span[@title='{company_name2}']")
                click(params)

                find_el(params, btn_add_a_contact_on_the_card_contractor.xpath)
                click(params)

                # Заполнение карточки контакта
                find_el(params, inp_fio_on_the_popup_new_contact.xpath)
                send_keys(params, individual_fio)

                find_el(params, inp_phone_on_the_popup_new_contact.xpath)
                send_keys(params, individual_fio, False)  # Заполним буквы вместо цифр
                send_keys(params, Keys.TAB, False)

                # Проверим, что появилась ошибка (некорректный номер телефона)
                find_el(params, text_error_incorrect_phone_format_on_the_popup_new_contractor.xpath)

                find_el(params, inp_email_on_the_popup_new_contact.xpath)
                click(params)
                send_keys(params, individual_fio)

                # Проверим, что появилась ошибка (некорректная почта)
                find_el(params, text_error_error_invalid_email_address_format_on_the_popup_new_contractor.xpath)

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

        status_and_name_tst = addition_of_contact_to_the_ka_card()
        status_and_name_tst = addition_an_another_country_contact_to_the_ka_card()
        status_and_name_tst = editing_a_contact_in_the_ka_card()
        status_and_name_tst = deleting_a_contact_in_the_ka_card()
        status_and_name_tst = negative_checks_for_creating_a_contact_in_the_ka_card()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()



