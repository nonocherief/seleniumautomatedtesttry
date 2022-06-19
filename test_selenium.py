from tkinter import Button
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

class RefurbedSearch(unittest.TestCase):   

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_refurbed(self):
        driver = self.driver
        driver.get("https://www.refurbed.at/")
        self.assertIn("refurbed", driver.title)
        elem = driver.find_element(by=By.NAME, value="query")
        elem.send_keys("apple")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def test_button(self):
        driver=self.driver
        driver.get("https://www.refurbed.at/")
        button=driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Handys")
        button.click()
        self.assertIn("Handys & Smartphones:",driver.find_element(by=By.XPATH, value='//*[@id="wrapper"]/div/div[2]/div[2]/main/div[1]/div[1]/h1').text)
        self.assertNotIn("No results found.", driver.page_source)

    def test_other_button(self):
        driver=self.driver
        driver.get("https://www.refurbed.at/")
        button=driver.find_element(by=By.XPATH, value="/html/body/header/div[1]/ul/a[2]/li")
        button.click()
        self.assertIn("https://fashion.refurbed.com/at", driver.current_url)
        self.assertNotIn("No results found", driver.page_source)

    def test_some_API(self):
        r=requests.get("https://api.refurbed.io/v1/categories/id/27/")
        data=r.json()
        self.assertEqual(27,data["id"])
        self.assertEqual("huawei-phones",data["slug"])

    def tearDown(self):
        self.driver.quit()

unittest.main()









