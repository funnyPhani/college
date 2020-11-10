
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
 
url = 'https://www.flipkart.com/search?q=mobiles'
 
res = requests.get(url).content
 
soup = BeautifulSoup(res,'html.parser')
 
titles = soup.find_all('div',class_='_3wU53n')
ratings  =soup.find_all('div',class_='hGSR34') 
reviews  =soup.find_all('span',class_='_38sUEc') 
prices  =soup.find_all('div',class_='_1vC4OE _2rQ-NK') 
 
mobiles = []
m_ratings =[]
m_reviews =[]
m_prices =[]
 
 
 
for title,rating,review,price in zip(titles,ratings,reviews,prices):
    #print(c, title.text,rating.text,review.text,price.text)
    mobiles.append(title.text)
    m_ratings.append(rating.text)
    m_reviews.append(review.text)
    m_prices.append(price.text)
     
 
# Exporting to CSV files
 
data = {'mobiles':mobiles,'ratings':m_ratings,'reviews':m_reviews,'prices':m_prices}
 
df = pd.DataFrame(data=data)
 
print(df.head())
 
df.to_csv('mobile_data.csv',index=False)
print('Success..!')
 
df.to_json('content.json',orient='records')
# Exporting to JSON
d = json.dumps(data)
#print(d)
 
l = json.loads(d)
 
with open('mobile_data.json','w') as f:
    f.write(d)
    f.close()
     
print('Success..!')