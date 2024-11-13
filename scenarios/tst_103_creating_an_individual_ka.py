import time

from Business_Actions import *
from Methods import *
from pages.contractors_page import *


def check_creating_an_individual_ka(params):
    main_description = "Тест №103 - Создание КА — ФИЗ.лицо"
    status_and_name_tst = {}

    try:
        authorization_lk(params, url_base_org)

        """1. Создание Контрагента (Физическое лицо), Россия, российский номер телефона"""
        def creating_an_individual_ka_ru_phone():
            description = "Создание Контрагента (Физическое лицо), Россия, Российский номер телефона (VZ)"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                """Кликаем на кнопку '+ Добавить'"""
                find_el(params, btn_add_on_the_contractors_main_page.xpath)
                click(params)

                """Заполняем форму 'Новый контрагент'"""
                # Заполняем поле 'Телефон' и нажимаем 'Далее'
                find_el(params, inp_phone_on_the_popup_new_contractor.xpath)
                send_keys(params, add_individual_phone_ru)

                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Проверим, что загрузились нужные данные
                check_text_attribute(params, inp_phone_on_the_popup_new_contractor.xpath, '+7 (967) 979-97-93')
                check_text_attribute(params, inp_fio_on_the_popup_new_contractor.xpath, add_individual_fio_ka)

                # Нажимаем на кнопку "Добавить"
                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                enable_loader(params, 45)

                # Обновляем страницу и проверяем, что карточка КА появилась в списке физ. лиц
                params.refresh()
                wait_page(params, url_contractors_org)

                find_el(params, f"//span[@title='{add_individual_fio_ka}']")

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

        """2. Создание Контрагента (Физическое лицо), Россия, зарубежный номер телефона"""
        def creating_an_individual_ka_not_ru_phone():
            description = "Создание Контрагента (Физическое лицо), Россия, Зарубежный номер телефона (VZ)"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                """Кликаем на кнопку '+ Добавить'"""
                find_el(params, btn_add_on_the_contractors_main_page.xpath)
                click(params)

                """Заполняем форму 'Новый контрагент'"""
                # Выбираем страну у поля "Телефон" Заполняем поле 'Телефон' и нажимаем 'Далее'
                find_el(params, btn_choosing_a_country_phone_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_belarus_country_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, inp_phone_on_the_popup_new_contractor.xpath)
                send_keys(params, add_individual_phone_bel, clean_before=False)  # отключим предварительную очистку, чтобы бел. номер не превратился в казахский

                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Проверим, что загрузились нужные данные
                # check_text_attribute(params, inp_phone_on_the_popup_new_contractor.xpath, '+375 (77) 777-77-77')
                # check_text_attribute(params, inp_fio_on_the_popup_new_contractor.xpath, add_individual_fio_ka)

                # Проверим отправку без заполнения ФИО
                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params, True)
                find_el(params, text_error_empty_fio_on_the_popup_new_contractor.xpath)

                # Заполним ФИО
                find_el(params, inp_fio_on_the_popup_new_contractor.xpath)
                send_keys(params, add_test_name_ka)

                # Нажимаем на кнопку "Добавить"
                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params, True)  # Передадим True для того, чтобы исключить тот момент, если ошибка все еще висит

                enable_loader(params, 45)

                # Обновляем страницу и проверяем, что карточка КА появилась в списке физ. лиц
                params.refresh()
                params.refresh()
                wait_page(params, url_contractors_org)

                # Найдем только что созданного КА в списке и перейдем в него
                find_el(params, f"//span[@title='{add_test_name_ka}']")
                find_el(params, f"//span[@title='375{add_individual_phone_bel}']")
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Убедимся, что это нужный КА
                find_el(params, text_name_ka_on_the_card_create_contractor.xpath)

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

        """3. Создание Контрагента (Физическое лицо), не Россия, российский номер телефона"""
        def creating_an_individual_ka_not_ru_and_ru_phone():
            description = "Создание Контрагента (Физическое лицо), не Россия, Российский номер телефона"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                """Кликаем на кнопку '+ Добавить'"""
                find_el(params, btn_add_on_the_contractors_main_page.xpath)
                click(params)

                """Заполняем форму 'Новый контрагент'"""
                # Выбираем страну у КА и заполняем поле 'Телефон' и нажимаем 'Далее'
                find_el(params, btn_choosing_a_country_ka_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_kazakhstan_country_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, inp_phone_on_the_popup_new_contractor.xpath)
                send_keys(params, add_individual_phone_rf)

                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Проверим, что загрузились нужные данные
                # check_text_attribute(params, inp_phone_on_the_popup_new_contractor.xpath, '+375 (77) 777-77-77')
                # check_text_attribute(params, inp_fio_on_the_popup_new_contractor.xpath, add_individual_fio_ka)

                # Заполним ФИО
                find_el(params, inp_fio_on_the_popup_new_contractor.xpath)
                send_keys(params, add_test_name_ka_2)

                # Нажимаем на кнопку "Добавить"
                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params, True)  # Передадим True для того, чтобы исключить тот момент, если ошибка все еще висит

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 45)

                # Обновляем страницу и проверяем, что карточка КА появилась в списке физ. лиц
                params.refresh()
                wait_page(params, url_contractors_org)

                find_el(params, f"//span[@title='{add_test_name_ka_2}']")

                # Найдем только что созданного КА в списке и перейдем в него
                find_el(params, f"//span[@title='{add_test_name_ka_2}']")
                find_el(params, f"//span[@title='7{add_individual_phone_rf}']")
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Убедимся, что это нужный КА
                find_el(params, text_name_ka_on_the_card_create_contractor.xpath)

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

        """4. Создание Контрагента (Физическое лицо), Другая страна, номер телефона выбранной страны"""
        def creating_an_individual_ka_not_ru_and_not_ru_phone():
            description = "Создание Контрагента (Физическое лицо), Другая страна, Номер телефона выбранной страны"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                """Кликаем на кнопку '+ Добавить'"""
                find_el(params, btn_add_on_the_contractors_main_page.xpath)
                click(params)

                """Заполняем форму 'Новый контрагент'"""
                # Выбираем страну у КА и заполняем поле 'Телефон' и нажимаем 'Далее'
                find_el(params, btn_choosing_a_country_ka_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_kazakhstan_country_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_country_phone_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, btn_choosing_a_kazakhstan_country_on_the_popup_new_contractor.xpath)
                click(params)

                find_el(params, inp_phone_on_the_popup_new_contractor.xpath)
                send_keys(params, add_individual_phone_kz, clean_before=False)

                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Проверим, что загрузились нужные данные
                # check_text_attribute(params, inp_phone_on_the_popup_new_contractor.xpath, '+375 (77) 777-77-77')
                # check_text_attribute(params, inp_fio_on_the_popup_new_contractor.xpath, add_individual_fio_ka)

                # Заполним ФИО
                find_el(params, inp_fio_on_the_popup_new_contractor.xpath)
                send_keys(params, add_test_name_ka_2)

                # Нажимаем на кнопку "Добавить"
                find_el(params, btn_next_or_add_on_the_popup_new_contractor.xpath)
                click(params, True)  # Передадим True для того, чтобы исключить тот момент, если ошибка все еще висит

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 45)

                # Обновляем страницу и проверяем, что карточка КА появилась в списке физ. лиц
                params.refresh()
                wait_page(params, url_contractors_org)

                find_el(params, f"//span[@title='{add_test_name_ka_2}']")

                # Найдем только что созданного КА в списке и перейдем в него
                find_el(params, f"//span[@title='{add_test_name_ka_2}']")
                find_el(params, f"//span[@title='7{add_individual_phone_kz}']")
                click(params)

                # Подождем пока исчезнет лоадер (получим ответ от 1С)
                enable_loader(params, 15)

                # Убедимся, что это нужный КА
                find_el(params, text_name_ka_on_the_card_create_contractor.xpath)

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

        """5. Создание Контрагента (Физическое лицо) негативные проверки"""
        def creating_an_individual_ka_negative_checks():
            description = "Создание Контрагента (Физическое лицо) с пустым номером"

            try:
                """Переходим на страницу контрагентов"""
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)

                """Кликаем на кнопку '+ Добавить'"""
                find_el(params, btn_add_on_the_contractors_main_page.xpath)
                click(params)

                """Негативные проверки"""
                # Проверяем задизэйблена ли кнопка, чтобы исключить отправку формы с пустым номером
                find_el(params, btn_next_check_disabled_on_the_popup_new_contractor.xpath)

                # Заполняем поле 'Телефон' символами отличными от цифр (буквы)
                find_el(params, inp_phone_on_the_popup_new_contractor.xpath)
                send_keys(params, test_message, clean_before=False)  # Передадим False, чтобы увидеть ошибку о невалидном вводе
                find_el(params, text_error_invalid_phone_number_on_the_popup_new_contractor.xpath)

                find_el(params, inp_phone_on_the_popup_new_contractor.xpath)
                send_keys(params, test_white_space)
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

        status_and_name_tst = creating_an_individual_ka_ru_phone()
        status_and_name_tst = creating_an_individual_ka_not_ru_phone()
        status_and_name_tst = creating_an_individual_ka_not_ru_and_ru_phone()
        status_and_name_tst = creating_an_individual_ka_not_ru_and_not_ru_phone()
        status_and_name_tst = creating_an_individual_ka_negative_checks()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

