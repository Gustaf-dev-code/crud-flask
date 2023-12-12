from flask import Flask
from config import config
from scr.route import route_attention_control

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])  # configuracion del proyecto

    # Blueprint
    app.register_blueprint(route_attention_control.main, url_prefix='/')  # registrar el blueprint

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()