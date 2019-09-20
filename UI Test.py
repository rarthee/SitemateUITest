from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import logging


class Customer_Confirmation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        ##Go to the main login page
        self.driver.get("**/modal-test/index.html")

    def test_01_Click_MainPage(self):

        ##Check if we have reached the correct page. In this example I am assuming a sample title "Consumer Main"
        self.assertIn("Consumer Main", self.driver.title)
        ##Check if the Click Me button is clickable and then click it
        element="self.driver.find_element_by_id('button-1')"
        try:
            element.click()
            ##Providing a an implicit wait time for the next page to load
            self.driver.implicitly_wait(self, 5)
        except WebDriverException:
            print("Element is not clickable")


    def test_02_Accept_alert(self):

        ##Checking if the alert is displayed and if so accept the alert. If not print that there is no alert
        try:
            alert = self.driver.switch_to.alert()
            alert.accept()
            print("alert accepted")
            ##Get the successful message displayed on the screen after accepting the alert
            text = self.driver.find_element_by_xpath("*[@id='result']").getText();
            # Check if the message is "You just clicked "Yes"."
            self.assertIn('You just clicked "Yes".', text)
        except TimeoutException:
            print("There is no alert")

    def test_03_Reject_alert(self):
        # refresh the webpage so that we will get to the main page
        self.driver.refresh()

        # Check if we have reached the correct Main page again
        self.assertIn("Consumer Main", self.driver.title)
        ##Check if the Click Me button is clickable and then click it
        element = "self.driver.find_element_by_id('button-1')"
        try:
            element.click()
            ##Switch to alert and reject it. Then evaluate the message displayed
            alert = self.driver.switch_to.alert()
            alert.reject()
            print("alert rejected")
            text = ''
            ## Providing an explicit Wait for the main page to load with the message after rejecting the alert
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.id, "result")))
            ##Get the message displayed on the screen after rejecting the alert
            text = self.driver.find_element_by_xpath("*[@id='result']").getText();
            # Check if the message is "You just clicked "Cancel"."
            self.assertIn('You just clicked "Cancel".', text)
        except WebDriverException:
            print("Element is not clickable")

    def test_04_log(self):
        log = logging.getLogger()  # root logger
        log.setLevel(logging.INFO)
    def tearDown(self):
        self.driver.quit()
