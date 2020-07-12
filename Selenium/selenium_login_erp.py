from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from time import sleep
def page_is_loaded(driver):
  return driver.find_element_by_tag_name("body") != None
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("https://erp.iitkgp.ernet.in/IIT_ERP3/")
wait = ui.WebDriverWait(driver, 100)
wait.until(page_is_loaded)
#sleep(10)
# Put roll number
email_field = driver.find_element_by_id("user_id")
email_field.send_keys("XXXXXXXXX")
# Put password
password_field = driver.find_element_by_id("password")
password_field.send_keys("xxxxxxxx")
#password_field.send_keys(Keys.RETURN)

