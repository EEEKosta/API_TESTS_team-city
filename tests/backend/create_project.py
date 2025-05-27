import requests
from custom_requester.custom_requster import CustomRequester
from data.project_data import ProjectData


class TestProjectCreate:
    project_data = None

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project_data()
        cls.project_id = cls.project_data['id']


    def test_project_create(self):
        requester = CustomRequester(requests.Session())
        requester.session.auth = ("admin", "admin")

        # Get token
        csrf_token = requester.send_request('GET', '/authenticationTest.html?csrf').text
        requester._update_session_headers(**({'X-TC-CSRF-Token': csrf_token}))

        # Create project
        create_response = requester.send_request('POST', '/app/rest/projects', data=self.project_data)
        assert create_response.status_code == 200, 'Не удалось создать проект'

        # Check create project
        check_project = requester.send_request('GET', f'/app/rest/projects/{self.project_id}')
        assert check_project.status_code == 200, 'Проект не найден'

        # Delete project
        delete_project = requester.send_request('DELETE', '/app/rest/projects/' + self.project_id, expected_status=204)
        assert delete_project.status_code == 204, 'Не удалось удалить проект'
