import requests
from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__, 'tamplates/')

@main_routes.route('/')
def index():
    stocks_exchanges = requests.get('https://api.worldtradingdata.com/api/v1/exchange_list', {'api_token':
                                                                                                  'QJNaynFfHPUvjBbWoM9OwmbYynLvEvDIykOhBf3sjhLcO0HqK7fBxcdBgu8H'})
    return render_template('index.html', stocks_exchanges=stocks_exchanges.json())
