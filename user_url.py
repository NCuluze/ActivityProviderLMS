# Arquivo: user_url.py

from flask import Blueprint, request, Response
from .activity_factory import get_creator_by_type 

user_bp = Blueprint('user', __name__)

@user_bp.route('/deploy-atividade', methods=['GET'])
def deploy_activity():
    """
    Gera o URL final para o estudante com base no ID da instância e Tipo.
    """
    invenira_instance_id = request.args.get('invenira_instance_id')
    activity_type = request.args.get('activity_type') # Novo parâmetro essencial

    if not all([invenira_instance_id, activity_type]):
        return Response("Erro: IDs ou Tipo da atividade em falta.", status=400, mimetype='text/plain')

    try:
        # 1. Obter o Criador e a Atividade
        CreatorClass = get_creator_by_type(activity_type)
        creator = CreatorClass()
        activity_instance = creator.get_activity_product() # Factory Method
        
        # 2. Chamar o método específico da instância de Atividade
        deployment_url = activity_instance.get_deployment_url(
            invenira_instance_id,
            request.host_url
        )
        
        return Response(deployment_url, mimetype='text/plain')
    except ValueError as e:
        return Response(f"Erro: {str(e)}", status=404, mimetype='text/plain')

# Novas rotas que agora são implementadas pelas Atividades Concretas
@user_bp.route('/phishing_simulacao/<instance_id>', methods=['GET'])
def show_phishing_activity(instance_id):
    return f"<h1>Phishing Simulado</h1><p>Instância: {instance_id}</p>"

@user_bp.route('/malware_simulacao/<instance_id>', methods=['GET'])
def show_malware_activity(instance_id):
    return f"<h1>Alerta de Malware Simulado</h1><p>Instância: {instance_id}</p>"