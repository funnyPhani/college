import requests
from bs4 import BeautifulSoup

#keyword='phones under 10000'
keyword=input('Enter the keyword to search   :  ')
url='https://www.flipkart.com/search?q='+keyword+''

req=requests.get(url).content
#print(req)

soup=BeautifulSoup(req,'html.parser')
#print(soup.text)  # prettify()

#vertical data like mibiles laptops
data=soup.find_all('div',class_='_3wU53n')
price= soup.find_all('div',class_='_1vC4OE _2rQ-NK')


print('-'*50  +keyword+'-'*50)
for i,j in enumerate(data):
    print(i,':',j.text)
print()

#horinontal data like fans...

data=soup.find_all('a',class_='_2cLu-l')
print('!'*50  +keyword+'!'*50)
for i,j in enumerate(data):
    print(i,':',j.text)
print()

data=soup.find_all('a',class_='_2mylT6')
print('*'*50  +keyword+'*'*25)
for i,j in enumerate(data):
    print(i,':',j.text)
print()