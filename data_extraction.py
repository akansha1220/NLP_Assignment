import requests
from bs4 import BeautifulSoup
import pandas as pd
from config import Config

config = Config()




# first thing I have to do is to extract the data from every url one by one

# In the extract function I will scrap the data from url usin
def extract_data(url):
    try:
        response = requests.get(url)
        url_data = BeautifulSoup(response.content,'html.parser')   # extractting the whole data

        # extracting the article title and article text
        url_title = url_data.find('title').get_text().strip()  # Assuming <h1> is used for titles
        url_text = url_data.find('div', class_='td-post-content').get_text() .strip()

        # return the article title and article text
        return url_title,url_text
    
    except Exception as e:
        print(f"Error comming while reading the url which is {e}")
        return None,None


data = pd.read_excel(config.INPUT_FILE_PATH)
# read the Url one by one
total_row = data.shape                 #here extarcted the shape and then to get the url one by one i play a loop


for i in range(total_row[0]):
        title,content=extract_data(data.URL[i])                   # here i am passing the url in the extract data function

        #Here 

        if content:
             with open(f"{config.EXTRACTED_FILE_PATH}/{data.URL_ID[i]}.txt",'w',encoding= 'utf-8') as f:
                  f.write(f"{title} \n\n{content}")
                  print(f"file saved {data.URL[i]}")
        else:
             print(f'Error occur while extracting the data {data.URL_ID[i]}')