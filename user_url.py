from flask import Blueprint, request, Response
from .activity_facade import ActivityFacade

user_bp = Blueprint('user', __name__)
facade = ActivityFacade()

@user_bp.route('/deploy-atividade', methods=['GET'])
def deploy_activity():
    invenira_instance_id = request.args.get('invenira_instance_id')
    activity_type = request.args.get('activity_type')

    if not all([invenira_instance_id, activity_type]):
        return Response("Erro: parâmetros em falta.", status=400)

    try:
        deployment_url = facade.get_deployment_url(
            activity_type,
            invenira_instance_id,
            request.host_url
        )
        return Response(deployment_url, mimetype='text/plain')
    except ValueError as e:
        return Response(str(e), status=404)
