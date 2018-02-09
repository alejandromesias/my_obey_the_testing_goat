from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn( row_text , [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        input_placeholder = inputbox.get_attribute('placeholder')
        self.assertEqual(input_placeholder,'Enter a to-do item')

        #enter a new to do
        inputbox.send_keys('Buy this crazy thing')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy this crazy thing')

        inputbox = self.browser.find_element_by_id('id_new_item')
        #enter a second new to do
        inputbox.send_keys('Buy a second thing')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy this crazy thing')
        self.check_for_row_in_list_table('2: Buy a second thing')




if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
