import requests
from bs4 import BeautifulSoup
# finds the 3rd parafgraph's equation and solves it and sends the solution to the server
def ihatemathematics():
    url = "https://claude.chals.hackin.ca/"

    request = requests.get(url)
    request = BeautifulSoup(request.text, "html.parser")
    data = request.findAll("p")[2]
    data = data.text
    print(data.text)
    # divide the strings into 3 parts: number, operator, number
    parts = data.split("\n")
    print(parts)