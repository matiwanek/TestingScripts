from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj= Service(r"C:\Users\mateusz.iwanek\Desktop\New folder (2)\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()