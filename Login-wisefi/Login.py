from selenium import webdriver

driver = webdriver.Chrome()

#Loginw


class Login:

    def __init__(self, url, username, password):

        self.url = url
        self.username = username
        self.password = password

    def run(self):
        print("URL", self.url)
        driver.get(self.url)
        driver.find_element_by_id("username").send_keys(self.username)
        driver.find_element_by_name("password").send_keys(self.password)
        driver.find_element_by_tag_name("button").click()
        title = driver.title
        print(title)
        if "WiseFi" == title:
            print("Login feito com sucesso")
            return 1
        else:
            print("Login não foi feito")

        #driver.quit()

'''
if __name__ == '__main__':
    login("admin","12345678").login_wisefi()
'''