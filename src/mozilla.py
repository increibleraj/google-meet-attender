import time
import datetime

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# custom module import goes here
import user
import config

#---------------------------------------------------------------------------
# google loin page url goes here
loginurl = 'https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier'
uid = user.gmailid # login credentials provided by user goes here
pwd = user.password
meeturl = user.meeturl # meeting url provided by user goes here
meetdur = user.duration * 60 # meeting duration provided by user goes here
geckodriver = config.geckodriver # gecko driver path geos here
geckodriver_log = config.geckodriver_log # gecko driver log path geos here
timeout = 900 # waiting timeout time in seconds
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# webdriver initialization starts here
options = Options()
# options.add_argument("--headless")
options.add_argument('--incognito')
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')
options.add_argument("--disable-infobars")
options.set_preference("permissions.default.microphone", 2) # disable mic
options.set_preference("permissions.default.camera", 2) # disable camera

browser = webdriver.Firefox(
    firefox_profile=None, # default
    firefox_binary=None, # default
    timeout=30, # default
    capabilities=None, # default
    proxy=None, # default
    executable_path=geckodriver,
    options=options,
    service_log_path=geckodriver_log,
    firefox_options=None, # deprecated argument for options
    service_args=None, # default
    desired_capabilities=None, # default
    log_path=None, # deprecated argument for service_log_path
    keep_alive=True # default
)
#---------------------------------------------------------------------------
# login payload starts here
try:# login payload starts here

    print(datetime.datetime.now().strftime('%H:%M %d/%m/%Y'), " : logging in...")
    browser.get(loginurl)

    input1 = WebDriverWait(browser, timeout).until(expected_conditions.visibility_of_element_located((By.ID, 'identifierId')))
    input1.clear()
    input1.send_keys(uid)

    time.sleep(5)
    button1 = WebDriverWait(browser, timeout).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.VfPpkd-LgbsSe')))
    button1.click()

    input2 = WebDriverWait(browser, timeout).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")))
    input2.clear()
    input2.send_keys(pwd)

    time.sleep(5)
    button2 = WebDriverWait(browser, timeout).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ')))
    button2.click()
    print(datetime.datetime.now().strftime('%H:%M %d/%m/%Y'), " : login successful")

except Exception as error:
    print("error occurred while logging in :\n", error)
    browser.close()
    exit(-1)
# login payload ends here

# join meet payload starts here
try:
    print(datetime.datetime.now().strftime('%H:%M %d/%m/%Y'), " : joining meet...")
    browser.get(meeturl)
    time.sleep(10)
    buttonJoinMeet = WebDriverWait(browser, timeout).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'div.uArJ5e:nth-child(1)')))
    buttonJoinMeet.click()
    print(datetime.datetime.now().strftime('%H:%M %d/%m/%Y'), " : meeting joined successfully")

except Exception as error:
    print("error occurred while joining meet :\n", error)
    browser.close()
    exit(-1)
# join meet payload ends here

print(datetime.datetime.now().strftime('%H:%M %d/%m/%Y'), " : this meeting will be attended for ", meetdur/60, " mins")
print(datetime.datetime.now().strftime('%H:%M %d/%m/%Y'), " : to leave meeting any time press CTRL + C")

#explicit wait
time.sleep(meetdur)

# closing browser
browser.close()
print(datetime.datetime.now().strftime('%H:%M %d/%m/%Y'), " : left meeting\n")