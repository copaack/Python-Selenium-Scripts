from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 200)
driver.get("https://web.whatsapp.com/")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'span[title="Talha Uni"]')))
search=driver.find_element(By.CSS_SELECTOR,'span[title="Talha Uni"]').click()
for i in range(500):
    input=driver.find_element(By.CSS_SELECTOR,"p[class='selectable-text copyable-text']")
    input.send_keys("*404__Error*")
    #input.send_keys(Keys.RETURN)
    driver.find_element(By.CSS_SELECTOR,'span[data-testid="send"]').click()
    
time.sleep(15)