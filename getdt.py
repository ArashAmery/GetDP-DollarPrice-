import requests
from bs4 import BeautifulSoup
request = requests.get("https://donya-e-eqtesad.com/tags/%D9%82%DB%8C%D9%85%D8%AA_%D8%AF%D9%84%D8%A7%D8%B1")
if(request.status_code == 200):
    pass
else:
    print("can't conection")