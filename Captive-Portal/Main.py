from selenium import webdriver

#from Login import Logindfd

class Run:
    def __init__(self, ip, port, username, password):
        self.port = port
        self.ip = ip
        self.usename = username
        self.password = password

    def main(self):
        print("Sarting test Wisefi")
        print("IP:", self.ip)
        print("Port:", self.port)
        print("User:", self.usename)
        print("Password:", self.password)
        url = "http://" + str(self.ip) + ":" + str(self.port)
        print("URL", url)

        #status_login = login.wisefi_login(url, self.usename, self.password)
        #print(status_login)

if __name__ == '__main__':
    Run("127.0.0.1", 8000, "admin", "12345678").main()