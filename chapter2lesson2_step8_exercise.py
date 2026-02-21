import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname'][required]")
    input1.send_keys("Yuliya")

    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname'][required]")
    input2.send_keys("Andrushenkava")

    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email'][required]")
    input3.send_keys("test@test.com")


#файл загружаем

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir,file_name)

    element = browser.find_element(By.CSS_SELECTOR, 'input#file')

    element.send_keys(file_path)
#итог - файл должен прикрепиться и отобразиться рядом с кнопкой Browse

#сабмитим форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
# закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл    