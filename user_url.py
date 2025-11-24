# Arquivo: user_url.py
from flask import Blueprint, request, Response

user_bp = Blueprint('user', __name__)

@user_bp.route('/deploy-atividade', methods=['GET'])
def deploy_activity():
    """
    Gera o URL final para o estudante com base no ID da instância.
    """
    invenira_instance_id = request.args.get('invenira_instance_id')

    if invenira_instance_id:
        # Lógica interna (BD) seria aqui...
        
        dominio_ap = request.host_url.rstrip('/')
        deployment_url = f"{dominio_ap}/atividade_instancia/{invenira_instance_id}"
        
        return Response(deployment_url, mimetype='text/plain')
    else:
        return Response("Erro: ID da instância da Inven!RA em falta.", status=400, mimetype='text/plain')

# Rota extra para simular a atividade real onde o aluno entra
@user_bp.route('/atividade_instancia/<instance_id>', methods=['GET'])
def show_activity(instance_id):
    return f"<h1>Atividade a correr</h1><p>Instância: {instance_id}</p>"