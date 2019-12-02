from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__, 'tamplates/')

@main_routes.route('/')
def index():
    return render_template('index.html', name="Eitan")
