from flask import Blueprint, render_template

from stocks_website.exchanges import get_stock_exchanges

stocks_routes = Blueprint('stocks', __name__, 'tamplates/')

@stocks_routes.route('/exchanges/<exchange>')
def exchanges(exchange):
    stocks_exchanges = get_stock_exchanges()
    return render_template('exchanges.html', stocks_exchanges=stocks_exchanges)


