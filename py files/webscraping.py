from bs4 import BeautifulSoup
import requests
url= "http://www.opensourcesports.com/hockey/"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html") #parsing data into from htl format to another text format
#print(soup.pretify) ----use this to view html heirchy form
#soup.find("div") #finds the first div in html
#soup.find_all("div") #finds all divs characters ued in soup.
#soup.find_all("div",class="") #we can find that div which consist of concerning class assosciated with it.
#soup.find_all("div",class="").text.strip() #we can find that div which consist of concerning class assosciated with it.+ we can erase all extra and keep the neccesary inforamtion

