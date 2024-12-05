from Business_Actions import *
from pages.payment_page import *
from pages.contacts_page import *
from various_data import *
from scenarios.tst_1_clicker_main_page import clicker_main_page
from scenarios.tst_12_check_authorization_mobile import check_authorization_mobile
from scenarios.tst_13_check_authorization_email import check_authorization_email
from scenarios.tst_14_check_mini_calculator import check_mini_calculator
from scenarios.tst_15_check_data_transfer_from_mini_calculator import check_data_transfer_from_mini_calculator
from scenarios.tst_16_check_cargo_tracking import check_cargo_tracking
from scenarios.tst_22_sending_feedback_forms import sending_feedback_forms
from scenarios.tst_36_1_create_order_t_t import create_order_t_t
# from scenarios.tst_36_2_create_order_t_t_cycle import create_order_t_t_cycle
from scenarios.tst_45_choice_of_another_currency import checking_the_choice_of_another_currency
from scenarios.tst_61_setting_the_cargo_category import checking_the_category_selection
from scenarios.tst_78_checking_the_order_search_field import checking_input_search_number_order
from scenarios.tst_103_creating_an_individual_ka import check_creating_an_individual_ka
from scenarios.tst_104_creating_legal_entity_ka import check_creating_legal_entity_ka
from scenarios.tst_105_check_input_search_ka import check_input_search_individual_and_legal_entity_ka
from scenarios.tst_116_hiding_the_payer import hiding_the_payer
from scenarios.tst_117_adding_contacts_to_a_CA_legal_entity import checking_the_addition_of_contacts_to_the_ka_card
from scenarios.tst_118_creating_claim_individual_and_legal_entity import creating_claim_individual_and_legal_entity_in_the_ka_card


def running_for_debug():
    """Названия новых тестов добавлять в список tests для прогона очередью"""
    tests = [creating_claim_individual_and_legal_entity_in_the_ka_card]

    success_counter = 0
    failed_tsts = []
    failed_counter = 0
    sum_duration = round(0, 2)
    desc_main = ""

    for i in tests:
        # Каждый раз запускаем новую сессию запуска драйвера (с одной сессией разные тесты не работают)
        session = driver_start()
        desc_main, tst_success, duration_test = record_timer(i, session)
        sum_duration += duration_test

        # Вытащим из объекта tst_success - имя теста и его статус, если тест провален, то добавляем в статистику
        for name_test, status in tst_success.items():

            if status is True:
                success_counter += 1
            else:
                failed_counter += 1
                msg = f"{failed_counter}. 🚫 - {name_test}\n"
                failed_tsts.append(msg)

    statistic_msg = f"🅰️ Ретест автотеста '{desc_main}': {success_counter} из {success_counter + failed_counter}\nОбщее время: {sum_duration} сек.\n"

    # Проверим, есть ли упавшие тесты, и если да, то добавим эту информацию в статистику
    if failed_counter > 0:
        statistic_msg += f"\n📉 Тестов не пройдено: {failed_counter}\n"

        for i in failed_tsts:
            statistic_msg += f"{i}"

        send_message_tg(statistic_msg, token, chat_id)
    else:
        send_message_tg(statistic_msg, token, chat_id)


def running_of_all():
    """Названия новых тестов добавлять в список tests для прогона очередью"""
    tests = [check_authorization_mobile, check_authorization_email, check_cargo_tracking,
             check_data_transfer_from_mini_calculator, sending_feedback_forms, checking_the_choice_of_another_currency,
             checking_the_category_selection, checking_input_search_number_order, check_creating_an_individual_ka,
             check_creating_legal_entity_ka, check_input_search_individual_and_legal_entity_ka, hiding_the_payer,
             checking_the_addition_of_contacts_to_the_ka_card]

    success_counter = 0
    failed_tsts = []
    failed_counter = 0
    sum_duration = 0

    for i in tests:
        # Каждый раз запускаем новую сессию запуска драйвера (с одной сессией разные тесты не работают)
        session = driver_start()
        desc_main, tst_success, duration_test = record_timer(i, session)
        sum_duration += duration_test

        # Вытащим из объекта tst_success - имя теста и его статус, если тест провален, то добавляем в статистику
        for name_test, status in tst_success.items():

            if status is True:
                success_counter += 1
            else:
                failed_counter += 1
                msg = f"{failed_counter}. {name_test} - 🚫\n"
                failed_tsts.append(msg)

    statistic_msg = f"☑️ Автотестов пройдено: {success_counter} из {success_counter + failed_counter}\nОбщее время: {sum_duration} сек."

    # Проверим, есть ли упавшие тесты, и если да, то добавим эту информацию в статистику
    if failed_counter > 0:
        statistic_msg += f"\n📉 Тестов не пройдено: {failed_counter}\n"

        for i in failed_tsts:
            statistic_msg += f"{i}"

        send_message_tg(statistic_msg, token, chat_id)
    else:
        send_message_tg(statistic_msg, token, chat_id)


running_for_debug()
# running_of_all()

