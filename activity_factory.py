# NOVO FICHEIRO: activity_factory.py

from abc import ABC, abstractmethod
from typing import Type
from .activity import Activity, PhishingActivity, MalwareActivity

# =================================================================
# 1. CRIADOR ABSTRATO (Interface ActivityCreator)
# Declara o método de fábrica (create_activity), que retorna um objeto Activity.
# =================================================================
class ActivityCreator(ABC):
    """
    Classe abstrata que define o Factory Method. 
    Contém a lógica de domínio que usa o objeto Activity.
    """
    
    @abstractmethod
    def create_activity(self) -> Activity:
        """O método de fábrica. Implementado pelas subclasses."""
        pass

    def get_activity_product(self) -> Activity:
        """
        Lógica de domínio que depende da atividade criada.
        Esta é a vantagem principal do Factory Method: o código aqui não
        precisa de saber qual é a classe concreta de Activity.
        """
        # Chama o Factory Method para criar um objeto Produto
        activity = self.create_activity()
        return activity

# =================================================================
# 2. CRIADORES CONCRETOS (Fábricas Específicas)
# Sobrescrevem o método de fábrica para retornar um Produto Concreto.
# =================================================================
class PhishingActivityCreator(ActivityCreator):
    """Cria uma instância de PhishingActivity."""
    def create_activity(self) -> Activity:
        return PhishingActivity()

class MalwareActivityCreator(ActivityCreator):
    """Cria uma instância de MalwareActivity."""
    def create_activity(self) -> Activity:
        return MalwareActivity()

# =================================================================
# FÁBRICA DE CRIADORES (Ajuda a abstrair a escolha)
# Uma função ou classe auxiliar para selecionar o Criador.
# =================================================================
def get_creator_by_type(activity_type: str) -> Type[ActivityCreator]:
    """Seleciona o Criador apropriado com base no tipo de atividade."""
    if activity_type.lower() == 'phishing':
        return PhishingActivityCreator
    elif activity_type.lower() == 'malware':
        return MalwareActivityCreator
    else:
        raise ValueError(f"Tipo de atividade desconhecido: {activity_type}")