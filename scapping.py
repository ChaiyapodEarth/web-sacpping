from bs4 import BeautifulSoup
import requests
url = "https://pantip.com/forum/korea"
data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')
# <- ค่าที่ใช้ในการค้นหา
x = soup.find_all("h2")

for i in x:
    print(i.text)
