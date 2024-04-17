import requests
from bs4 import BeautifulSoup

def ihatemathematics():
    url = "http://challenges.ringzer0team.com:10032/"
    sol_url = "http://challenges.ringzer0team.com:10032/?r=" 

    request = requests.get(url)
    request = BeautifulSoup(request.text, "html.parser")
    data = request.find_all("div", class_= "message")
    data = data[0].text.strip()
    inner_message = data.split('\n')[1].strip()
    numbers = inner_message.split(" ")
    a,s1,b,s2,c = (
        numbers[0],
        numbers[1],
        numbers[2],
        numbers[3],
        numbers[4]
    )
    a = int(a)
    b = int(b,16)
    c = int(c,2)

    variable = eval(str(a) + s1 + str(b) + s2 + str(c))
    
    sol_url = sol_url + str(variable)
    submission = requests.get(sol_url)
    submission = BeautifulSoup(submission.text, "html.parser" )
    
    print(submission.text)
    
    
    
    
print(ihatemathematics())