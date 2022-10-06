import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/home/pulkit/Workstation/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

items ={}
ids = ["buyCursor", "buyGrandma", "buyFactory", "buyMine",
      "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"]

for id in ids:
    tag = driver.find_element(By.ID, id)
    tag = tag.find_element(By.CSS_SELECTOR, "b")
    item = tag.text.split('-')
    number = ""
    for num in item[1].split(','):
        number += num

    number = int(number)
    items[item[0].split()[0]] = number

time_up = time.time()+3

while time.time() < time_up:
    try:
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()

        money = int(driver.find_element(By.ID, "money").text)
        buy_key = None
        for key, value in items.items():
            if value <= money:
                buy_key = key
            else:
                break

        if buy_key is not None:
            element = driver.find_element(By.ID, "buy"+buy_key)
            element.click()
            element = element.find_element(By.CSS_SELECTOR, "b")
            item = element.text.split('-')
            number = ""
            for num in item[1].split(','):
                number += num

            number = int(number)
            items[item[0].split()[0]] = number


    except selenium.common.exceptions.StaleElementReferenceException:
        pass

cps = driver.find_element(By.ID, "cps")
print(cps)

