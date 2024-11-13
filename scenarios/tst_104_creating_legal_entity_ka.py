import time
from Business_Actions import *
from Methods import *
from pages.contractors_page import *


def check_creating_legal_entity_ka(params):
    main_description = "Тест №104 - Создание КА — ЮР.лицо"
    status_and_name_tst = {}

    try:
        authorization_lk(params, url_base_org)

        """1. Создание Контрагента (Юридическое лицо) Россия"""
        def creating_a_legal_entity_ka_ru():
            description = "Создание Контрагента (Юридическое лицо) Россия"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                """Кликаем на кнопку '+ Добавить'"""
                find_el(params, btn_add_on_the_contractors_main_page.xpath)
                click(params)

                """Заполняем форму 'Новый контрагент'"""
                # Кликаем на "Юридическое лицо" и заполняем форму и нажимаем 'Далее'
                find_el(params, btn_tab_legal_entities_ka_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, inp_inn_on_the_popup_new_contractor.xpath)
                send_keys(params, company_inn_number)

                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Проверим, что загрузились нужные данные
                check_text_attribute(params, inp_inn_on_the_popup_new_contractor.xpath, company_inn_number)

                find_el(params, inp_name_company_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, choice_name_company_in_the_input_on_popup_new_contractor.xpath)
                click(params)

                # Нажимаем на кнопку "Добавить"
                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                enable_loader(params, 45)

                # Обновляем страницу и проверяем, что карточка КА появилась в списке юр. лиц
                params.refresh()
                wait_page(params, url_contractors_org)

                find_el(params, btn_tab_legal_entities_on_the_contractor_page.xpath)
                click(params)

                # Найдем только что созданного КА в списке и перейдем в него
                find_el(params, f"//span[@title='{company_name}']")
                find_el(params, f"//span[@title='{company_inn_number}']")
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Убедимся, что это нужный КА
                find_el(params, f"//span[contains(text(), '{company_name}')]")
                find_el(params, f"//span[contains(text(), '{company_inn_number}')]")

                """Удаление созданного КА"""
                find_el(params, btn_delete_ka_on_the_card_create_contractor.xpath)
                click(params)

                find_el(params, btn_delete_ka_on_the_popup_card_create_contractor.xpath)
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

        """2. Создание Контрагента (Юридическое лицо) - не Россия"""
        def creating_a_legal_entity_ka_not_ru():
            description = "Создание Контрагента (Юридическое лицо) - не Россия"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                """Кликаем на кнопку '+ Добавить'"""
                find_el(params, btn_add_on_the_contractors_main_page.xpath)
                click(params)

                """Заполняем форму 'Новый контрагент'"""
                # Кликаем на "Юридическое лицо" и выбираем другую страну (КЗ) заполняем форму и нажимаем 'Далее'
                find_el(params, btn_tab_legal_entities_ka_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_country_ka_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_kazakhstan_country_on_the_popup_new_contractor.xpath)
                click(params)

                # Заполняем БИН и кликаем "Далее"
                find_el(params, inp_bin_on_the_popup_new_contractor.xpath)
                send_keys(params, company_inn_number_kz)

                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Проверим, что загрузились нужные данные
                check_text_attribute(params, inp_bin_on_the_popup_new_contractor.xpath, company_inn_number_kz)

                find_el(params, inp_name_company_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, choice_name_company_in_the_input_on_popup_new_contractor.xpath)
                click(params)

                # Нажимаем на кнопку "Добавить"
                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                enable_loader(params, 45)

                # Обновляем страницу и проверяем, что карточка КА появилась в списке юр. лиц
                params.refresh()
                wait_page(params, url_contractors_org)

                find_el(params, btn_tab_legal_entities_on_the_contractor_page.xpath)
                click(params)

                # Найдем только что созданного КА в списке и перейдем в него
                find_el(params, f"//span[contains(@title, '{company_name_kz}')]")
                find_el(params, f"//span[contains(@title, '{company_inn_number_kz}')]")
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Убедимся, что это нужный КА
                find_el(params, f"//span[contains(text(), '{company_name_kz}')]")
                find_el(params, f"//span[contains(text(), '{company_inn_number_kz}')]")

                """Удаление созданного КА"""
                find_el(params, btn_delete_ka_on_the_card_create_contractor.xpath)
                click(params)

                find_el(params, btn_delete_ka_on_the_popup_card_create_contractor.xpath)
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

        """3. Проверка полей у юр.лиц при разных странах"""
        def checking_fields_for_legal_entities_in_different_countries():
            description = "Проверка полей у юр.лиц при разных странах"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                """Кликаем на кнопку '+ Добавить'"""
                find_el(params, btn_add_on_the_contractors_main_page.xpath)
                click(params)

                """Проверяем форму 'Новый контрагент', исходя из разных стран"""
                # Кликаем на "Юридическое лицо" и заполняем форму и нажимаем 'Далее'
                find_el(params, btn_tab_legal_entities_ka_on_the_popup_new_contractor.xpath)
                click(params)

                # Проверка поля при стране - Россия
                find_el(params, inp_inn_on_the_popup_new_contractor.xpath)

                # Переключение на страну Беларусь и проверка поля УНП
                find_el(params, btn_choosing_a_country_ka_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_belarus_country_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, inp_upn_on_the_popup_new_contractor.xpath)

                # Переключение на страну Казахстан и проверка поля БИН
                find_el(params, btn_choosing_a_country_ka_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_kazakhstan_country_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, inp_bin_on_the_popup_new_contractor.xpath)

                # Переключение на страну Армения и проверка поля ИНН
                find_el(params, btn_choosing_a_country_ka_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_armenia_country_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, inp_inn_on_the_popup_new_contractor.xpath)

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

        """4. Создание Контрагента (Юридическое лицо) негативные проверки"""
        def creating_a_legal_entity_ka_negative_checks():
            description = "Создание Контрагента (Юридическое лицо) негативные проверки"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                """Кликаем на кнопку '+ Добавить' и переходим в Юридические лица"""
                find_el(params, btn_add_on_the_contractors_main_page.xpath)
                click(params)

                find_el(params, btn_tab_legal_entities_ka_on_the_popup_new_contractor.xpath)
                click(params)

                """Негативные проверки"""
                # Проверяем задизэйблена ли кнопка, чтобы исключить отправку формы с пустым номером
                find_el(params, btn_next_check_disabled_on_the_popup_new_contractor.xpath)

                # Заполняем поле 'ИНН' символами отличными от цифр (буквы)
                find_el(params, inp_inn_on_the_popup_new_contractor.xpath)
                send_keys(params, test_message)  # Передадим False, чтобы увидеть ошибку о невалидном вводе
                find_el(params, text_error_empty_phone_number_on_the_popup_new_contractor.xpath)

                # Заполняем поле 'ИНН' несуществующим номером
                find_el(params, inp_inn_on_the_popup_new_contractor.xpath)
                send_keys(params, cvv_cvc_code_test)  # Передадим False, чтобы увидеть ошибку о невалидном вводе
                find_el(params, text_error_invalid_inn_number_on_the_popup_new_contractor.xpath)

                # Введем корректный ИНН и нажмем на кнопку "Далее", чтобы открылась дальнейшая форма
                find_el(params, inp_inn_on_the_popup_new_contractor.xpath)
                send_keys(params, company_inn_number)

                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Нажмем на кнопку "Добавить" не заполняя форму и идентифицируем ошибку
                click(params, True)
                find_el(params, text_error_empty_company_name_on_the_popup_new_contractor.xpath)

                # Введем в поле КПП невалидное значение и отловим ошибку валидации поля
                find_el(params, inp_kpp_on_the_popup_new_contractor.xpath)
                send_keys(params, cvv_cvc_code_test)

                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params, True)

                find_el(params, text_error_invalid_kpp_number_on_the_popup_new_contractor.xpath)

                # Проверим, что имеется ошибка валидации поля наименование компании, если оно пустое
                find_el(params, text_error_empty_phone_number_on_the_popup_new_contractor.xpath)

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

        status_and_name_tst = creating_a_legal_entity_ka_ru()
        status_and_name_tst = creating_a_legal_entity_ka_not_ru()
        status_and_name_tst = checking_fields_for_legal_entities_in_different_countries()
        status_and_name_tst = creating_a_legal_entity_ka_negative_checks()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

