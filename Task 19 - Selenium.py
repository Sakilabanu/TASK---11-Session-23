from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#e =r"C:\Users\Dell\Desktop\ALL PYTHON AND SELENIUM G\SELENIUM\chromedriver.exe"
chrome_service = ChromeService(r"C:\Users\sahbi\OneDrive\Desktop\PyCharm Community Edition 2023.2.5\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/")
driver.title

