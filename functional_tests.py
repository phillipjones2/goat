from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		# Wendy wants to use a online to-do app. She goes to check out its homepage
		self.browser.get('http://localhost:8000')

		# She sees the page title and header mention to-do lists
		self.assertIn ('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# She is invited to enter a to-do item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)


		# She types play volleyball into a text box
		inputbox.send_keys('Play Volleyball')

		# When she hits enter, the page updates, and now the page lists "1: Play Volleyball"
		# as an item in a to-do lists
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Play Volleyball' for row in rows)
		)

		# There is still a text box inviting her to add another item.  She enters
		# "Work on website" 
		self.fail('Finish the test!')

		# The page updates again, and now shows both items on her lists


		# Wendy wonders if the site will remember her list.  She sees the site has generated a unique URL
		# for her (with some explanatory text to that effect)


		# She visits that URL - her to-do list is still there


		# Satisfied she goes back to sleep
	
if __name__ == '__main__':
	unittest.main()

