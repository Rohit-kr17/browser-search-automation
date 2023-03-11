# Description: This script will search for a list of queries on Bing.com and will log you in automatically using your Microsoft account.
import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By



load_dotenv()  # load environment variables from .env file
email0 = os.getenv("EMAIL0")  # Your email address from .env file
passWord0 = os.getenv("PASSWORD0") # Your password from .env file
email1 = os.getenv("EMAIL1") # Your email address from .env file
passWord1 = os.getenv("PASSWORD1") # Your password from .env file
email2 = os.getenv("EMAIL2") # Your email address from .env file
passWord2 = os.getenv("PASSWORD2") # Your password from .env file
url = "https://www.bing.com/" # Search engine URL

# creating a list of email addresses from os.getenv
emails = [email1, email0, email2]
# creating a list of passwords from os.getenv
passwords = [passWord1, passWord0, passWord2]
testQueries = ["Hi", "world quant"]  # this is a test query

# Navigate to the login page
def login(driver_,email_,passWord_):
    email = email_
    passWord = passWord_
    driver = driver_
    driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d16C20CCD6A2B602D072F1E026BD9618B&wp=MBI_SSL&lc=1033&CSRFToken=0843d6ef-a4de-43ce-8ec6-189f121347b6&aadredir=1")
    time.sleep(2)
    email_field = driver.find_element(By.ID, "i0116")
    email_field.send_keys(email)
    time.sleep(2)
    next_button = driver.find_element(By.ID, "idSIButton9")
    next_button.click()
    time.sleep(2)
    password_field = driver.find_element(By.ID, "i0118")
    password_field.send_keys(passWord)
    time.sleep(2)
    next_button = driver.find_element(By.ID, "idSIButton9")
    next_button.click()
    time.sleep(2)
    next_button = driver.find_element(By.ID, "idSIButton9")
    next_button.click()
    time.sleep(5)

def search(driver_, queries_):
    driver = driver_
    queries = queries_
    for query in queries:
        # Load the search engine page with the current query
        driver.get(url)
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()
        time.sleep(1)

if __name__ == "__main__":
    # Initialize a new instance of the Chrome driver
    # List of search queries
    queries = ["Artificial intelligence", "Blockchain technology", "Cloud computing", "Data analytics", "Cybersecurity", "Internet of Things (IoT)", "Virtual reality", "Augmented reality", "Machine learning", "Quantum computing", "3D printing", "Robotics", "Biotechnology", "Neural networks", "Natural language processing",
        "Big data", "Cryptocurrency", "Edge computing", "Fintech",    "Smart homes",    "Smart cities",    "Wireless technology",    "Autonomous vehicles",    "Drones",    "Gaming",    "Mobile devices",    "Social media",    "E-commerce",    "Digital transformation",    "Wearable technology"]
    
    for i,j in zip(emails, passwords):
        email = i
        passWord = j
        driver = webdriver.Chrome()
        login(driver, email, passWord)
        search(driver, queries)
        time.sleep(5)
    driver.quit()
