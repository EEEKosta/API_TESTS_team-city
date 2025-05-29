import requests
import pytest

from custom_requester.custom_requester import CustomRequester
from data.project_data import ProjectData


class TestProjectCreate:
    project_data = None

    @classmethod
    def setup_class(cls):
        cls.project_data= ProjectData.create_project_data()
        cls.create_project_id = cls.project_data["id"]

    def test_project_create(self, api_manager):
        create_project_response = api_manager.project_api.create_project(self.project_data).json()
        assert create_project_response.get("id", {}) == self.create_project_id

        get_projects_response = api_manager.project_api.get_project().json()
        project_ids = [project.get('id', {}) for project in get_projects_response.get('project', [])]
        assert self.create_project_id in project_ids

        api_manager.project_api.clean_up_project(self.create_project_id)
