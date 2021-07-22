from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import warnings, argparse, syss

warnings.filterwarnings('ignore')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-xss-auditor')
options.add_argument('--disable-web-security')
options.add_argument('--ignore-certification-errors')
options.add_argument('--no-sandbox')