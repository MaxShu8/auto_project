import datetime
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from Telegram import send_message_tg


# Monitoring partners

def driver_start():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver


def partners_sites(driver):
    # Список пар (URL-адрес, XPATH для поиска элемента)
    sites = [
        ('https://severtrans-spb.ru/', '//span[text()="Севертранс грузоперевозки по Северо-Западу"]'),
        ('https://ugtrans-tk.ru/', '//span[text()="ЮГТранс ТЭК"]'),
        ('https://tcdiligans.ru/', '//span[contains(text(),"Транспортная компания Дилижанс")]'),
        ('https://t-technology.ru/', '//span[contains(text(),"ТРАНСПОРТНЫЕ ТЕХНОЛОГИИ")]'),
        ('https://vzln.ru/', '//h1[text() = "404 Not Found"]')
    ]

    try:
        # Итерация по парам (URL-адрес, XPATH)
        for url, xpath in sites:
            # Открытие сайта в Chrome
            driver.get(url)
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, xpath)))

            # Поиск элемента
            element_site = driver.find_element(By.XPATH, xpath)

            msg = f"Element on {url} in Chrome: {element_site.text}"
            send_message_tg(msg)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.close()
        driver.quit()


def authorization_for_partners(driver):

    url = "https://vozovoz.partners/login"
    try:
        driver.get(url)

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@name='телефон']")))
        vozovoz_partners_phone = driver.find_element(By.XPATH, "//input[@name='телефон']")
        vozovoz_partners_phone.send_keys("79112713186")

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@name='пароль']")))
        vozovoz_partners_password = driver.find_element(By.XPATH, "//input[@name='пароль']")
        vozovoz_partners_password.send_keys("qwerty01")

        btn_vozovoz_partners_auth = driver.find_element(By.XPATH, "//span[text()='Авторизоваться']/ancestor::button")
        btn_vozovoz_partners_auth.click()

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//p[contains(text(),'АЛЬБУС')]")))
        response = requests.get('https://vozovoz.partners/dashboard')

        if response.status_code != 200:
            print('Error:', response.reason)

        msg = f"Element on {url} in Chrome: {vozovoz_partners_phone.text}"
        send_message_tg(msg)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.close()
        driver.quit()


partners_sites(driver_start())
