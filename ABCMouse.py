from selenium import webdriver
import ABCMouse_config

browser = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
browser.get('https://www.abcmouse.com/login')
emailElem = browser.find_element_by_id('login_email')
emailElem.send_keys(ABCMouse_config.EMAIL)
passwordElem = browser.find_element_by_id('login_password')
passwordElem.send_keys(ABCMouse_config.PASSWORD)
browser.find_element_by_class_name("submit_button").click()
browser.fullscreen_window()