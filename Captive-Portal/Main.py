from selenium import webdriver


import Login
import Voucher


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
        result = Voucher.Voucher(url, self.username, self.password).generate_voucher()
        print("Result Test Voucher: ", result)

if __name__ == '__main__':
    Run("127.0.0.1", 8000, "admin", "12345678").main()