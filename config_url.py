# Arquivo: config_url.py
from flask import Blueprint, Response

config_bp = Blueprint('config', __name__)

@config_bp.route('/configuracao-atividade', methods=['GET'])
def get_config_form():
    """
    Retorna o HTML do formulário de configuração.
    """
    html_content = """
    <form id="configForm">
        <label for="resumo">Resumo da Descrição Técnica:</label>
        <textarea name="resumo" id="resumo" rows="4" cols="50"></textarea><br><br>
        
        <label for="instrucoes">URL para Instruções Detalhadas:</label>
        <input type="url" name="instrucoes" id="instrucoes"><br><br>
        
        <input type="hidden" name="versao_ap" value="1.0">
    </form>
    """
    return Response(html_content, mimetype='text/html')