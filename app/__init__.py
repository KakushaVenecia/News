from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

app = Flask(__name__)

def create_app(config_name):
   

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    

    # Initializing flask extensions
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # Setting config 
    from .requests import configure_request
    configure_request(app)

    return app