# Coursera_capstone__Part-I
I am working in the final assessment 
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("Hello Capstone Project Course!")


url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M,'

import requests
import lxml.html as lh
import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request


url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
data = requests.get(url).text
soup = bs.BeautifulSoup(data,'lxml')
tables = soup.find_all('table')[0]
df = pd.read_html(str(tables))
canada_data = pd.read_json(df[0].to_json(orient='records'))
canada_data.head()

canada_selected = canada_data[canada_data['Borough'] != 'Not assigned']
canada_selected = canada_selected.groupby(['Borough', 'Postal Code'], as_index=False).agg(','.join)
canada_selected

canada_selected['Neighbourhood'] = np.where(canada_selected['Neighbourhood'] == 'Not assigned', canada_selected['Borough'], canada_selected['Neighbourhood'])
canada_selected.shape
