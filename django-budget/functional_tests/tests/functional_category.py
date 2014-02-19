from .functional_base import BaseLiveServer


class CategoryFunctionalTestCase(BaseLiveServer):

    def test_create_category(self):
        self.create_auth_session()
        self.visit('/setup/')

        self.browser.click_link_by_partial_href('/category/')
        self.assertEqual('Category List', self.browser.title)

        self.browser.click_link_by_partial_href('/category/add/')
        self.assertEqual('Add A Category', self.browser.title)

        self.browser.fill('name', 'Eggs')
        submit_button = self.browser.find_by_name('submit').first
        submit_button.click()

        self.assertEqual(302, self.browser.status_code.code)

        column_name = self.browser.find_by_css('.name').first
        self.assertEqual('Eggs', column_name.text)
