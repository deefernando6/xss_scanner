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
options.add_argument('--log-level=3')
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(executable_path="usr/bin/chromedriver", chrome_options=options)

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True)
parser.add_argument('-w', '--wordlist', required=True)
args = parser.parse_args()

if not '{fuzz}' in args.url:
    sys.exit("Need {fuzz} parameter !")
else:
    target = args.url
wordlist = args.wordlist