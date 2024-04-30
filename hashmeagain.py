from bs4 import BeautifulSoup
import requests
import re
import hashlib
import time

def hashmeagain():
    url = "https://claude.chals.hackin.ca/"
    sol_url = "https://claude.chals.hackin.ca/solution/"

    for _ in range(1000):
        request = requests.get(url)
        request = BeautifulSoup(request.text, "html.parser")
        data = request.findAll("div", class_="message")
        print(data)
        # data = data[0].text

        expression = re.search(pattern, data, re.DOTALL)
        expression = expression.group(1)
        hText = hashlib.sha512(expression.encode()).hexdigest()
        my_url1 = sol_url + str(hText)

        submission = requests.get(my_url1)
        submission = BeautifulSoup(submission.text, "html.parser")

        expression1 = re.search(pattern, submission.text, re.DOTALL)
        expression1 = expression1.group(1).strip()

        hText1 = hashlib.sha512(expression1.encode()).hexdigest()
        my_url2 = sol_url + str(hText1)

        sub1 = requests.get(my_url2)
        print(sub1.text)

hashmeagain()
