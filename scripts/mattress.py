import requests
from bs4 import BeautifulSoup

url = "https://vancouver.ca/home-property-development/how-to-dispose-of-mattresses.aspx"
page = requests.get(url)
#print(page.content)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="contentContainer")
container = results.find_all("div", class_="blk-content padding-right-eq70")

f= open("./data/mattress.txt","w+")
for i in container:
      f.write(i.text)
f.write(url)
f.close()

# Append-adds at last
#file1 = open("myfile.txt","a")#append mode
#file1.write("Today \n")
#file1.close()