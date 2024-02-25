from flask import Flask

from config import Config
from routes.card_front import card_front_blueprint
from routes.card_back import card_back_blueprint

app = Flask(__name__)
app.config.from_object(Config)
# Register blueprints
app.register_blueprint(card_front_blueprint, url_prefix='/api')
app.register_blueprint(card_back_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
