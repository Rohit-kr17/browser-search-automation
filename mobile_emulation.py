# This script will search for a list of queries on Bing.com and will log you in automatically using your Microsoft account.
import time
from selenium import webdriver
import main
from main import emails, passwords, testQueries


queries = ["internet", "computer", "science", "technological", "artificial intelligence", "machine learning", "cloud computing", "cybersecurity", "blockchain", "big data", "augmented reality", "virtual reality", "5G", "smart glasses","computer vision","mixed reality","spatial computing","AR cloud","biotechnology","engineering"]

for i,j in zip(emails, passwords):
        email = i
        passWord = j
        mobile_emulation = {"deviceName": "iPhone 5"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(options=chrome_options)
        main.login(driver, email, passWord)
        main.search(driver, queries)
        time.sleep(5)
        driver.quit()
