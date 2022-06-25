from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = "https://earth.google.com/web/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/earth-app//paper-drawer-panel/div/earth-toolbar//earth-gm2-icon-button[4]')))

element.click()
