from flask import Flask
from config import config
from scr.route import route_attention_control


app = Flask(__name__) #instancia de flask

#configuracion del proyecto (FLASK)

if __name__ == '__main__':
    app.config.from_object(config['development']) #configuracion del proyecto
    #Blueprint
    app.register_blueprint(route_attention_control.main, url_prefix='/') #registrar el blueprint
    app.run() #ejecutar el servidor