from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(treasure_x):
  return str(math.log(abs(12*math.sin(int(treasure_x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    find_treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
    treasure_x = find_treasure.get_attribute("valuex")
   
# расчет формулы
    y = calc(treasure_x)

  
# после всех вычислений нахожу элемент инпута куда надо вставить текст
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

#отмечаем чекбокс I'm the robot
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox[type='checkbox']")
    option1.click()
#отмечаем радиобаттон Robots rule
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule[type='radio']")
    option2.click()

# Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл