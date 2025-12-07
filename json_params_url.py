
from flask import Blueprint, jsonify, request
# Importar a função auxiliar da Fábrica de Criadores
from .activity_factory import get_creator_by_type 

json_params_bp = Blueprint('json_params', __name__)

@json_params_bp.route('/json-params-atividade', methods=['GET'])
def get_json_params():
    """
    Retorna os parâmetros usando o Factory Method.
    O tipo é especificado pelo parâmetro de query '?type=...'.
    """
    activity_type = request.args.get('type')
    if not activity_type:
        return jsonify({"error": "Parâmetro 'type' da atividade em falta."}), 400

    try:
        # 1. Obter o Criador (Fábrica) com base no tipo
        CreatorClass = get_creator_by_type(activity_type)
        creator = CreatorClass()
        
        # 2. Usar o Factory Method para criar o Produto e obter os dados
        activity_instance = creator.get_activity_product()
        params = activity_instance.get_json_params()

        return jsonify(params)

    except ValueError as e:
        return jsonify({"error": str(e)}), 404