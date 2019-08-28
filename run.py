from flask import Flask
from view import view

app = Flask(__name__)
app.register_blueprint(view, url_prefix='/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=520, debug=True)
