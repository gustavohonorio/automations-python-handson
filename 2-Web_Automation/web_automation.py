# Use Selenium to automate interactions with a website, such as logging in or submitting a form.
# Write a script to scrape data from a website and save it to a file.

# Import the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://www.google.com.br')


driver.find_element(By.NAME, 'q').send_keys('Clima agora em São Jose dos Campos')

driver.find_element(By.NAME, 'btnK').submit()

result = driver.find_element(By.ID, 'wob_tm').text

print(f'O clima em São Jose dos Campos é de {result}ºC')

driver.quit()
