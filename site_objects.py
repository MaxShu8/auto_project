from various_data import *
import copy


"""URL сайтов (dev, org, ru)"""

url_base_dev = "https://vozovoz.dev/"
url_base_dev_LK = "https://vozovoz.dev/personal/orders/onward/"
url_base_dev_order_create = "https://vozovoz.dev/personal/order/create/"
url_base_dev_personal_order = "https://vozovoz.dev/personal/order/"
url_base_dev_order_create_public = "https://vozovoz.dev/order/create/"
url_documents_dev = "https://vozovoz.dev/documents/"
url_contacts_dev = "https://vozovoz.dev/contacts/"
url_contractors_dev = "https://vozovoz.dev/personal/contractors/"


url_base_org = "https://vozovoz.org/"
url_base_org_LK = "https://vozovoz.org/personal/orders/onward/"
url_base_org_order_create = "https://vozovoz.org/personal/order/create/"
url_base_org_order_create_public = "https://vozovoz.org/order/create/"
url_base_org_personal_order = "https://vozovoz.org/personal/order/"
url_base_org_auth = "https://vozovoz.org/personal/auth/"
url_after_create_org = "order-sent"
url_order_manage_org = "https://vozovoz.org/order/manage/"
url_contractors_org = "https://vozovoz.org/personal/contractors/"
url_contacts_org = "https://vozovoz.org/contacts/"
url_tariffs_org = "https://vozovoz.org/tariffs/"


url_base_ru = "https://vozovoz.ru/"
url_base_ru_LK = "https://vozovoz.ru/personal/orders"
url_base_ru_order_create = "https://vozovoz.ru/personal/order/create"
url_contractors_ru = "https://vozovoz.ru/personal/contractors/"
url_documents_ru = "https://vozovoz.ru/documents/"
url_tariffs_ru = "https://vozovoz.ru/tariffs/"



url_auk = "https://vozovoz.partners/"
url_auk_login = "https://dev.vozovoz.partners/login"
url_auk_dash = "https://dev.vozovoz.partners/dashboard"


"""Сайты партнеры - перевозчики - ссылки для мониторинга доступности документов"""

url_diligans = "https://tcdiligans.ru/documents"
url_timelogistik = "https://timelogistik.ru/documents"
url_t_technology = "https://t-technology.ru/documents"
url_severtrans = "https://severtrans-spb.ru/documents"
url_ugtrans = "https://ugtrans-tk.ru/documents"
url_logtavrii = "https://calc.apex-tech.ru/iframe/documents/?color=%23e42c31&id=168"


class SiteObjects:
    def __init__(self, description, xpath):
        self.description = description
        self.xpath = xpath
        self.copy_xpath = copy.copy(self.xpath)

    def change_xpath(self, element):
        self.xpath = self.xpath.replace("xxx", element)

    def reset_xpath(self):
        self.xpath = self.copy_xpath



"""Окно авторизации/регистрации"""

btn_personal_area = SiteObjects(
            "Кнопка \"Личный Кабинет\" на главной в публичке",
            "(//div[@class='flex flex-align-items-center ml-auto']//div[@class='public-header-button-personal-text text-overflow'][contains(text(),'Личный кабинет')]//..//..)[1]")

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

offer_card_image_lk = SiteObjects(
            "Окно в ЛК с персональным предложением",
            "//img[@class='offer-card-image']")

btn_offer_card_image_lk = SiteObjects(
            "Кнопка \"Ознакомился\" в окне с персональным предложением",
            "//button[@class='vz-button primary']//span")


"""Main Page (Header)"""

btn_choice_city = SiteObjects("Кнопка выбора города",
                              "(//span[@class='vz-button-title'])[1]")

text_choice_city = SiteObjects("Кнопка выбора города",
                               "//span[@title='Выберите ваш город']")

btn_close_choice_city = SiteObjects("Кнопка закрытия окна с выбором города",
                                    "//span[@class='mdi mdi-close']")

btn_choice_color_theme = SiteObjects("Кнопка выбора темы оформления",
                                     "//div[contains(@class, 'vz-color-mode vz-cursor-pointer')]")

attribute_choice_dark_theme = SiteObjects("Признак темной темы",
                                          "//html[@class='dark']")

btn_calculate_button = SiteObjects("Кнопка 'Рассчитать' в хедере",
                                   "(//span[contains(text(), 'Рассчитать')]//ancestor::a[@class='public-header-control-link'])[1]")

btn_track_button = SiteObjects("Кнопка 'Отследить' в хедере",
                               "(//span[contains(text(), 'Отследить')]//ancestor::a[contains(@class, 'public-header-control-link')])[1]")

text_track_page = SiteObjects("Текст 'Введите номер заказа' на странице 'Управление заказом'",
                              "//h2[contains(text(), 'Введите номер заказа')]")

btn_contacts_button = SiteObjects(
    "Кнопка 'Контакты' в хедере",
    "(//span[contains(text(), 'Контакты')]//ancestor::a[@href='/contacts/'])[1]")

text_contacts_page = SiteObjects(
    "Текст 'Контакты' на странице 'Контакты'",
    "//h1[contains(text(), 'Контакты')]")


"""Main Page (Menu)"""

btn_header_services = SiteObjects("Кнопка Услуги в верхнем меню",
                                  "//div[@class='public-header-menu-collapse-item']//a[contains(text(), 'Услуги')]")

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
                                    "//div[@class='public-header-menu-collapse-item']//a[@href='/cargo/' and contains(text(), 'Грузоперевозки')]")


btn_directions_in_cargo_transportation = SiteObjects("Кнопка Направления в Грузоперевозки",
                                    "//div[@class='public-header-menu-collapse-item-links']/a[@href='/directions/'][contains(text(), 'Направления')]")


text_on_directions = SiteObjects("Текст на странице Грузоперевозки",
                                 "//div[@class='directions-most-popular mt-60 mb-60']//h2[contains(text(), 'направления')]")

text_edo_edo = SiteObjects("Текст 'ЭДО' на странице Электронный документооборот",
                           "//div[contains(text(), 'Электронный документооборот (ЭДО)')]")

btn_header_info = SiteObjects("Кнопка Информация в хедере",
                              "//div[@class='public-header-menu-collapse-item']//a[@href='/information/'][contains(text(), 'Информация')]")

btn_header_info_docs = SiteObjects("Кнопка Документы в Информации в хедере",
                                   "(//a[@href='/documents/'])[1]")

text_header_info_docs = SiteObjects("Текст 'Документы' на странице 'Документы'",
                                    "//h2[contains(text(), 'ДОКУМЕНТЫ ООО «ВОЗОВОЗ»')]")

btn_header_info_help = SiteObjects("Кнопка 'Часто задаваемые вопросы' в Информации в хедере",
                                   "(//a[@href='/help/'])[1]")

text_on_info_help_page = SiteObjects("Текст 'Какие документы нужны' на странице 'Документы'",
                                     "//div[contains(@class, 'vz-switcher-item')]")

btn_header_tariffs = SiteObjects("Кнопка Тарифы в Информации в хедере",
                                 "(//a[@href='/tariffs/'])[1]")

text_on_tariffs_page = SiteObjects("Текст 'Какие документы нужны' на странице 'Документы'",
                                   "//h2[contains(text(), 'Укажите направление для расчета тарифов')]")

btn_header_run_schedule = SiteObjects("Кнопка 'Сроки доставки' в Информации в хедере",
                                      "(//a[@href='/run-schedule/'])[1]")

text_on_run_schedule_page = SiteObjects("Текст 'Расписание' на кнопке на странице 'Калькулятор сроков доставки'",
                                        "//span[contains(text(), 'Расписание рейсов')]")

btn_header_prohibited_goods = SiteObjects("Кнопка 'Грузы, не принимаемые к перевозке' в Информации в хедере",
                                          "(//a[@href='/prohibited-goods/'])[1]")

text_on_prohibited_goods_page = SiteObjects("Текст 'К перевозке не...' на странице 'Грузы не принимаемые к ...'",
                                            "//h2[contains(text(), 'К перевозке не принимаются следующие грузы')]")

btn_header_payment_methods = SiteObjects("Кнопка 'Способы оплаты' в Информации в хедере",
                                         "(//a[@href='/payment-methods/'])[1]")

text_on_payment_methods_page = SiteObjects("Текст 'Безналичный расчет' на странице 'Способы оплаты'",
                                           "//div[contains(text(), 'Безналичный расчёт')]")

btn_header_franchise = SiteObjects("Кнопка 'Франшиза' в Информации в хедере",
                                   "(//a[@href='/franchise/'])[1]")

text_on_franchise_page = SiteObjects("Текст 'Расписание' на странице 'Франшиза'",
                                     "//h2[contains(text(), 'Сотрудничество с Vozovoz')]")

btn_header_vacancy = SiteObjects("Кнопка 'Франшиза' в Информации в хедере",
                                 "(//a[@href='/vacancy/'])[1]")

text_on_vacancy_page = SiteObjects("Текст 'Нам требуются' на странице 'Вакансии'",
                                   "//h2[contains(text(), 'Нам требуются:')]")

btn_header_partners = SiteObjects("Кнопка 'Перевозчикам' в Информации в хедере",
                                  "(//a[@href='https://vozovoz.partners/'])[1]")

btn_header_develop = SiteObjects("Кнопка 'Разработчикам' в Информации в хедере",
                                 "(//a[@href='/information/#develop'])[1]")

text_on_develop_page = SiteObjects("Текст 'Разработчикам' на странице 'Информация'",
                                   "//h2[contains(text(), 'Разработчикам')]")

btn_header_geo = SiteObjects("Кнопка География",
                             "//a[@class='public-header-menu-item'][contains(text(), 'География')]")

input_geo_page = SiteObjects("Поле на странице География",
                             "(//input[@placeholder='Введите название города'])[1]")

# Кнопка "Частным лицам"

btn_private_person_page = SiteObjects("Кнопка 'Частным лицам' на главной странице",
                                      "//span[contains(text(), 'Частным лицам')]")

btn_address_delivery_main = SiteObjects("Кнопка 'Адресная доставка' на главной странице",
                                        "//a[@href='/address-delivery/'][contains(@class, 'home-info-card')]")

btn_cargo_loading_main = SiteObjects("Кнопка 'Погрузочные работы' на главной странице",
                                     "//a[@href='/cargo-loading/'][contains(@class, 'home-info-card')]")

btn_wrapping_main = SiteObjects("Кнопка 'Упаковка' на главной странице",
                                "//a[@href='/wrapping/'][contains(@class, 'home-info-card')]")

btn_payment_methods_main = SiteObjects("Кнопка 'Удобные способы оплаты' на главной странице",
                                       "//a[@href='/payment-methods/'][contains(@class, 'home-info-card')]")

# Кнопка "Бизнесу"

btn_business_page = SiteObjects("Кнопка 'Бизнесу>' на главной странице",
                                "//span[contains(text(), 'Бизнесу')]")

btn_networkshops_main = SiteObjects("Кнопка 'Доставка в маркетплейсы' на главной странице",
                                    "//a[@href='/networkshops/'][contains(@class, 'home-info-card')]")

btn_edo_main = SiteObjects("Кнопка 'ЭДО' на главной странице",
                           "//a[@href='/edo/'][contains(@class, 'home-info-card')]")

btn_insurance_main = SiteObjects("Кнопка 'Страховка' на главной странице",
                                 "//a[@href='/insurance/'][contains(@class, 'home-info-card')]")

btn_fast_delivery_capital_main = SiteObjects("Кнопка 'Быстрая доставка м/у городами' на главной странице",
                                             "//a[@href='/fast-delivery-capital/'][contains(@class, 'home-info-card')]")

btn_commercial_offer_main = SiteObjects("Коммерческое предложение на странице",
                                        "//button[@class='vz-button public-primary large home-info-primary-button vz-cursor-pointer']")

text_feedback_popup = SiteObjects("Текст 'Обратная связь в форме'",
                                  "//span[@title='Обратная связь']")

# Интернет-магазинам

btn_net_shops_main_page = SiteObjects("Кнопка 'Интернет-магазинам' на главной странице",
                                      "//span[contains(text(), 'Интернет-магазинам')]")

btn_delivery_russia_main = SiteObjects("Кнопка 'БГЗ' на главной странице",
                                       "//a[@href='/delivery-russia/'][contains(@class, 'home-info-card')]")

btn_guide_lk_main = SiteObjects("Кнопка 'Онлайн управление' на главной странице",
                                "//a[@href='/guide-lk/'][contains(@class, 'home-info-card')]")

text_guide_lk_main = SiteObjects("Текст 'Личный кабинет Возовоз' на guide_lk",
                                 "//b[contains(text(), 'Личный кабинет Vozovoz')]")

btn_cash_on_delivery_main = SiteObjects("Кнопка 'Наложенный платеж' на главной странице",
                                        "//a[@href='/cash-on-delivery/'][contains(@class, 'home-info-card')]")

text_cash_on_delivery_main = SiteObjects("Текст 'Наложенный платеж' на /cash-on-delivery/",
                                         "//h2[contains(text(), 'Наложенный платеж')]")

btn_safe_custody_main = SiteObjects("Кнопка 'Бесплатное хранение' на главной странице",
                                    "//a[@href='/safe-custody/'][contains(@class, 'home-info-card')]")

# Партнерам

btn_partners_main_page = SiteObjects("Кнопка 'Партнерам' на главной странице",
                                     "//span[contains(text(), 'Партнёрам')]")

btn_carrier_main_page = SiteObjects("Кнопка 'Перевозчикам' на Партнерах",
                                    "(//a[@href='https://vozovoz.partners/'])[3]")

btn_franchise_main = SiteObjects("Кнопка 'Франшиза' на главной странице",
                                 "//a[@href='/franchise/'][contains(@class, 'home-info-card')]")

btn_all_services_main = SiteObjects("Кнопка 'Все услуги' на главной странице",
                                    "//a[@href='/services/'][contains(@class, 'text-decoration-underline')]")

text_all_services_page = SiteObjects("Текст 'Основные направления' на главной странице",
                                     "//h2[contains(text(), ' Основные направления')]")


# Подвал страницы

btn_services_footer = SiteObjects("Кнопка 'Услуги' в подвале сайта",
                                  "//a[@href='/services/'][contains(@class, 'public-footer-menu-link')]")

btn_tariffs_footer = SiteObjects("Кнопка 'Тарифы' в подвале сайта",
                                 "//a[@href='/tariffs/'][contains(@class, 'public-footer-menu-link')]")

btn_vacancy_footer = SiteObjects("Кнопка 'Вакансии' в подвале сайта",
                                 "//a[@href='/vacancy/'][contains(@class, 'public-footer-menu-link')]")

btn_terminals_footer = SiteObjects("Кнопка 'География' в подвале сайта",
                                   "//a[@href='/terminals/'][contains(@class, 'public-footer-menu-link')]")

btn_directions_footer = SiteObjects("Кнопка 'Направления' в подвале сайта",
                                    "//a[@href='/directions/'][contains(@class, 'public-footer-menu-link')]")

btn_information_footer = SiteObjects("Кнопка 'Информация' в подвале сайта",
                                     "//a[@href='/information/'][contains(@class, 'public-footer-menu-link')]")

btn_documents_footer = SiteObjects("Кнопка 'Документы' в подвале сайта",
                                   "//a[@href='/documents/'][contains(@class, 'public-footer-menu-link')]")

btn_franchise_footer = SiteObjects("Кнопка 'Франшиза' в подвале сайта",
                                   "//a[@href='/franchise/'][contains(@class, 'public-footer-menu-link')]")

btn_partners_footer = SiteObjects("Кнопка 'Партнеры' в подвале сайта",
                                  "//a[@href='https://vozovoz.partners/'][contains(@class, 'public-footer-menu-link')]")

btn_develop_footer = SiteObjects("Кнопка 'Разработчикам' в подвале сайта",
                                 "//a[@href='/information/#develop'][contains(@class, 'public-footer-menu-link')]")

btn_contacts_footer = SiteObjects("Кнопка 'Разработчикам' в подвале сайта",
                                  "(//span[contains(@class, 'vz-button-title')][contains(text(), 'Контакты')])[3]")


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

atr_btn_from_terminal = SiteObjects("От терминала в мини калькуляторе",
                                    "//span[contains(text(), 'От терминала')]/..")

btn_from_address = SiteObjects("От адреса в мини калькуляторе",
                               "//span[@class='vz-radiogroup-item-title'][contains(text(), 'От адреса')]")

atr_btn_from_address = SiteObjects("От адреса в мини калькуляторе",
                                   "//span[contains(text(), 'От адреса')]/..")

btn_to_terminal = SiteObjects("До терминала в мини калькуляторе",
                              "//span[@class='vz-radiogroup-item-title'][contains(text(), 'До терминала')]")

atr_btn_to_terminal = SiteObjects("До терминала в мини калькуляторе",
                                  "//span[contains(text(), 'До терминала')]/..")

btn_to_address = SiteObjects("До адреса в мини калькуляторе",
                             "//span[@class='vz-radiogroup-item-title'][contains(text(), 'До адреса')]")

atr_btn_to_address = SiteObjects("До адреса в мини калькуляторе",
                                 "//span[contains(text(), 'До адреса')]/..")

btn_to_pvz = SiteObjects("До пункта выдачи в мини калькуляторе",
                         "//span[@class='vz-radiogroup-item-title'][contains(text(), 'До пункта')]")

atr_btn_to_pvz = SiteObjects("До пункта выдачи в мини калькуляторе",
                             "//span[contains(text(), 'До пункта')]/..")

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

delivery_time_mini_calc = SiteObjects("Ссылка со сроками доставки в мини-калькуляторе",
                                      "//a[@class='vz-calculator-price-title color-primary']")

btn_calculate_mini_calc = SiteObjects("Кнопка Рассчитать в мини-калькуляторе",
                                      "//a[@class='vz-button primary large vz-calculator-button']")

inp_track_mini_calc = SiteObjects("Поле для отслеживания номера заказа в мини-калькуляторе",
                                  "//input[@placeholder='Пример 240******']")

btn_track_mini_calc = SiteObjects("Поле для отслеживания номера заказа в мини-калькуляторе",
                                  "//button[@class='vz-button primary large vz-calculator-button']")

text_order_track = SiteObjects("Текст с номером введенного заказа в мини-калькуляторе",
                               f"//h2[contains(text(), 'Заказ №{order_mini_calc}')]")

error_toast_main_page = SiteObjects("Тоаст с ошибкой на главной",
                                    "//div[contains(@class, 'vz-toast show bottom error')]")

btn_toast_main_page = SiteObjects("Тоаст с ошибкой на главной",
                                    f"//span[contains(., 'Рассчитать')]/ancestor::a[contains(@class, 'vz-button primary large')]")

inp_weight_mini_calc = SiteObjects("Поле вес в мини-калькуляторе",
                                   "(//label[contains(text(),'Вес')]/..//input)[1]")


"""https://vozovoz.ru/order/manage/"""  # Страница отслеживания заказа

inp_number_of_order_manage_page = SiteObjects("Поле Введите номер заказа на странице отслеживания заказа",
                                                "//div[@class='vz-input-wrapper']//input")

btn_track_order_manage_page = SiteObjects("Кнопка Отследить на странице отслеживания заказа",
                                          "//button[@class='vz-button primary outline large mx-auto']")

txt_number_order_manage_page = SiteObjects("Номер заказа на странице отслеживания заказа",
                                           f"//div[@class='order-manage-info-card vz-position-relative']/h2[contains(text(), '{order_mini_calc}')]")

inp_number_of_phone_from_order_manage_page = SiteObjects("Поле для ввода номера из заказа",
                                                         "//input[@class='vz-mask vz-input-control large']")

btn_confirm_phone_manage_page = SiteObjects("Кнопка подтверждения номера телефона из заказа",
                                            "//button[@class='vz-button primary large mx-auto']")

txt_number_order_in_detailing_manage_page = SiteObjects("Номер заказа на странице детализации после отслеживания заказа",
                                                        f"//div[@class='vz-individual-order-header-label-wrapper']//span[contains(text(), '{order_mini_calc}')]")

txt_error_input_number_order_manage_page = SiteObjects("Ошибка валидации поля номера заказа на странице отслеживания",
                                                       "//div[@class='vz-invalid-message error']")

txt_error_input_confirm_phone_manage_page = SiteObjects("Ошибка валидации поля номера телефона на странице отслеживания",
                                                        "//div[@class='text-caption color-primary']")



"""Auction"""

input_login_auk = SiteObjects("поле логин аук",
                              "//input[@type='text']")

input_password_auk = SiteObjects("поле пароль аук",
                                 "//input[@type='password']")

btn_auth_auk = SiteObjects("Кнопка логин аук",
                           "//button[@type='button'][1]")

img_auth_auk = SiteObjects("Лого ЛК аук",
                           "//img[@src='/images/profile/user-profile.png']")

btn_menu_auction = SiteObjects("Кнопка ЛК аук",
                               "//a[@href='/auction']")

text_menu_auction = SiteObjects("Текст аукционы в ЛК аук",
                                "//h4[contains(text(), 'Аукционы')]")

btn_bid_auc = SiteObjects("Кнопка ставка в ауке",
                          "//span[@class='vs-button-text vs-button--text'][contains(text(), 'Ставка')]")

text_actual_bid = SiteObjects("Текст актуальной ставки в ауке",
                              "//td[@class='td vs-table--td'][9]/span/span")

text_actual_bid_count_auk = SiteObjects("Текст актуальной ставки в ауке",
                                        "//tr[contains(@class, 'tr-values vs-table--tr auction-data-column tr-table-state')][1]/td[@class='td vs-table--td'][9]/span/span")

text_bid_set = SiteObjects("Текст СТАВКА ПРИНЯТА в ауке",
                           "//div[@class='con-text-noti']/h3[contains(text(), 'Ставка принята')]")

text_bid_err = SiteObjects("Текст СТАВКА ПРИНЯТА в ауке",
                           "//div[@class='con-text-noti']//p[contains(text(), 'Ваша ставка')]")

input_bid_auc = SiteObjects("Поле ставка в модалке аука",
                            "//input[@type='number']")

btn_confirm_bid = SiteObjects("Кнопка подтвердить",
                              "//span[@class='vs-button-text vs-button--text'][contains(text(), 'Подтвердить')]")

text_price_bid_auk = SiteObjects("Текущая стоимость аука",
                                 "//td[@class='td vs-table--td'][9]/span/span")


"""Оформление заказа"""

btn_new_order = SiteObjects("Кнопка 'Оформить заказ'",
                            "//a[@href='/personal/order/create/']")

text_placing_an_order = SiteObjects("Текст 'Расчет и оформление заказа'",
                                    "//h1[contains(text(), 'Калькулятор доставки груза')]")

input_dispatch_city = SiteObjects("Инпут 'НП отправления' в создании заказа",
                                  "//div[contains(text(),'Отправка')]/ancestor::div[@class='vz-direction-card']/div[2]//input[@class='vz-input-control big']")

input_dispatch_address = SiteObjects("Инпут 'Адрес отправления' в создании заказа",
                                     "//div[contains(text(),'Отправка')]/../..//input[@placeholder='Улица, дом']")

list_input_dispatch = SiteObjects("Список нас.пунктов 'Отправка' создание заказа",
                                  "//div[contains(@class, 'vz-new-autocomplete-list vz-scroll')][1]")

btn_dispatch_address = SiteObjects("Кнопка 'Адрес' в отправке в создании заказа",
                                   "//div[contains(text(),'Отправка')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Адрес')]")

btn_dispatch_address_check_status = SiteObjects("Кнопка 'Адрес' в отправке в создании заказа",
                                   "//div[contains(text(),'Отправка')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Адрес')]/..")

btn_dispatch_terminal = SiteObjects("Кнопка 'Терминал' в отправке в создании заказа",
                                    "//div[contains(text(),'Отправка')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Терминал')]")

btn_dispatch_terminal_check_status = SiteObjects("Кнопка 'Терминал' для проверки включена или нет",
                                                 "//div[contains(text(),'Отправка')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Терминал')]/..")

input_destination_city = SiteObjects("Инпут 'НП прибытия' в создании заказа",
                                     "//div[contains(text(),'Прибытие')]/ancestor::div[@class='vz-direction-card']/div[1]//input[@class='vz-input-control big']")

input_destination_address = SiteObjects("Инпут 'Адрес прибытия' в создании заказа",
                                        "//div[contains(text(),'Прибытие')]/../..//input[@placeholder='Улица, дом']")

input_destination_pvz = SiteObjects("Инпут 'Пункт выдачи' в создании заказа",
                                        "//div[contains(text(),'Прибытие')]/../..//input[@placeholder='Введите улицу для поиска']")

btn_destination_address = SiteObjects("Кнопка 'Адрес' в прибытии в создании заказа",
                                      "//div[contains(text(),'Прибытие')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Адрес')]")

btn_destination_terminal = SiteObjects("Кнопка 'Терминал' в прибытии в создании заказа",
                                       "//div[contains(text(),'Прибытие')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Терминал')]")

btn_destination_terminal_check_status = SiteObjects("Кнопка 'Терминал' в прибытии в создании заказа",
                                                    "//div[contains(text(),'Прибытие')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Терминал')]/..")

btn_destination_address_check_status = SiteObjects("Кнопка 'Адрес' для проверки включена или нет",
                                                 "//div[contains(text(),'Прибытие')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Адрес')]/..")

btn_destination_pvz = SiteObjects("Кнопка 'Пункт выдачи' в прибытии в создании заказа",
                                  "//div[contains(text(),'Прибытие')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Пункт')]/..")

input_value_places = SiteObjects("Поле 'Места' в создании заказа",
                                 "//label[contains(text(),'Мест')]/..//input")

input_value_volume = SiteObjects("Поле 'Объем' в создании заказа",
                                 "//label[contains(text(),'Объем')]/..//input")

input_value_weight = SiteObjects("Поле 'Вес' в создании заказа",
                                 "(//span[contains(text(),'Вес')]/..//input)[1]")

btn_create_order = SiteObjects("Кнопка 'Оформить' в создании заказа",
                               "(//div[contains(@class,'vz-order-total-price')]//span[contains(.,'Оформить')]/parent::button)[1]")

btn_close_popup_rate_your_order = SiteObjects("Кнопка 'Закрыть' в попапе 'Оцените оформление заказа'",
                                              "//span[@title='Оцените оформление']/../span[@class='vz-close-btn close-btn']")

btn_cancel_in_toast = SiteObjects("Кнопка 'Не нужно' в тоасте при оформлении заказа",
                                  "//div[@class='vz-toast-button-wrapper']/button[1]")

btn_continue_in_toast = SiteObjects("Кнопка 'Продолжить' в тоасте при оформлении заказа",
                                    "//div[@class='vz-toast-button-wrapper']/button[2]")

active_city_in_input_from_field = SiteObjects("Город указанный в поле",
                                              "(//div[contains(@class, 'active')]/div[@class='vz-new-autocomplete"
                                              "-list-item-title'])[1]")

price_in_block_price = SiteObjects("Город указанный в поле",
                                   "(//span[@class='flex flex-align-items-center flex-nowrap'])[1]")


""" Детализация заказа"""

text_number_order_after_create = SiteObjects(
    "Номер заказа в детализации заказа",
    "//span[contains(text(), 'Заказ №')]")


""" Участники перевозки (Физ.лицо)"""

# Отправитель физ.лицо
btn_type_ind_sender = SiteObjects("Кнопка 'Физ.лицо' у отправителя",
                                  "//span[text()='Отправитель']/../..//span[contains(text(),'Физическое лицо')]/..")

input_fio_ind_sender = SiteObjects("Поле ФИО у отправителя физ.лицо",
                                   "//span[text()='Отправитель']/../..//label[contains(text(),'ФИО')]/..//input")

input_phone_ind_sender = SiteObjects("Поле Телефон у отправителя физ.лицо",
                                     "//span[text()='Отправитель']/../..//label[contains(text(),'Телефон')]/..//input")

input_add_phone_ind_sender = SiteObjects("Кнопка доп. телефон у отправителя физ.лицо",
                                         "//span[text()='Отправитель']/../..//label[contains(text(),'+ Доп. номер')]")

input_email_ind_sender = SiteObjects("Поле email у отправителя физ.лицо",
                                     "//span[text()='Отправитель']/../..//label[contains(text(),'Email')]/..//input")

checkbox_send_code_ind_sender = SiteObjects("Поле email у отправителя физ.лицо",
                                            "//span[text()='Отправитель']/../..//span[contains(text(),'Отправить код получения')]/preceding-sibling::div")

list_fio_ka_sender = SiteObjects("Список всех КА",
                                 "//span[text()='Отправитель']/../..//label[contains(text(),'Телефон')]/..//input")


# Получатель физ.лицо
btn_type_ind_recipient = SiteObjects("Кнопка 'Физ.лицо' у получателя",
                                     "//span[text()='Получатель']/../..//span[contains(text(),'Физическое лицо')]/..")

input_fio_ind_recipient = SiteObjects("Поле ФИО у отправителя физ.лицо",
                                      "//span[text()='Получатель']/../..//label[contains(text(),'ФИО')]/..//input")

input_phone_ind_recipient = SiteObjects("Поле Телефон у отправителя физ.лицо",
                                        "//span[text()='Получатель']/../..//label[contains(text(),'Телефон')]/..//input")

input_add_phone_ind_recipient = SiteObjects("Кнопка доп. телефон у отправителя физ.лицо",
                                            "//span[text()='Получатель']/../..//label[contains(text(),'+ Доп. номер')]")

input_email_ind_recipient = SiteObjects("Поле email у отправителя физ.лицо",
                                        "//span[text()='Получатель']/../..//label[contains(text(),'Email')]/..//input")

checkbox_send_code_ind_recipient = SiteObjects("Поле email у отправителя физ.лицо",
                                               "//span[text()='Получатель']/../..//span[contains(text(),'Отправить код получения')]/preceding-sibling::div")

# Отправитель юр.лицо
btn_type_corp = SiteObjects("Кнопка 'Юр.лицо' у отправителя",
                            "//span[text()='Отправитель']/../..//span[contains(text(),'Юридическое лицо')]/..")

btn_type_corp_recipient = SiteObjects("Кнопка 'Юр.лицо' у отправителя",
                            "//span[text()='Получатель']/../..//span[contains(text(),'Юридическое лицо')]/..")

input_name_corp = SiteObjects("Инпут 'Наименование компании' у отправителя юр.лица",
                              "//span[text()='Отправитель']/../..//label[contains(text(),'Наименование компании')]/..//input")

input_name_corp_recipient = SiteObjects("Инпут 'Наименование компании' у отправителя юр.лица",
                              "//span[text()='Получатель']/../..//label[contains(text(),'Наименование компании')]/..//input")

input_phone_corp = SiteObjects("Поле Телефон у отправителя юр.лицо",
                               "//span[text()='Отправитель']/../..//label[contains(text(),'Телефон')]/..//input")

input_additional_phone_corp = SiteObjects(
    "Кнопка доп. телефон у отправителя юр.лицо",
    "//span[text()='Отправитель']/../..//label[contains(text(),'+ Доп. номер')]")

"""Страница Контрагенты"""

btn_top_up_account_counteragent = SiteObjects("Кнопка 'Пополнить счет' у контрагента",
                                              "(//button[@class='vz-button primary'])[1]")

btn_top_up_in_modal_counteragent = SiteObjects("Кнопка 'Пополнить счет' у контрагента",
                                               "//span[text()=' Пополнить ']/..")


