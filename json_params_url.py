# json_params_url.py
from flask import Blueprint, jsonify, request
from .activity_facade import ActivityFacade

json_params_bp = Blueprint('json_params', __name__)
facade = ActivityFacade()

@json_params_bp.route('/json-params-atividade', methods=['GET'])
def get_json_params():
    activity_type = request.args.get('type')
    if not activity_type:
        return jsonify({"error": "Parâmetro 'type' em falta."}), 400

    try:
        params = facade.get_json_params(activity_type)
        return jsonify(params)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
