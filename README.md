# google-meet-attender
your college is using browser extension to auto collect gmeet attendance? 
Uh! then why don't you use this gmeet attendance bot

#### how to use?
* go to /google-meet-attender/src/user.py
* put your gmail id, password, meeting url and meeting duration there
* go to /google-meet-attender/src/config.py
* uncomment every thing after 'windows file paths' if you are using a microsoft based os
* uncomment every thing before 'windows file paths' if you are using a linux based os
* go to /google-meet-attender/src/ directory and run 'python3 mozilla.py' from terminal
* to launch firefox in headless mode (in background) just uncomment this line '# options.add_argument("--headless")' in /google-meet-attender/src/mozilla.py

#### dependencies
    $pip3 install selenium
    
* mozilla firefox web browser

#### debugging 
##### if you see some error related to webdriver
* make sure your firefox is up to date
* download the latest release of gecko webdriver and extract it in '/google-meet-attender/src/'

#### extension

* you can use 'windows scheduler' or cron (for linux) to schedule this to script to run daily during your class time
* you can also deploy this on web servers (like heroku which is free) 
