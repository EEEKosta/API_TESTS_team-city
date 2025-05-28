from http import HTTPStatus
from custom_requester.custom_requster import CustomRequester


class ProjectAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)
        self.session = session


    def create_project(self, project_data, expected_status_code=HTTPStatus.OK):
        return self.send_request('POST', '/app/rest/projects', data=project_data, expected_status=expected_status_code)


    def get_project(self):
        return self.send_request('GET', '/app/rest/projects')


    def delete_project(self, project_id, expected_status_code=HTTPStatus.NO_CONTENT):
        return self.send_request('DELETE', f'/app/rest/projects/{project_id}', expected_status=expected_status_code)


    def clean_up_project(self, fake_project_id, expected_status_code=HTTPStatus.NO_CONTENT):
        self.delete_project(fake_project_id)
        get_project_response = self.get_project().json()
        project_id = [project.get('id') for project in get_project_response.get('project', [])]
        assert fake_project_id not in project_id, 'ID созданного проекта найден в списке проектов после удаления'
