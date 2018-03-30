from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.set_page_load_timeout(15)


class Login:

    def __init__(self, url, username, password):

        self.url = url
        self.username = username
        self.password = password

    def run(self):
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(self.username)
        driver.find_element_by_name("password").send_keys(self.password)
        driver.find_element_by_tag_name("button").click()
        title = driver.title
        print(title)
        if driver.find_element_by_id("button_home"):
            botao = driver.find_element_by_id("button_home").get_attribute("id")
            print(botao)
            print("Login feito com sucesso")
        else:
            print("Login não foi feito!")
        return driver
        #driver.quit()


if __name__ == '__main__':
    Login("http://127.0.0.1:8000", "admin","12345678").run()
