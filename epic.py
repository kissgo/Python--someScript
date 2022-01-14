from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

desired = DesiredCapabilities.CHROME
desired["pageLoadStrategy"]="none"

driver = webdriver.Chrome()
driver.get("https://www.epicgames.com/store/zh-CN/")
time.sleep(15)
driver.find_element_by_class_name('sign-text item-label display-name text-color').click()
time.sleep(15)
driver.find_element_by_class_name('MuiTypography-root SocialBarListLabel MuiTypography-subtitle1').click()
time.sleep(15)