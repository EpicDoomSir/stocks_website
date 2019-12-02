import requests


def get_stock_exchanges():
    stocks_exchanges_response = requests.get('https://api.worldtradingdata.com/api/v1/exchange_list', {'api_token':
                                                                                                           'QJNaynFfHPUvjBbWoM9OwmbYynLvEvDIykOhBf3sjhLcO0HqK7fBxcdBgu8H'})
    stocks_exchanges_response.raise_for_status()
    stocks_exchanges = stocks_exchanges_response.json()
    if 'message' in stocks_exchanges:
        raise ValueError(stocks_exchanges['message'])
    return stocks_exchanges