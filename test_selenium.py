import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RefurbedSearch(unittest.TestCase):   

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_refurbed(self):
        driver = self.driver
        driver.get("https://www.refurbed.at/")
        self.assertIn("refurbed", driver.title)
        elem = driver.find_element_by_name("query")
        elem.send_keys("apple")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def test_button(self):
        driver=self.driver
        driver.get("https://www.refurbed.at/")
        button=driver.find_element_by_partial_link_text("Handys")
        button.click()
    
    def tearDown(self):
        self.driver.quit()

unittest.main()









