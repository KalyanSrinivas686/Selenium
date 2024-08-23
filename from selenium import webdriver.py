from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Test data
username = 'your_github_username'
password = 'your_github_password'

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Open GitHub homepage
    driver.get("https://github.com")
    
    # Step 2: Click on "Sign in" button
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_button.click()
    
    # Step 3: Enter valid username/email
    username_input = driver.find_element(By.ID, "login_field")
    username_input.send_keys(username)
    
    # Step 4: Enter valid password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    
    # Step 5: Click on "Sign in" button
    submit_button = driver.find_element(By.NAME, "commit")
    submit_button.click()
    
    # Step 6: Verify successful login by checking for the profile icon
    time.sleep(3)  # Wait for the page to load
    profile_icon = driver.find_element(By.XPATH, "//summary[@aria-label='View profile and more']")
    
    assert profile_icon is not None, "Login Failed: Profile icon not found."
    print("Login Successful: Profile icon found.")

finally:
    # Close the browser
    driver.quit()
