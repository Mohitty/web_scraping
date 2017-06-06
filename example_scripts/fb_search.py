
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = raw_input("your username: ")
pwd = raw_input("yourpassword: ")

driver = webdriver.Firefox()
# or you can use Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

find = raw_input("what you want to search: ")
search = driver.find_element_by_name("q") 
search.clear()
search.send_keys(find)
search.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close()
