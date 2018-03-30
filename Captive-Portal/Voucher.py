from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, invisibility_of_element_located, \
                                                            title_contains, title_is
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import socket

import Login
import Socket_client_voucher


class Voucher:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def generate_voucher(self):

        driver = Login.Login(self.url, self.username, self.password).run()
        driver.find_element_by_id("button_cp").click()
        driver.find_element_by_id("qtd").send_keys("1")
        driver.find_element_by_id("numDevices").send_keys("1")
        select_temp = Select(driver.find_element_by_id("id_time"))
        select_temp.select_by_value("other")
        driver.find_element_by_id("valueTime").clear()
        driver.find_element_by_id("valueTime").send_keys("1")
        driver.find_element_by_id("generate").click()
        voucher = driver.find_element_by_id("122_cod").get_attribute("id")
        result = Socket_client_voucher.Socket("SSID", voucher, "1", "1").Socket_client()
        driver.quit()
        return result