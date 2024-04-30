import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re

#  8736 - 228 = ? - find a pattern that matches this
for i in range(1000):
    soup = BeautifulSoup(requests.get("https://claude.chals.hackin.ca/").text,"html.parser")
    data = soup.findAll("p")[2].text

    # split the data into 3 parts
    pattern = data.split(" ")
    num1,op,num2 = (
            pattern[0],
            pattern[1],
            pattern[2]
        )

    result = eval(str(num1) + op + str(num2))
    print(result)

    #send the input to the textbox in the website using html parser
    response = requests.post("https://claude.chals.hackin.ca/", data={"input": result})
    

