from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


# date display

# @app.route('/')
# def date_today():
#     date = datetime.now()
#     html = f"<h1>{date}</h1>"
#     return html


# site I found online to help understand importing css

# @app.route('/')
# def home():
#     return render_template('home.html')
#
# @app.route('/about/')
# def about():
#     return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
