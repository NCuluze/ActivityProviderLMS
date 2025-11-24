# Arquivo: analytics_list_url.py
from flask import Blueprint, jsonify

analytics_list_bp = Blueprint('analytics_list', __name__)

@analytics_list_bp.route('/lista-analytics-atividade', methods=['GET'])
def get_analytics_list():
    """
    Lista os metadados dos analytics disponíveis.
    """
    analytics_list = {
        "qualAnalytics": [
            {"name": "Student activity profile", "type": "URL"},
            {"name": "Actitivy Heat Map", "type": "URL"}
        ],
        "quantAnalytics": [
            {"name": "Acedeu à atividade", "type": "boolean"},
            {"name": "Download documento 1", "type": "boolean"},
            {"name": "Evolução pela atividade ()", "type": "string"}
        ]
    }
    return jsonify(analytics_list)