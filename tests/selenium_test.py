from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск браузера
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000")

# Знайти поле вводу та кнопку
name_field = driver.find_element(By.ID, "name")
name_field.send_keys("Test User")

submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
submit_button.click()

time.sleep(2)  # Дочекайтеся алерту

# Перевірка заголовка сторінки
assert "Test Page" in driver.title

# Закриття браузера
driver.quit()
