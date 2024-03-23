# Used to import the webdriver from selenium
from selenium import webdriver  
from selenium.webdriver.common.by import By

# import things to get env vars
from dotenv import load_dotenv
import os

#  load env vars
load_dotenv()

# get env vars
# --- info user
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
url = os.getenv("URL")

# --- website ID's
username_id = os.getenv("USERNAME_INPUT")
password_id = os.getenv("PASS_INPUT")
submit_id = os.getenv("SUBMIT_INPUT")


def initBot():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
     
    # initialize driver for chrome
    driver = webdriver.Chrome(options=options)
     
    # open url on chrome
    driver.get(url)
     
    # get user and pass input for username and pass
    # add content on them
    driver.find_element(By.ID,username_id).send_keys(username) # username input
    driver.find_element(By.ID, password_id).send_keys(password) # password input

    # click on login button 
    driver.find_element(By.ID, submit_id).click() # click on submit button
 
    driver.close()

if __name__ == "__main__" :
    # init bot
    initBot()
