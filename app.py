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
        