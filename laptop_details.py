
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Edge("D:\python vscode\msedgedriver.exe") #Set the path to chromedriver

products=[] #List to store name of the product

prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?q=smartwatches&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smartwatches%7CSmart+Watches&requestId=3ff7f2a2-0ce9-44d8-b4d3-6aeff1572ec9&as-backfill=on")

content = driver.page_source
soup = BeautifulSoup(content)
all_laptops = soup.findAll('a',href=True, attrs={'class':'_1fQZEK'})

for laptop in all_laptops:
    name=laptop.find('div', attrs={'class':'_4rR01T'})
    price=laptop.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=laptop.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text.strip())
    prices.append(price.text.strip())
    # ratings.append(rating) 
    

df = pd.DataFrame({'Product Name':products,'Price':prices}) 
print(df)

df.to_csv(r'D:\python vscode\3. Flipkart\datacollection.csv')

