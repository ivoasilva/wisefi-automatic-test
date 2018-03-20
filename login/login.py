from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/")


driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_tag_name("button").click()

title = driver.title

print(title)

if "WiseFi" == title:
    print("Test Ok")
else:
    print("Test NOk")

driver.quit()