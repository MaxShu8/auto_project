

class SiteObjects:
    def __init__(self, description, xpath):
        self.description = description
        self.xpath = xpath


"""Окно авторизации/регистрации"""

btn_personal_area = SiteObjects(
            "Кнопка \"Личный Кабинет\" на главной в публичке",
            "(//div[@class='flex flex-align-items-center']//div[@class='public-header-button-personal-text text-o"
            "verflow'][contains(text(),'Личный кабинет')]//..//..)[1]")

inp_login = SiteObjects(
            "Поле \"Логин\" на главной в публичке",
            "//input[@placeholder='Телефон или E-mail*']")

btn_continue = SiteObjects(
            "Кнопка \"Далее\" в модалке авторизации",
            "//button[@class='vz-button primary large flex flex-center login-button']//span[@class='vz-button-tit"
            "le']/..")

inp_password = SiteObjects(
            "Поле \"Пароль\" на главной в публичке",
            "//input[@placeholder='Пароль*']")

btn_login = SiteObjects(
            "Кнопка \"Войти\" на главной в публичке",
            "//button[@class='vz-button primary large']//span[@class='vz-button-title']")

img_logo_lk = SiteObjects(
            "Лого Возовоз в ЛК",
            "//img[contains(@src,'/svg/logo/vz-logo-white.svg')]")

span_header_new_order = SiteObjects(
            "Ссылка в хэдере 'Новый заказ'",
            "//a[@href='/personal/order/create/']")

modalOffer = SiteObjects(
            "Модалка со спец. предложением в ЛК",
            "//div[contains(@class,'vz-adaptive-modal vz-offer-modal')]")

btn_offer_decline = SiteObjects(
            "Кнопка 'Не интересует' в модалке спец предложения",
            "//span[contains(.,'Не интересует')]/ancestor::button")

modal_set_to_pallet_offer_close = SiteObjects(
            "Крестик для закрытия toast",
            "(//div[@class='vz-toast-close'])[last()]")

input_login_on_auth_page = SiteObjects(
            "Поле 'Телефон или E-mail' на странице авторизации",
            "//input[@placeholder='Телефон или E-mail*']")



"""Main Page (Header)"""


"""Main Page (Menu)"""

btn_header_services = SiteObjects("Кнопка Услуги в верхнем меню",
                                  "//div[@class='public-header-menu-collapse-item-title'][contains(text(), 'Услуги')]")

btn_header_address_delivery = SiteObjects("Кнопка адресная доставка в 'Услуги'",
                                          "//a[@href='/address-delivery/'][contains(text(), 'Адресная доставка')]")

text_on_address_delivery = SiteObjects("Текст 'Забор груза' на странице адресная доставка",
                                       "//span[@class='mt-5'][contains(text(), 'Забор груза')]")

btn_header_wrapping = SiteObjects("Кнопка упаковка в 'Упаковка'",
                                  "//a[@href='/wrapping/'][contains(text(), 'Упаковка')]")

icon_on_wrapping = SiteObjects("Иконка 'Дополнительная упаковка' на странице упаковка",
                               "//a[@href='/wrapping/extra-package/']")

btn_header_safe_custody = SiteObjects("Кнопка ответственное хранение в 'Упаковка'",
                                      "//a[@href='/safe-custody/'][contains(text(), 'хранение')]")

text_on_safe_custody = SiteObjects("Текст 'Ответственное хранение' на странице Ответственное хранение",
                                   "//div[contains(text(), 'Ответственное хранение')]")

btn_header_insurance = SiteObjects("Кнопка страхование в 'Упаковка'",
                                   "//a[@href='/insurance/'][contains(text(), 'Страхование')]")

text_on_insurance = SiteObjects("Текст 'Страхование грузов' на странице страхование",
                                "//div[contains(text(), 'Страхование грузов')]")

btn_header_cargo_loading = SiteObjects("Кнопка ППР в 'Упаковка'",
                                       "//a[@href='/cargo-loading/'][contains(text(), 'разгрузочные работы')]")

text_on_cargo_loading = SiteObjects("Текст 'ПРР на адресе' на странице ПРР",
                                    "//span[@class='text-bold'][contains(text(), 'ПРР на адресе')]")

btn_header_yandex_market = SiteObjects("Кнопка Яндекс-Маркет в 'Упаковка'",
                                       "//a[@href='/yandex-market/'][contains(text(), 'Яндекс')]")

banner_on_yandex_market = SiteObjects("Баннер 'Яндекс' на странице Яндекс-маркет",
                                      "//div[@class='yandex_info-banner']")

btn_header_ozon = SiteObjects("Кнопка Яндекс-Маркет в 'Упаковка'",
                              "//a[@href='/ozon/'][contains(text(), 'OZON')]")

banner_on_ozon = SiteObjects("Баннер 'Ozon' на странице Ozon-маркет",
                             "//div[@class='ozon_info-banner-text-description']")

btn_header_networkshops = SiteObjects("Кнопка Доставка в торговые сети в 'Упаковка'",
                                      "//a[@href='/networkshops/'][contains(text(), 'торговые сети')]")

text_on_networkshops = SiteObjects("Текст 'Vozovoz' на странице доставка в маркетплейсы",
                                   "//h2[@class='vz-text-align-left'][contains(text(), 'Vozovoz')]")

btn_header_online_store = SiteObjects("Кнопка Доставка для интернет-магазинов в 'Упаковка'",
                                      "//a[@href='/online-store/'][contains(text(), 'для интернет-магазинов')]")

text_on_online_store = SiteObjects("Текст 'Vozovoz' на странице доставка в маркетплейсы",
                                   "//div[@class='online-store-services__introduction public-container-mobile'][contains(text(), 'для интернет-магазинов')]")

btn_header_delivery_russia = SiteObjects("Кнопка Доставка в торговые сети в 'Упаковка'",
                                      "//a[@href='/delivery-russia/'][contains(text(), 'Доставка сборных грузов')]")

text_on_delivery_russia = SiteObjects("Текст 'Vozovoz' на странице доставка в маркетплейсы",
                                   "//span[contains(text(), 'для доставки сборного груза')]")

btn_header_free_group_pickup = SiteObjects("Кнопка Бесплатный ГЗ в 'Услуги'",
                                      "//a[@href='/free-group-pickup/'][contains(text(), 'Бесплатный групповой забор')]")

banner_on_free_group_pickup = SiteObjects("Banner на странице бесплатный ГЗ",
                                   "//div[@id='banner']")

btn_header_cargo_belarus = SiteObjects("Кнопка Грузоперевозки Беларусь",
                                      "//a[@href='/belarus/'][contains(text(), 'Беларусь')]")

text_on_cargo_belarus = SiteObjects("Текст на странице Грузоперевозки Беларусь",
                                   "//span[contains(text(), 'Беларуси')]")

btn_header_cargo_kazakhstan = SiteObjects("Кнопка Грузоперевозки Казахстан",
                                      "//a[@href='/kazakhstan/'][contains(text(), 'Казахстан')]")

text_on_cargo_kazakhstan = SiteObjects("Текст на странице Грузоперевозки Казахстан",
                                   "//h2[contains(text(), 'Казахстане')]")

btn_header_cargo_china = SiteObjects("Кнопка Грузоперевозки Китай",
                                      "//a[@href='/china/'][contains(text(), 'Китай')]")

text_on_cargo_china = SiteObjects("Текст на странице Грузоперевозки Китай",
                                   "//span[@class='color-primary'][contains(text(), 'Китая')]")

btn_header_shipping_types = SiteObjects("Кнопка Типы грузоперевозок",
                                      "//a[@href='/shippingtypes/'][contains(text(), 'Типы')]")

text_on_shipping_types = SiteObjects("Текст на странице типы грузоперевозок",
                                     "//h2[@class='vz-text-align-left'][contains(text(), 'грузы')]")

btn_header_fast_delivery_capital = SiteObjects("Кнопка перевозка между столицами",
                                      "//a[@href='/fast-delivery-capital/'][contains(text(), 'столицами')]")

text_on_fast_delivery_capital = SiteObjects("Текст на странице перевозка между столицами",
                                            "//h2[@class='vz-text-align-left'][contains(text(), 'между')]")

btn_header_directions = SiteObjects("Кнопка Грузоперевозки",
                                    "//a[@href='/directions/'][contains(text(), 'Направления')]")

text_on_directions = SiteObjects("Текст на странице Грузоперевозки",
                                 "//div[@class='directions-most-popular mt-60 mb-60']//h2[contains(text(), 'направления')]")





btn_header_info = SiteObjects("Кнопка Информация в хедере",
                              "//div[@class='public-header-menu-collapse-item-title'][contains(text(), 'Услуги')]")

btn_header_geo = SiteObjects("Кнопка География",
                             "//a[@class='public-header-menu-item'][contains(text(), 'География')]")


"""Main Page (Mini-calculator)"""

div_loader = SiteObjects("Лоадер в мини калькуляторе",
                         "//div[@class='vz-loader']")

input_from_mini = SiteObjects("Поле Откуда в мини-калькуляторе",
                              "//label[contains(text(), 'Откуда')]/ancestor::div[@class='vz-input']/div/input")

list_from_mini = SiteObjects("Список поля Откуда в мини-калькуляторе",
                             "//div[contains(@class, 'vz-new-autocomplete-list vz-scroll')][1]")

# first_value_in_list_from = SiteObjects("Первый в списке поля Откуда в мини-калькуляторе",
#                                        "//div[@class='vz-new-autocomplete-list-item-title'][contains(text(), 'Санкт-Петербург')]/ancestor::div[@class='vz-new-autocomplete-list-item active']")

# first_value_in_list_to = SiteObjects("Первый в списке поля Куда в мини-калькуляторе",
#                                      "//div[@class='vz-new-autocomplete-list-item-title'][contains(text(), 'Москва')]/ancestor::div[@class='vz-new-autocomplete-list-item active']")

first_value_in_list_from = SiteObjects("Первый в списке поля Откуда в мини-калькуляторе",
                                       "//div[contains(@class, 'vz-new-autocomplete-list vz-scroll')][1]/div[@class='vz-new-autocomplete-list-item active']")

first_value_in_list_to = SiteObjects("Первый в списке поля Куда в мини-калькуляторе",
                                       "//div[contains(@class, 'vz-new-autocomplete-list vz-scroll')][2]/div[@class='vz-new-autocomplete-list-item active']")

list_to_mini = SiteObjects("Список поля Куда в мини-калькуляторе",
                           "//div[contains(@class, 'vz-new-autocomplete-list vz-scroll')][2]")

input_to_mini = SiteObjects("Поле Куда в мини-калькуляторе",
                            "//label[contains(text(), 'Куда')]/ancestor::div[@class='vz-input']/div/input")

btn_from_terminal = SiteObjects("От терминала в мини калькуляторе",
                                "//span[@class='vz-radiogroup-item-title'][contains(text(), 'От терминала')]")

btn_from_address = SiteObjects("От адреса в мини калькуляторе",
                               "//span[@class='vz-radiogroup-item-title'][contains(text(), 'От адреса')]")

btn_to_terminal = SiteObjects("До терминала в мини калькуляторе",
                              "//span[@class='vz-radiogroup-item-title'][contains(text(), 'До терминала')]")

btn_to_address = SiteObjects("До адреса в мини калькуляторе",
                             "//span[@class='vz-radiogroup-item-title'][contains(text(), 'До адреса')]")

btn_to_pvz = SiteObjects("До пункта выдачи в мини калькуляторе",
                         "//span[@class='vz-radiogroup-item-title'][contains(text(), 'До пункта')]")

price_mini = SiteObjects("Цена в мини-калькуляторе",
                         "//div[@class='vz-calculator-price-cost']/span")

btn_currency_mini_rub = SiteObjects("Радиокнопка выбора валюты",
                                   "//span[@class='vz-radiogroup-item-title'][contains(text(), '₽')]/parent::div/span[contains(@class, 'item-radio')]")

btn_currency_mini_kzt = SiteObjects("Радиокнопка выбора валюты",
                                    "//span[@class='vz-radiogroup-item-title'][contains(text(), '₸')]/parent::div/span[contains(@class, 'item-radio')]")

btn_currency_mini_ber = SiteObjects("Радиокнопка выбора валюты",
                                    "//span[@class='vz-radiogroup-item-title'][contains(text(), 'Br')]/parent::div/span[contains(@class, 'item-radio')]")

btn_currency_mini_active = SiteObjects("Активная кнопка валюты",
                                       "//span[@class='vz-radiogroup-item-title'][contains(text(), 'Br')]/parent::div/span[contains(@class, 'item-radio')]")

btn_change_city = SiteObjects("Кнопка поменять нас.пункты местами",
                                  "//img[@src='/svg/icon/narrow-swap.svg']")

price_mini_currency = SiteObjects("Цена в мини-калькуляторе",
                                  "//div[@class='vz-calculator-price-cost']/strong[contains(text(), 'Br')]")
