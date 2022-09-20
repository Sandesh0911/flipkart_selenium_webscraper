
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Edge("D:\python vscode\msedgedriver.exe") #Set the path to chromedriver

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?q=phones&otracker=AS_Query_HistoryAutoSuggest_3_0&otracker1=AS_Query_HistoryAutoSuggest_3_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=3&as-type=HISTORY")
content = driver.page_source
soup = BeautifulSoup(content)

electronics = soup.findAll('a',href=True, attrs={'class':'_1fQZEK'})

for items_electronics in electronics:
    name=items_electronics.find('div', attrs={'class':'_4rR01T'})
    price=items_electronics.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=items_electronics.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text.strip())
    prices.append(price.text.strip())
    ratings.append(rating.text.strip())

df = pd.DataFrame({'Product Name':products,'Price':prices,'rating':ratings}) 
print(df)

df.to_csv(r'D:\python vscode\3. Flipkart\datacollection.csv')