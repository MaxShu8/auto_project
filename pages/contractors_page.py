from site_objects import SiteObjects


"""Элементы страницы \"Контрагенты\" """

btn_add_on_the_contractors_main_page = SiteObjects(
    "Кнопка 'Добавить' на странице 'Контрагенты'",
    "//span[contains(text(), 'Добавить')]")

list_of_ka_on_the_contractor_page = SiteObjects(
    "Список КА на странице контрагентов",
    "//div[@class='vz-contractors-list']")

btn_tab_favorites_on_the_contractor_page = SiteObjects(
    "Кнопка вкладка 'Избранные' на странице контрагентов",
    "//span[contains(text(), 'Избранные')]")

btn_tab_individuals_on_the_contractor_page = SiteObjects(
    "Кнопка вкладка 'Физические лица' на странице контрагентов",
    "//span[contains(text(), 'Физические лица')]")

btn_tab_legal_entities_on_the_contractor_page = SiteObjects(
    "Кнопка вкладка 'Юридические лица' на странице контрагентов",
    "//span[contains(text(), 'Юридические лица')]")

inp_search_ka_on_the_contractor_page = SiteObjects(
    "Поле 'Поиск' на странице 'Контрагенты'",
    "//input[@class='vz-input-control iconical']")

btn_add_claim_on_the_contractors_main_page = SiteObjects(
    "Кнопка 'Добавить' на странице 'Контрагенты'",
    "//span[contains(., 'Добавить')]")


# Попап "Новый контрагент"

btn_tab_individual_ka_on_the_popup_new_contractor = SiteObjects(
    "Кнопка вкладка 'Физическое лицо' в попапе 'Новый контрагент'",
    "//span[contains(text(), 'Физическое лицо')]")

btn_tab_legal_entities_ka_on_the_popup_new_contractor = SiteObjects(
    "Кнопка вкладка 'Юридическое лицо' в попапе 'Новый контрагент'",
    "//span[contains(text(), 'Юридическое лицо')]")

inp_phone_on_the_popup_new_contractor = SiteObjects(
    "Поле 'Телефон' в попапе 'Новый контрагент'",
    "//label[contains(text(), 'Телефон')]/../div/input")

inp_inn_on_the_popup_new_contractor = SiteObjects(
    "Поле 'ИНН' в попапе 'Новый контрагент'",
    "//label[contains(text(), 'ИНН')]/../div/input")

inp_kpp_on_the_popup_new_contractor = SiteObjects(
    "Поле 'КПП' в попапе 'Новый контрагент'",
    "//label[contains(text(), 'КПП')]/../div/input")

inp_name_company_on_the_popup_new_contractor = SiteObjects(
    "Поле 'Наименование компании' в попапе 'Новый контрагент'",
    "//label[contains(text(), 'Наименование компании')]/../div/input")

inp_upn_on_the_popup_new_contractor = SiteObjects(
    "Поле 'УНП' в попапе 'Новый контрагент'",
    "//label[contains(text(), 'УНП')]/../div/input")

inp_bin_on_the_popup_new_contractor = SiteObjects(
    "Поле 'БИН' в попапе 'Новый контрагент'",
    "//label[contains(text(), 'БИН')]/../div/input")

choice_name_company_in_the_input_on_popup_new_contractor = SiteObjects(
    "Вариант наименования компании при клике на поле 'Наименование компании' в попапе 'Новый контрагент'",
    "//div[@class='vz-new-autocomplete-list-item-title']")

btn_next_or_add_on_the_popup_new_contractor = SiteObjects(
    "Кнопка 'Далее'/'Добавить' в попапе 'Новый контрагент'",
    "//div[@class='vz-dialog-card-buttons']/button[@class='vz-button primary']/span")

inp_fio_on_the_popup_new_contractor = SiteObjects(
    "Поле 'ФИО' в попапе 'Новый контрагент'",
    "//label[contains(text(), 'ФИО')]/../div/input")

btn_choosing_a_country_phone_on_the_popup_new_contractor = SiteObjects(
    "Кнопка выбора страны телефона 'Физическое лицо' в попапе 'Новый контрагент'",
    "//div[contains(@class, 'vz-select-dropdown select-country')]")

btn_choosing_a_country_ka_on_the_popup_new_contractor = SiteObjects(
    "Кнопка выбора страны КА 'Физическое лицо' в попапе 'Новый контрагент'",
    "//span[text()='Статус']/..//div[contains(@class, 'vz-select-dropdown-value')]")

btn_choosing_a_belarus_country_on_the_popup_new_contractor = SiteObjects(
    "Кнопка выбора страны 'Беларусь' в попапе 'Новый контрагент'",
    "//div[@title='Беларусь']")

btn_choosing_a_kazakhstan_country_on_the_popup_new_contractor = SiteObjects(
    "Кнопка выбора страны 'Казахстан' в попапе 'Новый контрагент'",
    "//div[@title='Казахстан']")

btn_choosing_a_armenia_country_on_the_popup_new_contractor = SiteObjects(
    "Кнопка выбора страны 'Армения' в попапе 'Новый контрагент'",
    "//div[@title='Армения']")

btn_next_check_disabled_on_the_popup_new_contractor = SiteObjects(
    "Задизэйбленная кнопка 'Далее' в попапе 'Новый контрагент'",
    "//span[text()='Далее']/../../button[@disabled]")


# Ошибки

text_error_empty_fio_on_the_popup_new_contractor = SiteObjects(
    "Текст ошибки если не указать ФИО - 'Укажите ФИО'",
    "//span[contains(., 'Укажите ФИО')]")

text_error_invalid_phone_number_on_the_popup_new_contractor = SiteObjects(
    "Текст ошибки если не указать ФИО - 'Укажите ФИО'",
    "//div[text()='Неверный формат телефона']")

text_error_empty_phone_number_on_the_popup_new_contractor = SiteObjects(
    "Текст ошибки если не указать ФИО - 'Укажите ФИО'",
    "//div[text()='Поле обязательно для заполнения']")

text_error_empty_company_name_on_the_popup_new_contractor = SiteObjects(
    "Текст ошибки если не указать наименование организации",
    "//span[contains(text(), 'Укажите наименование организации')]")

text_error_invalid_inn_number_on_the_popup_new_contractor = SiteObjects(
    "Текст ошибки если некорректно ввести КПП",
    "//div[text()='Неверно введен ИНН']")

text_error_invalid_kpp_number_on_the_popup_new_contractor = SiteObjects(
    "Текст ошибки если некорректно ввести КПП",
    "//div[text()='Неверно введен КПП']")


"""Карточка контрагента"""

text_name_ka_on_the_card_create_contractor = SiteObjects(
    "Наименование КА в карточке контрагента",
    "//span[contains(., 'Тестовый')]")

btn_delete_ka_on_the_card_create_contractor = SiteObjects(
    "Кнопка 'Удалить' в карточке контрагента",
    "//span[contains(., 'Удалить')]")

btn_delete_ka_on_the_popup_card_create_contractor = SiteObjects(
    "Кнопка 'Удалить' в карточке контрагента",
    "//button[@class='vz-button primary big']")

btn_add_a_contact_on_the_card_contractor = SiteObjects(
    "Кнопка 'Добавить контакты' в карточке контрагента",
    "//span[contains(., 'контакты')]")

btn_the_expand_contact_block_button_in_the_counterparty_card_contractor = SiteObjects(
    "Кнопка развернуть блок контактов в карточке контрагента",
    "//div[@class='vz-icon mdi mdi-chevron-down rounded-icon vz-collapse-header-collapsebtn vz-cursor-pointer out']")

btn_hide_payer_button_card_contractor = SiteObjects(
    "Кнопка 'Скрыть плательщика' в карточке контрагента",
    "//div[contains(@class, 'vz-toggler-button')]")


# Модалка "Новый контакт"

inp_fio_on_the_popup_new_contact = SiteObjects(
    "Поле 'ФИО' в попапе 'Новый контакт'",
    "//label[contains(text(), 'ФИО')]/../div/input[contains(@class, 'vz-input-control')]")

inp_phone_on_the_popup_new_contact = SiteObjects(
    "Поле 'Телефон' в попапе 'Новый контакт'",
    "//label[contains(text(), 'Телефон')]/../div/input[contains(@class, 'vz-input-control')]")

inp_email_on_the_popup_new_contact = SiteObjects(
    "Поле 'Email' в попапе 'Новый контакт'",
    "//label[contains(text(), 'Email')]/../div/input[contains(@class, 'vz-input-control')]")

btn_add_a_contact_on_the_popup_card_contractor = SiteObjects(
    "Кнопка 'Добавить контакты' в карточке контрагента",
    "//div[@class='vz-dialog-card-buttons']/..//span[contains(., 'Добавить')]")

text_error_incorrect_phone_format_on_the_popup_new_contractor = SiteObjects(
    "Текст ошибки если некорректно ввести номер телефона",
    "//div[@class='vz-invalid-message error' and contains(., 'Неверный формат телефона')]")

text_error_error_invalid_email_address_format_on_the_popup_new_contractor = SiteObjects(
    "Текст ошибки если некорректно ввести электронную почту",
    "//div[@class='vz-invalid-message error' and contains(., 'Неверный формат email адреса')]")

# Блок "Контакты" у КА

text_fio_contact_on_the_card_contractor = SiteObjects(
    "ФИО в карточке контакта",
    "//p/span[text()='ФИО']/../span[2]")

text_phone_contact_on_the_card_contractor = SiteObjects(
    "Телефон в карточке контакта",
    "//p/span[text()='Телефон']/../span[2]")

text_email_contact_on_the_card_contractor = SiteObjects(
    "Email в карточке контакта",
    "//p/span[text()='Email']/../span[2]")

btn_editing_contact_on_the_card_contractor = SiteObjects(
    "Кнопка Редактировать в карточке контакта",
    "//div[@class='vz-icon mdi mdi-pencil rounded-icon vz-cursor-pointer']")

input_fio_contact_on_the_card_contractor = SiteObjects(
    "Поле ФИО в карточке контактов",
    "//label[contains(text(), 'ФИО')]/..//input[@class='vz-input-control']")

btn_cancel_editing_contact_on_the_card_contractor = SiteObjects(
    "Кнопка Отмена редактирования в карточке контакта",
    "//div[@class='vz-icon mdi mdi-close rounded-icon mr-10 vz-cursor-pointer']")

btn_confirm_editing_contact_on_the_card_contractor = SiteObjects(
    "Кнопка подтверждения редактирования в карточке контакта",
    "//div[contains(@class, 'vz-icon mdi mdi-check rounded-icon')]")

btn_delete_contact_on_the_card_contractor = SiteObjects(
    "Кнопка подтверждения редактирования в карточке контакта",
    "//span[contains(., 'Контакт №')]/../..//div[contains(@class, 'vz-icon mdi mdi-delete')]")

text_the_contact_counter_in_the_contacts_with_counterparties_block = SiteObjects(
    "Счетчик в карточке контакта",
    "//span[contains(text(), 'Контакты')]")


# Модалка "Удаление контакта"

btn_delete_contact_on_the_popup_deleting_contact_on_card_contractor = SiteObjects(
    "Кнопка подтверждения удаления контакта в попапе Удаление контакта",
    "//div[contains(@class, 'vz-dialog-card-buttons')]//span[contains(., 'Подтвердить')]")

btn_cancel_delete_contact_on_the_popup_deleting_contact_on_card_contractor = SiteObjects(
    "Кнопка отмены подтверждения удаления контакта в попапе Удаление контакта",
    "//div[contains(@class, 'vz-dialog-card-buttons')]//span[contains(., 'Отмена')]")


"""Различные уведомления"""
text_notification_the_claim_has_been_registered = SiteObjects(
    "Уведомление о том, что претензия зарегистрирована",
    "//div[contains(@class, 'vz-toast-wrapper-content')]/span[contains(., 'претензия зарегистрирована')]")

"""Претензии"""
btn_show_collapse_counterparty_claims_on_card_contractor = SiteObjects(
    "Кнопка показать/свернуть претензии у контрагента",
    "//div[contains(@class, 'vz-icon mdi mdi-chevron-down rounded-icon vz-collapse-header-collapsebtn vz-cursor-pointer out')]")

text_the_claim_number_in_the_created_claim = SiteObjects(
    "Номер претензии в созданной претензии",
    "//div[@class='vz-contact-panel-header-title']")

text_the_order_number_in_the_created_claim = SiteObjects(
    "Номер заказа в созданной претензии",
    "//span[text()='Номер заказа']/../span[2]")

