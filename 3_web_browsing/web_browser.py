from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.archive.org/web/20180926132852/http://www.seleniumeasy.com:80/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World!')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('20')
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()
