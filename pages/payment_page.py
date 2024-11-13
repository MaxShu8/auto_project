from site_objects import SiteObjects

"""Шлюз оплаты Альфа"""

# Элементы тестового шлюза

input_number_card_alfa = SiteObjects(
    "Поле 'Номер карты' при заполнении данных платежа в Альфе",
    "//span[contains(text(), 'Номер карты')]/../span/input[@type='tel']")

input_cardholder_name_alfa = SiteObjects(
    "Поле 'Имя владельца' при заполнении данных платежа в Альфе",
    "//span[contains(text(), 'Имя владельца')]/../span/input[@type='text']")

input_expiration_date_alfa = SiteObjects(
    "Поле 'ММ/ГГ' при заполнении данных платежа в Альфе",
    "//span[contains(text(), 'ММ/ГГ')]/../span/input[@type='tel']")

input_cvv_cvc_code_alfa = SiteObjects(
    "Поле 'CVV/CVC' при заполнении данных платежа в Альфе",
    "//span[contains(text(), 'CVV/CVC')]/../span/input[@type='password']")

btn_pay_alfa = SiteObjects(
    "Кнопка 'Оплатить' у контрагента",
    "//button[@id='submit']")

# Элементы продовского шлюза

btn_pay_alfa_prod = SiteObjects(
    "Кнопка 'Оплатить' у контрагента",
    "//button[@class='Button_button__w+JtY Button_primary__ki19P']")

input_number_card_alfa_prod = SiteObjects(
    "Поле 'Номер карты' при заполнении данных платежа в Альфе",
    "(//input[@class='Input_input__eXwaT'])[1]")

input_expiration_date_alfa_prod = SiteObjects(
    "Поле 'Имя владельца' при заполнении данных платежа в Альфе",
    "(//input[@class='Input_input__eXwaT'])[2]")

input_cvv_cvc_code_prod = SiteObjects(
    "Поле 'Имя владельца' при заполнении данных платежа в Альфе",
    "(//input[@class='Input_input__eXwaT CvcInput_input__Bi2to'])[1]")

btn_pay_alfa_after_input_data_prod = SiteObjects(
    "Кнопка 'Оплатить' у контрагента в форме оплаты Альфы",
    "//button[@type='submit']")

inp_confirm_code_alfa_prod = SiteObjects(
    "Кнопка 'Оплатить' у контрагента в форме оплаты Альфы",
    "//input[@id='pwdInputVisible']")

text_code_sms_on_phone_alfa_prod = SiteObjects(
    "Текст в форме 'код отправлен на 79********24'",
    "//p[@class='heading heading_size_s'][contains(text(), 'Код отправлен')]")

inp_confirm_sms_code_vtb_prod = SiteObjects(
    "Поле 'Код из СМС' в форме подтверждения оплаты ВТБ",
    "//p[@class='desc'][contains(text(), 'введите код')]")











