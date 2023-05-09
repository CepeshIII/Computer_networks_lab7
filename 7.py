import json
import requests

# Ключ API сайту
API_KEY = '47c1b07c64be40e48263883f9712c180'

# Ввід даних з клавіатури
date = input('Введіть дату в форматі YYYY-MM-DD: ')
from_currency = input('Введіть код валюти, з якої переводити: ').upper()
to_currency = input('Введіть код валюти, в яку переводити: ').upper()

# Створення запиту до API
url = f'https://openexchangerates.org/api/historical/{date}.json?app_id={API_KEY}'
response = requests.get(url)

# Перетворення отриманої відповіді в об'єкт Python
data = json.loads(response.text)

# Отримання потрібних даних з об'єкту
conversion_rate = data['rates'][to_currency] / data['rates'][from_currency]

# Виведення результатів в консоль
print(f"Курс конвертації з {from_currency} в {to_currency} на {date}: {conversion_rate}")