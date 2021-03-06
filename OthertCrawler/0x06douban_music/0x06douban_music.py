import requests
import re
import csv
from bs4 import BeautifulSoup

url = "https://music.douban.com/chart"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'lxml')
source = str(soup.find_all(attrs={"class": "col5"}))
#print(source)

pattern = re.compile('<li.*?"green-num-box">(.*?)</span>.*?<a href="javascript:;">(.*?)</a>.*?<p>(.*?)</p>', re.S | re.I)#.*?<p>(.*?)</p>
items = re.findall(pattern, source)

#写入csv文件
"""
with open('db music.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['排名', '歌名                  ', '歌手和播放数量'])
    writer.writerows(items)
"""
#写入txt文件
for item in items:
    string = str(item)
    with open('db music.txt', 'a') as f:
        f.write(string+'\n')
    f.close()


