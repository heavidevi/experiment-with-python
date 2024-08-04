from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
survey=soup.find_all('table')[0]
world_title=survey.find_all('th')[0:11]
world_table_title=[title.text.strip() for title in world_title]
world_table_title=world_table_title[0:3]+[world_table_title[3]+"/"+world_table_title[4]]+world_table_title[5:]
dataframe=pd.DataFrame(columns=world_table_title)
column_data=survey.find_all("tr")

for row in column_data[2:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]

    length=len(dataframe)
    dataframe.loc[length]=[length+1]+individual_row_data
    
print(dataframe)