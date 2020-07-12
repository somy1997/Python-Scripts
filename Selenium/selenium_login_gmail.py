import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Firefox()
#driver= webdriver.Chrome("E:\QA\Resource\WEBDRIVER\chromedriverserver\chromedriver.exe")
driver.get("http://mail.google.com")

emailid=driver.find_element_by_id("Email")
emailid.send_keys("username")

passw=driver.find_element_by_id("Passwd")
passw.send_keys("password")

signin=driver.find_element_by_id("signIn")
signin.click()

time.sleep(10)

driver.switch_to_frame('canvas_frame')

sentmail= driver.find_element_by_link_text('Sent Mail')
sentmail.click()

time.sleep(10)

sentmail= driver.find_element_by_link_text('Your Name')
sentmail.click()

lout= driver.find_element_by_link_text('Sign out')
lout.click()