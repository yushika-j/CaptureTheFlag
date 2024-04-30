import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# Create a WebDriver instance
driver = webdriver.Chrome()  # You may need to adjust this based on your WebDriver's location

for i in range(1000):
    # Fetch the webpage
    driver.get("https://claude.chals.hackin.ca/")
    
    # Extracting the calculation from the webpage
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data = soup.findAll("p")[2].text

    # Split the data into 3 parts
    pattern = data.split(" ")
    num1, op, num2 = pattern[0], pattern[1], pattern[2]

    # Perform the calculation
    result = eval(f"{num1} {op} {num2}")

    # Print the result
    print(result)

    # Send the result to the input box of the website using Selenium
    input_box = driver.find_element_by_name("input")
    input_box.clear()
    input_box.send_keys(str(result))

    # Submit the form
    submit_button = driver.find_element_by_xpath("//input[@type='submit']")
    submit_button.click()

# Close the WebDriver session
driver.quit()
