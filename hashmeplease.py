from bs4 import BeautifulSoup
import requests
import re
import hashlib


def hashmeplease():
    url = "http://challenges.ringzer0team.com:10013/"
    sol_url = "http://challenges.ringzer0team.com:10013/?r=" 

    request = requests.get(url)
    request = BeautifulSoup(request.text, "html.parser")
    data = request.findAll("div", class_= "message")
    #print(data[0].text)

    # create pattern
    pattern = r"----- BEGIN MESSAGE -----\s*(.*?)\s*----- END MESSAGE -----"
    
    data = data[0].text
    
    expression = re.search(pattern, data, re.DOTALL)
    text= expression.group(1)
    #print(text)
    
    #hashing algorithm
    hText = hashlib.sha512(text.encode()).hexdigest()
    sol_url = sol_url + hText
    submission = requests.get(sol_url)
    submission = BeautifulSoup(submission.text, "html.parser" )
    print(submission.text)
print(hashmeplease())