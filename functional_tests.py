from selenium import webdriver
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
		self.fail('Finish the test!')
		
		# She is invited to enter a to-do item 


		# She types play volleyball into a text box


		# When she hits enter, the page updates, and now the page lists "1: Play Volleyball"
		# as an item in a to-do lists

		# There is still a text box inviting her to add another item.  She enters
		# "Work on website" 


		# The page updates again, and now shows both items on her lists


		# Wendy wonders if the site will remember her list.  She sees the site has generated a unique URL
		# for her (with some explanatory text to that effect)


		# She visits that URL - her to-do list is still there


		# Satisfied she goes back to sleep
	
if __name__ == '__main__':
	unittest.main()

