import time
import Settings
from Business_Actions import check_try
from Methods import *
from Settings import *
from pages.documents_page import *
from pages.payment_page import *


def driver_start_monitoring():
    driver = None

    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--headless')

        prefs = {"download.default_directory": f"{os.getcwd()}\\downloads"}

        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=chrome_options)

        driver.implicitly_wait(5)

    except Exception as e:
        err = f"\nОшибка при установке драйвера:"
        send_message_tg(f'{err}\nПроизошла ошибка в тесте\n{e}', token, chat_id)

    return driver


"""Проверка скачивания файлов на странице \"Документы\""""
# def check_downloads_documents():
#
#     description = "Проверка скачивания файлов на странице документы"
#     send_message_tg(f"🔔 {description}", token, chat_id)
#     links = [file_1_on_documents_page.xpath, file_2_on_documents_page.xpath, file_3_on_documents_page.xpath,
#              file_4_on_documents_page.xpath, file_5_on_documents_page.xpath, file_6_on_documents_page.xpath,
#              file_7_on_documents_page.xpath, file_8_on_documents_page.xpath, file_9_on_documents_page.xpath,
#              file_10_on_documents_page.xpath, file_11_on_documents_page.xpath, file_12_on_documents_page.xpath,
#              file_13_on_documents_page.xpath, file_14_on_documents_page.xpath, file_15_on_documents_page.xpath,
#              file_16_on_documents_page.xpath, file_17_on_documents_page.xpath, file_18_on_documents_page.xpath,
#              file_19_on_documents_page.xpath, file_20_on_documents_page.xpath, file_21_on_documents_page.xpath,
#              file_22_on_documents_page.xpath, file_23_on_documents_page.xpath, file_24_on_documents_page.xpath,
#              file_25_on_documents_page.xpath, file_26_on_documents_page.xpath, file_27_on_documents_page.xpath,
#              file_28_on_documents_page.xpath, file_29_on_documents_page.xpath, file_30_on_documents_page.xpath,
#              file_31_on_documents_page.xpath, file_32_on_documents_page.xpath, file_33_on_documents_page.xpath,
#              file_34_on_documents_page.xpath, file_35_on_documents_page.xpath, file_36_on_documents_page.xpath,
#              file_37_on_documents_page.xpath, file_38_on_documents_page.xpath, file_39_on_documents_page.xpath,
#              file_40_on_documents_page.xpath, file_41_on_documents_page.xpath, file_42_on_documents_page.xpath,
#              file_43_on_documents_page.xpath, file_44_on_documents_page.xpath, file_45_on_documents_page.xpath,
#              file_46_on_documents_page.xpath, file_47_on_documents_page.xpath, file_48_on_documents_page.xpath]
#
#     set_page(driver, url_documents_ru)
#     wait_page(driver, url_documents_ru)
#
#     WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, elem_on_documents_page.xpath)))
#     elem_text = ''
#     current_file = ''
#
#     try:
#         for el in links:
#             elem_href = driver.find_element(By.XPATH, el).get_attribute("href")  # Достанем ссылку
#             elem_text = driver.find_element(By.XPATH, el).get_attribute("text")  # Достанем наименование договора
#             driver.get(elem_href)
#
#             time.sleep(2)  # Установим доп время для загрузки файла
#
#             # Получим список файлов в директории "files_for_tsts"
#             listdir = os.listdir(f"{os.getcwd()}\\files_for_tsts")
#             current_file = listdir[0]
#
#             if elem_text in current_file or 'Реквизиты ООО _Возовоз_' in current_file:
#                 os.remove(f"{os.getcwd()}\\files_for_tsts\\{current_file}")
#                 time.sleep(1)
#                 pass
#             else:
#                 # Попробуем подождать и снова посмотреть в папку
#                 time.sleep(10)
#                 listdir = os.listdir(f"{os.getcwd()}\\files_for_tsts")
#                 current_file = listdir[0]
#                 if elem_text in current_file:
#                     os.remove(f"{os.getcwd()}\\files_for_tsts\\{current_file}")
#                 else:
#                     send_message_tg(f"{description}\nФайл не загружен: \"{elem_text}\"", token, chat_id)
#                 continue
#
#     except Exception as e:
#         send_message_tg(f"{description}\nЧто-то пошло не так {e}", token, chat_id)
#         pass
#
#     finally:
#         driver.close(), driver.quit()

# check_downloads_documents()


"""Проверка доступности файлов на странице \"Документы\" на сайте Vozovoz"""
def checking_file_availability_on_vozovoz(driver):
    description = "Проверка файлов на странице \"Документы\" (PROD)"
    counter_success = 0
    unavailable = 0

    send_message_tg(f"🔔 {description}", token, chat_id)

    try:
        set_page(driver, url_documents_ru)
        wait_page(driver, url_documents_ru)

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, elem_on_documents_page.xpath)))

        # Достанем все элементы со ссылками из блока документов
        documents = driver.find_elements(By.XPATH, "//div[@class='vz-docs-tree-item documents-tree']//a")

        for element in documents:
            elem_href = element.get_attribute("href")  # Достанем ссылку
            # elem_text = element.text  # текст не достает почему-то...

            try:
                response = requests.get(elem_href)
                headers = response.headers  # {'Server': 'QRATOR', 'Date': 'Wed, 14 Aug 2024 11:27:57 GMT', 'Content-Type': 'application/pdf', 'Content-Length': '1364111', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=15', 'pragma': 'public', 'accept-ranges': 'bytes', 'expires': '0', 'cache-control': 'must-revalidate, post-check=0, pre-check=0', 'content-disposition': 'attachment; filename="Ð\x94Ð¾Ð³Ð¾Ð²Ð¾Ñ\x80 Ð½Ð° Ð¾ÐºÐ°Ð·Ð°Ð½Ð¸Ðµ Ñ\x82Ñ\x80Ð°Ð½Ñ\x81Ð¿Ð¾Ñ\x80Ñ\x82Ð½Ð¾-Ñ\x8dÐºÑ\x81Ð¿ÐµÐ´Ð¸Ñ\x86Ð¸Ð¾Ð½Ð½Ñ\x8bÑ\x85 Ñ\x83Ñ\x81Ð»Ñ\x83Ð³.pdf"; filename*=utf-8\'\'%D0%94%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%20%D0%BD%D0%B0%20%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%BE-%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D1%85%20%D1%83%D1%81%D0%BB%D1%83%D0%B3.pdf', 'strict-transport-security': 'max-age=31536000; includeSubDomains; preload', 'x-frame-options': 'ALLOWALL', 'x-xss-protection': '1; mode=block', 'host': 'vozovoz.ru', 'x-content-type-options': 'nosniff', 'referrer-policy': 'origin-when-cross-origin', 'x-served-by': 'vozovoz.ru', 'set-cookie': 'ycsessionback="600b1b21a933fc55"; HttpOnly'}
                if response.status_code == 200:
                    counter_success += 1
                    continue
                else:
                    send_message_tg(f"Документы на \"Возовоз\"\n🔴 Ошибка: {response.status_code}\nСсылка на файл: \"{elem_href}\" - недоступен", token_vozovoz_bot, group_id_predprod)
                    # send_message_tg(f"Документы на \"Возовоз\"\n🔴 Ошибка: {response.status_code}\nСсылка на файл: \"{elem_href}\" - недоступен", token, chat_id_predprod)
                    unavailable += 1
                    continue

            except Exception:
                print(f"Что-то пошло не так с запросом доступа файла:\n\"{elem_href}\"\n Попробуем снова...")
                try:
                    response = requests.get(elem_href)
                    if response.status_code == 200:
                        counter_success += 1
                        continue
                    else:
                        send_message_tg(f"Документы на \"Возовоз\"\n🔴 Ошибка: {response.status_code}\nСсылка на файл: \"{elem_href}\" - недоступен", token_vozovoz_bot, group_id_predprod)
                        # send_message_tg(f"Документы на \"Возовоз\"\n🔴 Ошибка: {response.status_code}\nСсылка на файл: \"{elem_href}\" - недоступен", token, chat_id_predprod)
                        unavailable += 1
                        continue

                except Exception:
                    send_message_tg(f"Что-то пошло не так с запросом доступа файла:\n\"{elem_href}\"\n", token, chat_id)
                    continue

    except Exception as e:
        send_message_tg(f"Скрипт не запустился:\n{e}", token, chat_id)

    finally:
        print(f"Кол-во обработанных файлов на Vozovoz: {counter_success}")
        if unavailable == 0:
            check_try(1, 0, 0)
        else:
            check_try(0, 1, 0)
        driver.close(), driver.quit()


"""Проверка доступности файлов на странице \"Документы\" на сайтах партнеров"""
def checking_file_availability_on_partners(driver):
    description = "Проверка доступности файлов на сайтах партнеров (Partners)"
    counter_success_partners = 0
    unavailable_partners = 0

    sites_companies = [url_timelogistik, url_diligans, url_t_technology, url_severtrans, url_ugtrans, url_logtavrii]

    send_message_tg(f"🔔 {description}", token, chat_id)

    try:
        for site in sites_companies:

            set_page(driver, site)
            wait_page(driver, site)

            # WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, text_name_company_on_documents_page.xpath)))
            elem_text = ""
            elem_href = ""

            if site is not url_logtavrii:
                link_doc = driver.find_element(By.XPATH, "//iframe").get_attribute("src")  # Получим ссылку страницы доков на Апексе для текущего сайта
                set_page(driver, link_doc)
                wait_page(driver, link_doc)

            # Достанем все элементы со ссылками из блока документов
            documents = driver.find_elements(By.XPATH, "//div[@class='vz-docs-tree-item documents-tree']//a")

            # WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, elem_on_documents_page.xpath)))

            for element in documents:

                elem_href = element.get_attribute("href")  # Достанем ссылку
                # elem_text = element.text  # текст не достает почему-то...
                try:
                    response = requests.get(elem_href)
                    headers = response.headers  # {'Server': 'QRATOR', 'Date': 'Wed, 14 Aug 2024 11:27:57 GMT', 'Content-Type': 'application/pdf', 'Content-Length': '1364111', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=15', 'pragma': 'public', 'accept-ranges': 'bytes', 'expires': '0', 'cache-control': 'must-revalidate, post-check=0, pre-check=0', 'content-disposition': 'attachment; filename="Ð\x94Ð¾Ð³Ð¾Ð²Ð¾Ñ\x80 Ð½Ð° Ð¾ÐºÐ°Ð·Ð°Ð½Ð¸Ðµ Ñ\x82Ñ\x80Ð°Ð½Ñ\x81Ð¿Ð¾Ñ\x80Ñ\x82Ð½Ð¾-Ñ\x8dÐºÑ\x81Ð¿ÐµÐ´Ð¸Ñ\x86Ð¸Ð¾Ð½Ð½Ñ\x8bÑ\x85 Ñ\x83Ñ\x81Ð»Ñ\x83Ð³.pdf"; filename*=utf-8\'\'%D0%94%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%20%D0%BD%D0%B0%20%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%BE-%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D1%85%20%D1%83%D1%81%D0%BB%D1%83%D0%B3.pdf', 'strict-transport-security': 'max-age=31536000; includeSubDomains; preload', 'x-frame-options': 'ALLOWALL', 'x-xss-protection': '1; mode=block', 'host': 'vozovoz.ru', 'x-content-type-options': 'nosniff', 'referrer-policy': 'origin-when-cross-origin', 'x-served-by': 'vozovoz.ru', 'set-cookie': 'ycsessionback="600b1b21a933fc55"; HttpOnly'}
                    if response.status_code == 200:
                        counter_success_partners += 1
                        continue
                    else:
                        send_message_tg(f"Документы на \"Возовоз\"\n🔴 Ошибка: {response.status_code}\nСсылка на файл: \"{elem_href}\" - недоступен", token_vozovoz_bot, group_id_predprod)
                        # send_message_tg(f"Документы на \"Возовоз\"\n🔴 Ошибка: {response.status_code}\nСсылка на файл: \"{elem_href}\" - недоступен", token, chat_id_predprod)
                        unavailable_partners += 1
                        continue

                except Exception:
                    print(f"Что-то пошло не так с запросом доступа файла:\n\"{elem_href}\"\n Попробуем снова...")
                    try:
                        response = requests.get(elem_href)
                        if response.status_code == 200:
                            counter_success_partners += 1
                            continue
                        else:
                            send_message_tg(f"Документы на \"Возовоз\"\n🔴 Ошибка: {response.status_code}\nСсылка на файл: \"{elem_href}\" - недоступен", token_vozovoz_bot, group_id_predprod)
                            # send_message_tg(f"Документы на \"Возовоз\"\n🔴 Ошибка: {response.status_code}\nСсылка на файл: \"{elem_href}\" - недоступен", token, chat_id_predprod)
                            unavailable_partners += 1
                            continue

                    except Exception:
                        send_message_tg(f"Что-то пошло не так с запросом доступа файла:\n\"{elem_href}\"\n", token, chat_id)
                        continue

    except Exception as e:
        send_message_tg(f"Скрипт не запустился:\n{e}", token, chat_id)

    finally:
        print(f"Кол-во обработанных файлов у партнеров: {counter_success_partners}")
        if unavailable_partners == 0:
            check_try(1, 0, 1)
        else:
            check_try(0, 1, 1)
        driver.close(), driver.quit()

def main_monitoring_func():
    time_now = datetime.datetime.now()
    current_time_hour = time_now.hour

    checking_file_availability_on_vozovoz(driver_start_monitoring())

    if current_time_hour == 14:
        checking_file_availability_on_partners(driver_start_monitoring())


main_monitoring_func()
