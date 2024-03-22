from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define the URL to open
url = "https://www.google.com/"

# Set up options for headless browsing
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model

# Set up the WebDriver
driver = webdriver.Chrome(options=options)

# Open the URL
driver.get(url)

# Print the title of the page
print("Title of the page:", driver.title)

# Close the browser
driver.quit()
