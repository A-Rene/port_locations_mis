# get information about the ports along the mississippi river 
# get data from website 
    #http://www.worldportsource.com/waterways/Mississippi_River_120.php
from bs4 import BeautifulSoup 
import requests 
import re 

information_source = requests.get('http://www.worldportsource.com/waterways/Mississippi_River_120.php').text

soup = BeautifulSoup(information_source, 'lxml')

# find the states that the ports are in 
cities = soup.find_all('td',)

information_list = []

for x in cities:
    x = x.text.strip()
    
    # remove unwanted information from the list 
    y = re.sub('\(\d{1}\d{1}\)', "", x)
    f = re.sub('\(\d{1}\)', "" ,y)
    g = re.sub('\*', "", f)
    b =  re.sub('Top', '', g)
    information_list.append(b)

information_list.remove('')  
information_list.remove('')  


for x in information_list:
    print(x)














