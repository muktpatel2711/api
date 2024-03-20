from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://dev.baps.dev/mis")
Title = driver.title
assert Title == "BAPS MIS"
True
print("Title is valid:", Title)
