from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import pyautogui
import yaml
import time
import random
import logging

logging.basicConfig(level=logging.INFO);
logger = logging.getLogger()

class EasyApplyBot:
    def __init__(self, config_filename):
        with open(config_filename,'r') as file:
            self.config = yaml.safe_load(file)
        
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def login(self):
        self.driver.get("https://www.linkedin.com/login")
        
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        
        username_input.send_keys(self.config['username'])
        password_input.send_keys(self.config['password'])
        
        password_input.send_keys(Keys.RETURN)
    
    def search_jobs(self, position, location):
        # Navigate to the LinkedIn jobs page
        self.driver.get("https://www.linkedin.com/jobs/")

        # Find the job position and location search fields using their respective identifiers
        # Note: The exact identifiers might change over time. It's always a good idea to check the current page's source.
        position_field = self.driver.find_element_by_css_selector("input[aria-label='Search jobs']")
        location_field = self.driver.find_element_by_css_selector("input[aria-label='Search location']")

        # Input the desired position and location into the fields
        position_field.clear()
        position_field.send_keys(position)
        location_field.clear()
        location_field.send_keys(location)

        # Locate the search button and click it
        # Note: The search button might not have an ID or name, so we might need to use other methods like XPath.
        search_button = self.driver.find_element_by_xpath("//button[@data-control-name='search_jobs']")
        search_button.click()


 if __name__ == "__main__":
    bot = EasyApplyBot('config.yaml')
    bot.login()
    # We'll add more methods and functionality as we go.
