# Arquivo: json_params_url.py
from flask import Blueprint, jsonify

# Cria um módulo para esta rota
json_params_bp = Blueprint('json_params', __name__)

@json_params_bp.route('/json-params-atividade', methods=['GET'])
def get_json_params():
    """
    Retorna os parâmetros para o formulário da Inven!RA.
    """
    params = [
        {"name": "resumo", "type": "text/plain"},
        {"name": "instrucoes", "type": "text/plain"},
        {"name": "versao_ap", "type": "text/plain"}
    ]
    return jsonify(params)