from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Налаштування опцій для headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Запуск Chrome
driver = webdriver.Chrome(options=chrome_options)

try:
    # Відкриття сторінки
    driver.get("http://127.0.0.1:5000")

    # Знайти поле вводу та кнопку
    name_field = driver.find_element(By.ID, "name")
    name_field.send_keys("Test User")

    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    # Обробка алерта
    alert = driver.switch_to.alert  # Перемикання на alert
    print("Alert text:", alert.text)  # Вивести текст alert для перевірки
    alert.accept()  # Закрити alert (натиснути OK)

    # Затримка для завершення дій
    time.sleep(2)

    # Перевірка заголовка сторінки
    assert "Test Page" in driver.title
    print("Test Passed: Title contains 'Test Page'")

except Exception as e:
    print("Test Failed:", str(e))

finally:
    # Закриття браузера
    driver.quit()
