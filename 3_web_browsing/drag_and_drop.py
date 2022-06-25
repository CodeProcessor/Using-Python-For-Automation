import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

url = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
source = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[12]')
dest = driver.find_element_by_xpath('//*[@id="box107"]')

actions = ActionChains(driver)
actions.drag_and_drop(source, dest).perform()
time.sleep(5)
driver.close()