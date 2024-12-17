from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Налаштування опцій для Chrome (headless mode)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск без графічного інтерфейсу
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Запуск Chrome
service = Service(executable_path="/usr/bin/chromedriver")  # GitHub Actions знає шлях до chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Перехід на сторінку
driver.get("http://127.0.0.1:5000")

# Тестування: знайти поле вводу та кнопку
name_field = driver.find_element(By.ID, "name")
name_field.send_keys("Test User")

submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
submit_button.click()

time.sleep(2)  # Зачекати для підтвердження роботи

# Перевірка заголовка сторінки
assert "Test Page" in driver.title

# Завершення тесту
driver.quit()
