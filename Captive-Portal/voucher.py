from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, invisibility_of_element_located, \
                                                            title_contains, title_is
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
driver.maximize_window()

wait = WebDriverWait(driver, 5)

def find(self, *locator, timeout=30):
    element = WebDriverWait(driver, timeout).until(visibility_of_element_located(*locator))
    return element

'''
def login(user, password):
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_tag_name("button").click()
    title = driver.title
    print(title)
    if "WiseFi" == title:
        print("Title OK")
    else:
        print("Title NOk")
'''
login.wisefi_login("admin", "12345678").login()



def configure_ssid():
    driver.find_element_by_id("button_cp").click()
    driver.find_element_by_id("qtd").send_keys("1")
    driver.find_element_by_id("numDevices").send_keys("1")
    select_temp = Select(driver.find_element_by_id("id_time"))
    select_temp.select_by_value("other")
    driver.find_element_by_id("valueTime").clear()
    driver.find_element_by_id("valueTime").send_keys("1")
    driver.find_element_by_id("generate").click()


'''
login("admin", "12345678")
configure_ssid()
driver.implicitly_wait(20)
driver.quit()
'''