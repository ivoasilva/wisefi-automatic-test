from selenium import webdriver


import Login
import Voucher
import Configure_SSID_CP_Voucher


class Run:
    def __init__(self, ip, port, username, password):
        self.port = port
        self.ip = ip
        self.username = username
        self.password = password

    def main(self):
        print("Sarting test Wisefi")
        print("IP:", self.ip)
        print("Port:", self.port)
        print("User:", self.username)
        print("Password:", self.password)
        url = "http://" + str(self.ip) + ":" + str(self.port)
        print("URL", url)
        #Login.Login(url, self.username, self.password).run()
        Configure_SSID_CP_Voucher.Wlan(url, self.username, self.password).configure_ssid_cp_voucher()

if __name__ == '__main__':
    Run("127.0.0.1", 8000, "admin", "12345678").main()