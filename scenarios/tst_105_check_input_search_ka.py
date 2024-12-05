import time
from Business_Actions import *
from Methods import *
from pages.contractors_page import *


def check_input_search_individual_and_legal_entity_ka(params):
    main_description = "Тест №105 - Проверка поиска КА"
    status_and_name_tst = {}

    try:
        """Авторизовываемся и переходим на страницу контрагентов"""
        authorization_lk(params, url_base_org, individual_phone_full, passw)

        set_page(params, url_contractors_org)
        wait_page(params, url_contractors_org)

        """1. Проверка поиска по ФИО, номеру телефона, email, наименованию компании, ИНН, КПП, ФИО сотрудника"""
        def search_individual_and_legal_ka():
            description = "Проверка поиска по ФИО, номеру телефона, email, наименованию компании, ИНН, КПП, ФИО сотрудника"

            try:
                """Позитивные проверки для КА"""

                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                # Поиск по ФИО
                send_keys(params, individual_fio)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым ФИО
                find_el(params, f"//span[@title='{individual_fio}']")

                # Поиск по номеру телефона
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, individual_phone_full)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым номером телефона
                find_el(params, f"//span[@title='{individual_phone_full}']")

                # Поиск по номеру email
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, individual_email)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым email
                find_el(params, f"//span[@title='{individual_email}']")

                # Поиск по наименованию компании
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, company_name2)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым наименованием компании
                find_el(params, f"//span[@title='{company_name2}']")

                # Поиск по ИНН компании
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, company_inn_number2)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым ИНН компании
                find_el(params, f"//span[@title='{company_inn_number2}']")

                # Поиск по КПП компании
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, company_kpp_number2)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым КПП компании
                find_el(params, f"//span[@title='{company_kpp_number2}']")

                # Поиск по имени менеджера компании
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, manager_name)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым именем менеджера компании
                find_el(params, f"//span[@title='{manager_name}']")

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

        """2. Прочие проверки для поиска КА"""
        def other_checks_for_the_search_ka():
            description = "Прочие проверки для поиска КА"

            try:
                """Проверка регистронезависимости"""
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, individual_fio_low_case)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым ФИО
                find_el(params, f"//span[@title='{individual_fio}']")

                """Поиск по части фамилии"""
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, individual_fio_not_full)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым ФИО
                find_el(params, f"//span[@title='{individual_fio}']")

                """Поиск если поменять данные местами"""
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, individual_fio_swap_places)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым номером телефона
                find_el(params, f"//span[@title='{individual_fio}']")

                """Поиск по части почты email"""
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, individual_email_not_full)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым email
                find_el(params, f"//span[@title='{individual_email}']")

                """Поиск по наличию пробелов в начале в конце"""
                find_el(params, inp_search_ka_on_the_contractor_page.xpath)
                click(params)

                send_keys(params, individual_fio_with_spaces)
                send_keys(params, Keys.ENTER, False)

                enable_loader(params, 15)

                # Проверим есть ли данная карточка в списке с искомым наименованием компании
                find_el(params, f"//span[@title='{individual_fio}']")

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

        status_and_name_tst = search_individual_and_legal_ka()
        status_and_name_tst = other_checks_for_the_search_ka()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

