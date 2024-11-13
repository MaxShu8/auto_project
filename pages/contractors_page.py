from site_objects import SiteObjects


"""Элементы страницы \"Контрагенты\" """

btn_add_on_the_contractors_main_page = SiteObjects(
    "Кнопка 'Добавить' на странице 'Контрагенты'",
    "//span[contains(text(), 'Добавить')]")

# data_exist_ka_in_the_list_contractor_page = SiteObjects(
#     "Карточка КА в списке на странице контрагент",
#     f"//span[@title='{}']")

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


# Карточка созданного КА

text_name_ka_on_the_card_create_contractor = SiteObjects(
    "Наименование КА в карточке контрагента",
    "//span[contains(., 'Тестовый')]")

btn_delete_ka_on_the_card_create_contractor = SiteObjects(
    "Кнопка 'Удалить' в карточке контрагента",
    "//span[contains(., 'Удалить')]")

btn_delete_ka_on_the_popup_card_create_contractor = SiteObjects(
    "Кнопка 'Удалить' в карточке контрагента",
    "//button[@class='vz-button primary big']")













