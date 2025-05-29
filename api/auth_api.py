from requests import session
from custom_requester.custom_requester import CustomRequester


class AuthAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)
        self.session = session
        self.auth_and_get_csfr()


    def auth_and_get_csfr(self):
        self.session.auth = ('admin', 'admin')
        csrf_token = self.send_request('GET', '/authenticationTest.html?csrf').text
        if not csrf_token:
            raise ValueError(f'CSRF token is missing or invalid - {csrf_token}')
        self._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})