# activity_facade.py
from typing import List, Dict, Any
from .activity_factory import get_creator_by_type

class ActivityFacade:
    """
    Facade que simplifica o acesso ao subsistema de atividades.
    """

    def _get_activity(self, activity_type: str):
        CreatorClass = get_creator_by_type(activity_type)
        creator = CreatorClass()
        return creator.get_activity_product()

    def get_json_params(self, activity_type: str) -> List[Dict[str, str]]:
        activity = self._get_activity(activity_type)
        return activity.get_json_params()

    def get_deployment_url(
        self,
        activity_type: str,
        invenira_instance_id: str,
        host_url: str
    ) -> str:
        activity = self._get_activity(activity_type)
        return activity.get_deployment_url(invenira_instance_id, host_url)

    def get_analytics_data(self, activity_type: str, activity_id: str) -> List[Dict[str, Any]]:
        activity = self._get_activity(activity_type)
        return activity.get_analytics_data(activity_id)
