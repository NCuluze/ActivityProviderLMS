# Arquivo: app.py
from flask import Flask

# Importar os Blueprints (módulos) dos outros ficheiros
from json_params_url import json_params_bp
from config_url import config_bp
from user_url import user_bp
from analytics_list_url import analytics_list_bp
from analytics_url import analytics_bp

app = Flask(__name__)

# Registar as rotas
app.register_blueprint(json_params_bp)
app.register_blueprint(config_bp)
app.register_blueprint(user_bp)
app.register_blueprint(analytics_list_bp)
app.register_blueprint(analytics_bp)

if __name__ == '__main__':
    print("Servidor Activity Provider a correr na porta 5000...")
    app.run(debug=True, port=5000)