from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "https://SunInJuly.github.io/execute_script.html"


def calc(value_x):
  return str(math.log(abs(12*math.sin(value_x)))) #возвращаем формат srt, чтобы вставить значение в инпут


try:
    browser = webdriver.Chrome()
    browser.get(link)

#находим значение числа
    find_value_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    value_x = int(find_value_x.text) #делаем int, чтобы вычисления сработали

    
    # расчет формулы (сумма на int)
    result_fin = calc(value_x)

# после всех вычислений нахожу элемент инпута куда надо вставить текст
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(result_fin)

#находим кнопку и скролим страницу вниз
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


#отмечаем чекбокс I'm the robot
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox[type='checkbox']")
    option1.click()

#отмечаем радиобаттон Robots rule
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule[type='radio']")
    option2.click()


#нажимаем на Submit
    button1 = browser.find_element(By.CSS_SELECTOR,'button.btn')
    button1.click()

finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
# закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл