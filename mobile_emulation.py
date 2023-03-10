import time
from selenium import webdriver
import main

mobile_emulation = {"deviceName": "iPhone 5"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=chrome_options)
queries = ["internet", "computer", "science", "technological", "artificial intelligence", "machine learning", "cloud computing", "cybersecurity", "blockchain", "big data", "augmented reality", "virtual reality", "5G", "smart glasses","computer vision","mixed reality","spatial computing","AR cloud","biotechnology","engineering"]


main.login(driver)
main.search(driver, queries)
time.sleep(10)
driver.quit()
