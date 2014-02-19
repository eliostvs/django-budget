from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, get_user_model, SESSION_KEY
from django.contrib.sessions.backends.db import SessionStore
from django.test import LiveServerTestCase
from selenium.webdriver import DesiredCapabilities
from splinter import Browser

User = get_user_model()


class BaseLiveServer(LiveServerTestCase):
    username = 'spam'
    password = 'eggs'

    @classmethod
    def setUpClass(cls):
        super(BaseLiveServer, cls).setUpClass()
        capabilities = DesiredCapabilities.PHANTOMJS.copy()
        capabilities['phantomjs.page.customHeaders.Accept-Language'] = 'en,en_US;q=0.8'
        cls.browser = Browser('phantomjs', desired_capabilities=capabilities)

    @classmethod
    def tearDownClass(cls):
        super(BaseLiveServer, cls).tearDownClass()
        cls.browser.quit()

    def get_or_create_user(self):
        try:
            user = User.objects.get(username__exact=self.username)
        except User.DoesNotExist:
            user = User.objects.create_user(self.username, '', self.password)

        return user

    def create_pre_authenticated_session(self):
        user = self.get_or_create_user()
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()
        self.browser.visit(self.live_server_url)
        driver = self.browser.driver
        driver.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/'))


class LoginTestCase(BaseLiveServer):

    def test_login_with_valid_user(self):
        self.get_or_create_user()

        self.browser.visit(self.live_server_url)

        self.assertEqual('Login', self.browser.title)

        self.browser.fill('username', self.username)
        self.browser.fill('password', self.password)
        self.browser.find_by_name('login').click()

        welcome_text = self.browser.find_by_css('.navbar-text').first

        self.assertEqual('Welcome, %s!' % self.username.capitalize(), welcome_text.html)
