from custom_requester.custom_requster import CustomRequester


class AurhAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)
        self.session = session
        self.auth_and_get_csrf()

    def auth_and_get_csrf(self):
        self.session.auth = ("admin", "admin")
        csrf_token = self.send_request('GET', '/authenticationTest.html?csrf').text
        if not csrf_token:
            raise ValueError("CSRF token is missing")
        self._update_session_headers(**{'X-CSRFToken': csrf_token})