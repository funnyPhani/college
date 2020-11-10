
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


#url='https://www.wedmegood.com/vendors/hyderabad/planners/'
city=str(input('enter the city name to search wedding planners  : '))
pagenum=input('enter the num of pages to scrape data : ')
url='https://www.wedmegood.com/vendors/{}/planners/?page={}'.format(city,pagenum)
req=requests.get(url).content

#print(req.status_code)

soup=BeautifulSoup(req,'html.parser')

infos=soup.find_all('div',class_='vendor-info')

c=1
#print(info)

planners=[]
locations=[]
reviews=[]
ratings=[]
prices=[]

for page in range(0,int(pagenum)):
    for info in infos:

        planner=info.find('a',class_='vendor-detail')
        #print(c,'-',planner.text.strip())
        planners.append(planner.text.strip())

        rating=info.find('span',class_='StarRating')
        #print(rating.text.strip())
        ratings.append(rating.text.strip())

        loc=info.find('p',class_='vendor-detail')
        #print(loc.text.strip())
        locations.append(loc.text.strip())


        review=info.find('span',class_='review-cnt')
        #print(reviews.text.strip())
        reviews.append(review.text.strip())

        price=info.find('span',class_="")
        #print(price.text.strip()) 
        prices.append(price.text.strip())
        #print('-'*50)

        #c+=1


data={'Planner':planners,'Rating':ratings,'Location':locations,'Review-Count':reviews,'Price':prices}

df=pd.DataFrame(data=data)

print(df.head())

df.to_csv('wedding.csv',index=False)
print('-'*50)
print('csv created')

sns.countplot(df['Rating'])
plt.show()

'''
fig, ax1 = plt.subplots()
plt.figure(figsize=(10,10))
fig.autofmt_xdate()
sns.catplot(x='Price',y='Rating',data=df)
plt.show()

'''




