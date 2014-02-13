from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase

from splinter import Browser

User = get_user_model()


class BaseLiveServerTestCase(LiveServerTestCase):
    username = 'spam'
    password = 'eggs'

    @classmethod
    def setUpClass(cls):
        super(BaseLiveServerTestCase, cls).setUpClass()
        cls.browser = Browser('phantomjs')

    @classmethod
    def tearDownClass(cls):
        super(BaseLiveServerTestCase, cls).tearDownClass()
        cls.browser.quit()

    def test_login_with_valid_user(self):
        self.get_or_create_user()
        self.login()

    def get_or_create_user(self):
        try:
            User.objects.get(username__exact=self.username)
        except User.DoesNotExist:
            User.objects.create_user(self.username, '', self.password)

    def login(self):
        url = self.get_url('login')
        self.browser.visit(url)

        self.assertEqual('Login', self.browser.title)

        self.browser.fill('username', self.username)
        self.browser.fill('password', self.password)
        self.browser.find_by_name('login').click()

    def get_url(self, urlname):
        return '%s%s' % (self.live_server_url, reverse(urlname))
