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


class Wlan:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def configure_ssid_cp_voucher(self):

        driver = Login.Login(self.url, self.username, self.password).run()
        driver.find_element_by_id("button_network").click()
        driver.find_element_by_id("button_wlan").click()
        driver.find_element_by_id("1_edit").click()
        driver.find_element_by_id("ssid1").clear()
        driver.find_element_by_id("ssid1").send_keys("WiseFiTest")
        select_temp = Select(driver.find_element_by_id("id_ssid1Security"))
        select_temp.select_by_value("5")
        select_temp = Select(driver.find_element_by_id("id_ssid1CaptivePortal"))
        select_temp.select_by_value("2")
        driver.find_element_by_id("save").click()
        print("SSID ALTERADO PARA CP VOUCHER")
        driver.quit()
