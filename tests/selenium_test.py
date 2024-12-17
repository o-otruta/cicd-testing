from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://127.0.0.1:5000")

    name_field = driver.find_element(By.ID, "name")
    name_field.send_keys("Test User")

    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()

    time.sleep(2)

    assert "Test Page" in driver.title
    print("Test Passed: Title contains 'Test Page'")

except Exception as e:
    print("Test Failed:", str(e))

finally:
    driver.quit()
