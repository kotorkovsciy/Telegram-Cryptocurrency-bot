from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from create_bot import TOKEN_CRYPTO

class CryptoCurrency:
    # Получаем данные
    def getCurrentPrice(symbol, valute):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
        "symbol": symbol,
        'convert': valute
        }
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': TOKEN_CRYPTO,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e