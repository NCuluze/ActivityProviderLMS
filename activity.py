# NOVO FICHEIRO: activity.py

from abc import ABC, abstractmethod
from typing import List, Dict, Any

# =================================================================
# 1. PRODUTO ABSTRATO (Interface Activity)
# Define a interface para os objetos que o método de fábrica irá criar.
# =================================================================
class Activity(ABC):
    """Interface comum para todos os Minicursos de Cibersegurança."""
    
    @abstractmethod
    def get_json_params(self) -> List[Dict[str, str]]:
        """Retorna a lista de metadados para configuração na Inven!RA."""
        pass

    @abstractmethod
    def get_deployment_url(self, invenira_instance_id: str, host_url: str) -> str:
        """Gera o URL de deployment final para o estudante."""
        pass

    @abstractmethod
    def get_analytics_data(self, activity_id: str) -> List[Dict[str, Any]]:
        """Retorna dados simulados de analytics para a atividade."""
        pass

# =================================================================
# 2. PRODUTOS CONCRETOS (Simulações Específicas)
# Implementam as atividades concretas.
# =================================================================
class PhishingActivity(Activity):
    """Simulação de Ataque de Phishing."""
    
    def get_json_params(self) -> List[Dict[str, str]]:
        # Parâmetros específicos para Phishing (e.g., campo 'email_modelo')
        return [
            {"name": "titulo_minicurso", "type": "text/plain"},
            {"name": "payload_simulacao_json", "type": "text/plain"}, # Email simulado
            {"name": "acao_correta_esperada", "type": "text/plain"}, # Ex: Reportar
            {"name": "tipo_simulacao", "type": "text/plain", "value": "Phishing"}
        ]

    def get_deployment_url(self, invenira_instance_id: str, host_url: str) -> str:
        # A URL aponta para a atividade de Phishing
        dominio_ap = host_url.rstrip('/')
        return f"{dominio_ap}/phishing_simulacao/{invenira_instance_id}"

    def get_analytics_data(self, activity_id: str) -> List[Dict[str, Any]]:
        # Dados específicos para Phishing (Ex: Clicou no Link/Reportou)
        return [{"inveniraStdID": "1001", "quantAnalytics": [{"name": "Reportou Email", "value": True}]}]


class MalwareActivity(Activity):
    """Simulação de Ataque de Malware."""

    def get_json_params(self) -> List[Dict[str, str]]:
        # Parâmetros específicos para Malware (e.g., campo 'popup_warning')
        return [
            {"name": "titulo_minicurso", "type": "text/plain"},
            {"name": "descricao_malware", "type": "text/plain"},
            {"name": "acao_correta_esperada", "type": "text/plain"}, # Ex: Isolar sistema
            {"name": "tipo_simulacao", "type": "text/plain", "value": "Malware"}
        ]

    def get_deployment_url(self, invenira_instance_id: str, host_url: str) -> str:
        # A URL aponta para a atividade de Malware
        dominio_ap = host_url.rstrip('/')
        return f"{dominio_ap}/malware_simulacao/{invenira_instance_id}"

    def get_analytics_data(self, activity_id: str) -> List[Dict[str, Any]]:
        # Dados específicos para Malware (Ex: Tempo de Reação/Ação de Quarentena)
        return [{"inveniraStdID": "1002", "quantAnalytics": [{"name": "Tempo de Reação (Segundos)", "value": 35}]}]

#