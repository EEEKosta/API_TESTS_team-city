import requests
import pytest
from enums.host import BASE_URL
from custom_requester.custom_requster import CustomRequester
from data.project_data import ProjectData


class TestProjectCreate:

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project_data()
        cls.project_id = cls.project_data['id']

    def test_project_create(self):
        requester = CustomRequester(requests.Session())

        # Get token
        auth_response = requests.get(url=f'{BASE_URL}/authenticationTest.html?csrf', auth=('admin', 'admin'))
        csrf_token = auth_response.text
        headers = {'X-TC-CSRF-Token': csrf_token}

        # Set data
        project_id = 'simpleprojectID2'
        project_data = {
                        "parentProject": {
                                            "locator": "_Root"
                                         },
                        "name": "ProjectNameSimple2",
                        "id": project_id
                        }

        # Create project
        create_response = requests.post(url=f'{BASE_URL}/app/rest/projects', headers=headers, json=project_data)
        assert create_response.status_code == 200, 'Не удалось создать проект'

        # Check create project
        chek_project = requests.get(url=f'{BASE_URL}/app/rest/projects/id:{project_id}', headers=headers)
        assert chek_project.status_code == 200, 'Проект не найден'

        # Delete project
        delete_project = requests.delete(url=f'{BASE_URL}/app/rest/projects/id:{project_id}', headers=headers)
        assert delete_project.status_code == 204, 'Не удалось удалить проект'
