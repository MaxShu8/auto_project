from Settings import *
from dadata import Dadata

token_dadata = "84beb76a98914195f374779f2f313d31efca3c5d"
secret = "cb82deee2d367b967ba569b5fc11b9e21a8c4832"
dadata = Dadata(token_dadata, secret)
result_statistic_dadata = dadata.get_daily_stats()

path = "E:\\Vozovoz\\AutoPtoject"  # Нужно для вызова из планировщика заданий windows, т.к. оттуда выбирается дефолтная папка
os.chdir(path)

#  {'date': '2024-10-31', 'services': {'clean': 155, 'company': 0, 'company_similar': 0, 'merging': 0, 'suggestions': 31961}, 'remaining': {'clean': 73821, 'company': 50, 'company_similar': 2214, 'merging': 1107325, 'suggestions': 169476}}

# Вытащим данные из ответа
date = result_statistic_dadata['date']

clean_ser = result_statistic_dadata['services']['clean']
company_ser = result_statistic_dadata['services']['company']
company_similar_ser = result_statistic_dadata['services']['company_similar']
merging_ser = result_statistic_dadata['services']['merging']
suggestions_ser = result_statistic_dadata['services']['suggestions']

clean_rem = result_statistic_dadata['remaining']['clean']
company_rem = result_statistic_dadata['remaining']['company']
company_similar_rem = result_statistic_dadata['remaining']['company_similar']
merging_rem = result_statistic_dadata['remaining']['merging']
suggestions_rem = result_statistic_dadata['remaining']['suggestions']

if suggestions_ser >= 150000:
    msg_date = f"🔔 Превышено кол-во подсказок по Dadata\nНа дату {date}:\n"
    msg_services = f"\nИзрасходовано:\n1️⃣ стандартизация - {clean_ser}\n2️⃣ компания по email - {company_ser}\n3️⃣ поиск дублей - {merging_ser}\n4️⃣ подсказки - {suggestions_ser} ❗\n"
    msg_remaining = f"\nОстаток:\n1️⃣ стандартизация - {clean_rem}\n2️⃣ компания по email - {company_rem}\n3️⃣ поиск дублей - {merging_rem}\n4️⃣ подсказки - {suggestions_rem} ❗"

    message = msg_date + msg_services + msg_remaining
    send_message_tg(message, token_vozovoz_bot, chat_id_prod)
else:
    pass

with open('logs/logs_dadata.txt', 'a') as f:
    date_today = datetime.datetime.today()
    data_to_log = str(date_today) + " " + str(result_statistic_dadata)
    f.write(f"{data_to_log}\n")


