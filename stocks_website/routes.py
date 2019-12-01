from flask import Blueprint

main_routes = Blueprint('main', __name__, 'tamplates/')

@main_routes.route('/')
def index():
    return 'Hi'
