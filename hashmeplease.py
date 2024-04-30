from bs4 import BeautifulSoup
import requests
import re
import hashlib


def hashmeplease():
    url = "https://claude.chals.hackin.ca/"
    sol_url = "https://claude.chals.hackin.ca/"

    request = requests.get(url)
    request = BeautifulSoup(request.text, "html.parser")
    data = request.findAll("p")[2]
    print(data)

    # create pattern
    pattern = r"----- BEGIN MESSAGE -----\s*(.*?)\s*----- END MESSAGE -----"
    
    
    
   
    text= expression.group(1)
    #print(text)
    
    #hashing algorithm
    
    
    submission = BeautifulSoup(submission.text, "html.parser" )
    print(submission.text)
print(hashmeplease())