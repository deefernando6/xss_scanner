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

for payload in open(wordlist, "r").readlines():
    url = target.replace('{fuzz}', payload)
    driver.get(url)
	try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to_alert
        alert.accept
        print("XSs alert accpeted with ", payload)
    except:
        print("XSS doesn\'t work with", payload)