# Arquivo: analytics_url.py
from flask import Blueprint, request, jsonify

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics-atividade', methods=['POST'])
def get_analytics_data():
    """
    Retorna os dados de analytics para uma activityID específica.
    """
    data = request.get_json()
    activity_id = data.get('activityID') if data else None

    if activity_id:
        # Simulação de resposta da Base de Dados
        analytics_response = [
            {
                "inveniraStdID": "1001",
                "quantAnalytics": [
                    {"name": "Acedeu à atividade", "value": True},
                    {"name": "Download documento 1", "value": True},
                    {"name": "Evolução pela atividade ()", "value": "33.3"}
                ],
                "qualAnalytics": {
                    "Student activity profile": f"{request.host_url}?APAnID=11111111",
                    "Actitivy Heat Map": f"{request.host_url}?APAnID=21111111"
                }
            }
        ]
        return jsonify(analytics_response)
    else:
        return jsonify({"error": "activityID em falta."}), 400