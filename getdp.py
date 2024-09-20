import requests
from bs4 import BeautifulSoup
from re import findall

def get_dp():
    request = requests.get("https://donya-e-eqtesad.com/tags/%D9%82%DB%8C%D9%85%D8%AA_%D8%AF%D9%84%D8%A7%D8%B1")
    if(request.status_code == 200):
        soup = BeautifulSoup(request.text,"html.parser")
        td = soup.findAll("td")
        DP = findall("<.*td.*?>(.*).*<span",str(td[5]))[0]
        return DP
    else:
        return str(request.status_code)
