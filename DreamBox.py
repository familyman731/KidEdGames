from selenium import webdriver
import DreamBox_config

browser = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
browser.get('https://play.dreambox.com/play/login')
emailElem = browser.find_element_by_id('txtEmailAddress')
emailElem.send_keys(DreamBox_config.EMAIL)
passwordElem = browser.find_element_by_id('txtPassword')
passwordElem.send_keys(DreamBox_config.PASSWORD)
browser.find_element_by_id("buttonLogin").click()
browser.get("https://play.dreambox.com/login/user_selected?user_id=25499999")
browser.fullscreen_window()