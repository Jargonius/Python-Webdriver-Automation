import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge2(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_search_exotics_find_porsche(self):
        # This test connects to copart.com, searches for exotics in the search bar
        # and then finds Porsche in the list of results

        css_selector = "span[data-uname='lotsearchLotmake']"

        self.driver.get("https://www.copart.com")
        self.assertIn("Copart USA", self.driver.title)

        search_bar = self.driver.find_element_by_id("input-search")
        search_bar.clear()
        search_bar.send_keys("Exotics")
        search_bar.send_keys(Keys.RETURN)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, css_selector)))

        make_elements = self.driver.find_elements_by_css_selector(css_selector)
        makes = list(map(lambda make: make.get_attribute("innerHTML"), make_elements))
        self.assertIn("PORSCHE", makes)

    def test_follow_link_find_porsche(self):
        # This test connects to copart.com, follows the Exotics link on the homepage
        # and then finds Porsche in the list of results

        css_selector = "span[data-uname='lotsearchLotmake']"

        self.driver.get("https://www.copart.com")
        self.assertIn("Copart USA", self.driver.title)

        exotics_link = self.driver.find_element_by_link_text("Exotics").get_attribute("href")
        self.driver.get(exotics_link)

        make_elements = self.driver.find_elements_by_css_selector(css_selector)
        makes = list( map(lambda make: make.get_attribute("innerHTML"), make_elements))
        self.assertIn("PORSCHE", makes)


if __name__ == '__main__':
    unittest.main()
