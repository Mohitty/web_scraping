from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.pclub.in')
titles = driver.find_elements_by_css_selector("h2")

for title in titles:
    print title.text
