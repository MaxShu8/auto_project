from site_objects import SiteObjects


"""Элементы попапа формы \"Обратная связь\" """

btn_i_am_your_client_documents_page = SiteObjects(
    "Кнопка 'Я ваш клиент' на странице документы",
    "//span[contains(., 'Я ваш клиент')]")

txt_popup_i_am_your_client_popup_feedback = SiteObjects(
    "Текст 'Обратная связь' в попапе 'Обратная связь'",
    "//span[contains(., 'Обратная связь')]")

field_type_of_appeal_popup_feedback = SiteObjects(
    "Поле 'Тип обращения' в попапе 'Обратная связь'",
    "//span[@title='Вопрос по оформленной перевозке']")

choice_claim_in_type_appeal_field_popup_feedback = SiteObjects(
    "Опция 'Претензия' в выпадающем списке 'Тип обращения' в попапе 'Обратная связь'",
    "//span[contains(., 'Претензия')]")

choice_original_documents_in_type_appeal_field_popup_feedback = SiteObjects(
    "Опция 'Оригиналы документов' в выпадающем списке 'Тип обращения' в попапе 'Обратная связь'",
    "//span[contains(., 'Запрос оригиналов документов')]")

tab_by_cargo_original_documents_popup_feedback = SiteObjects(
    "Вкладка 'По грузу' в попапе 'Оригиналы документов'",
    "//div[contains(@class, 'vz-switcher-item') and (contains(., 'По грузу'))]")

tab_reconciliation_report_original_documents_popup_feedback = SiteObjects(
    "Вкладка 'Акт сверки' в попапе 'Оригиналы документов'",
    "//div[contains(@class, 'vz-switcher-item') and (contains(., 'Акт сверки'))]")

text_popup_claim_in_popup_feedback = SiteObjects(
    "Заголовок 'Претензия' в попапе 'Претензия'",
    "//span[@class='vz-dialog-card-header-title' and contains(.,' Претензия ')]")

text_popup_original_documents_in_popup_feedback = SiteObjects(
    "Заголовок 'Оригиналы документов' в попапе 'Запрос оригиналов документов'",
    "//span[@class='vz-dialog-card-header-title' and contains(.,'Запрос оригиналов документов')]")

input_number_of_order_popup_feedback = SiteObjects(
    "Поле 'Номер заказа' в попапе 'Обратная связь'",
    "//label[contains(text(), 'Номер заказа')]/..//input")

input_inn_company_popup_feedback = SiteObjects(
    "Поле 'ИНН' в попапе 'Обратная связь'",
    "//label[contains(text(), 'Компания')]/..//input")

choice_first_company_in_list_popup_feedback = SiteObjects(
    "Первая компания из списка в поле 'Компания' в попапе 'Обратная связь'",
    "//div[@class='vz-new-autocomplete-list-item active']")

input_email_popup_feedback = SiteObjects(
    "Поле 'E-mail' в попапе 'Обратная связь'",
    "//label[contains(text(), 'E-mail')]/..//input")

input_your_name_popup_feedback = SiteObjects(
    "Поле 'Ваше имя' в попапе 'Обратная связь'",
    "//label[contains(text(), 'Ваше имя')]/..//input")

input_your_phone_number_popup_feedback = SiteObjects(
    "Поле 'Номер телефона' в попапе 'Обратная связь'",
    "//label[contains(text(), 'Ваш телефон')]/..//input")

input_phone_number_from_the_order_popup_feedback = SiteObjects(
    "Поле 'Номер телефона из заказа' в попапе 'Запрос оригиналов документов'",
    "//label[contains(text(), 'Телефон из заказа')]/..//input")

input_bik_number_popup_feedback = SiteObjects(
    "Поле 'БИК' в попапе 'Обратная связь'",
    "//label[contains(text(), 'БИК')]/..//input")

input_payment_account_number_popup_feedback = SiteObjects(
    "Поле 'Расчетный счет' в попапе 'Обратная связь'",
    "//label[contains(text(), 'Расчётный счёт')]/..//input")

input_the_essence_of_the_claim_popup_feedback = SiteObjects(
    "Поле 'Суть претензии' в попапе 'Обратная связь'",
    "//label[contains(text(), 'Суть претензии')]/..//textarea")

input_message_popup_feedback = SiteObjects(
    "Поле 'Сообщение' в попапе 'Обратная связь'",
    "//label[contains(text(), 'Сообщение')]/..//textarea")

btn_upload_file_popup_feedback = SiteObjects(
    "Кнопка 'Добавить' (скан претензии) в попапе 'Обратная связь'",
    "(//input[@type='file'])[1]")

btn_send_feedback_form_popup_feedback = SiteObjects(
    "Кнопка 'Отправить' в попапе 'Обратная связь'",
    "//span[@class='vz-button-title' and text()=' Отправить ']")

btn_send_claim_popup_feedback = SiteObjects(
    "Кнопка 'Создать претензию' в попапе 'Обратная связь'",
    "//span[contains(., 'Создать претензию')]/ancestor::button")

btn_request_original_documents_popup_feedback = SiteObjects(
    "Кнопка 'Запросить' в попапе 'Запрос оригиналов документов'",
    "//span[contains(., 'Запросить')]")

popup_request_sending_success_popup_feedback = SiteObjects(
    "Уведомление 'Запрос успешно отправлен' в попапе 'Запрос оригиналов документов'",
    "//span[contains(., 'Запрос успешно отправлен')]")

btn_close_error_popup_feedback = SiteObjects(
    "Кнопка 'Закрыть' в попапе 'Запрос оригиналов документов'",
    "//div[@class='vz-toast-close']/span[@class='mdi mdi-close']")




