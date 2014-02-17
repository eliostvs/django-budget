from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase

from splinter import Browser
from selenium.webdriver import DesiredCapabilities

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


class LoginTestCase(BaseLiveServer):

    def test_login_and_logout(self):
        self.get_or_create_user()

        self.browser.visit(self.live_server_url)

        self.assertEqual('Login', self.browser.title)

        self.browser.fill('username', self.username)
        self.browser.fill('password', self.password)
        self.browser.find_by_name('login').click()

        icon = self.browser.find_by_id('userIcon')

        self.assertTrue(icon)
