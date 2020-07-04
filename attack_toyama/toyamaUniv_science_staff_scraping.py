import requests
from bs4 import BeautifulSoup

url = "http://www3.u-toyama.ac.jp/geochem/JP/members.html"

html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")
member = soup.find(id="member")

mailList = []

for dlTag in soup.find_all("dl"):
    mailList.append(dlTag.find("dd").text)

with open("text/mailList.txt", mode="w") as f:
    for mailAddress in mailList:
        fixMailAddress = mailAddress.replace(" * ", "＠") + "\n"
        f.write(fixMailAddress)

