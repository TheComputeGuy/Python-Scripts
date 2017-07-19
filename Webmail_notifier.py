from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from win10toast import ToastNotifier

login_id='USERNAME'
passwordStr='PASSWORD'

def failedCase():
    logout_btn=browser.find_element_by_xpath('//*[@id="horde-logout"]/a')
    logout_btn.click()
    browser.quit()

def passedCase():
    mailbox=browser.find_element_by_partial_link_text('Mail')
    mailbox.click()
    toaster = ToastNotifier()
    toaster.show_toast('New Webmail Message', 'Check automated browser', duration=10)
    
    
browser=webdriver.Chrome()

browser.get('https://webmail.nitt.edu/hordenew/login.php')

username=browser.find_element_by_id('horde_user')
username.send_keys(login_id)

password=browser.find_element_by_id('horde_pass')
password.send_keys(passwordStr)

login_btn=browser.find_element_by_id('login-button')
login_btn.click()

try:
    browser.find_element_by_xpath('//*[@id="block_0_0"]/table/tbody/tr/td[2]/span[contains(text(),"new")]')
except:
    failedCase()
else:
    passedCase()
    
                                  
    
