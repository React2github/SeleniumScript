from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:\Users\abdel\OneDrive\Desktop\New folder (4)\chromedriver.exe')
driver.get("https://indeed.com")
driver.find_element_by_xpath('//*[@id="text-input-what"]').send_keys("web developer")
driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button').send_keys(Keys.RETURN)


