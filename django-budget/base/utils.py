from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import Client

from djet.testcases import ViewTestCase
from djet.assertions import MessagesAssertionsMixin, StatusCodeAssertionsMixin
from djet.utils import refresh

from mock import MagicMock
from model_mommy import mommy


class BaseTestCase(MessagesAssertionsMixin,
                   StatusCodeAssertionsMixin,
                   ViewTestCase):

    def setUp(self, *args, **kwargs):
        super(BaseTestCase, self).setUp(*args, **kwargs)
        self.mock_user = self._create_mock_user()
        self.mock_session = self._create_mock_session()
        self.anonymous_user = AnonymousUser()
        self.user_model = get_user_model()
        self.user = mommy.prepare('User')
        self.client = Client()

    def login(self):
        try:
            self.user_model.objects.get(username=self.user.username)

        except self.user_model.DoesNotExist:
            self.user_model.objects.create_user(self.user.username, '', self.user.password)

        self.client.login(username=self.user.username, password=self.user.password)

    def _create_mock_user(self):
        user = MagicMock()
        user.is_authenticated = MagicMock(return_value=True)
        return user

    def _create_mock_session(self):
        session = MagicMock()
        session.flush = MagicMock()
        return session

    def refresh(self, instance):
        return refresh(instance)
