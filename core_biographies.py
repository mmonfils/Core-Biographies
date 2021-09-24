import pandas as pd
import requests

# Writing a script to retrieve and locally save the data
# from the Wikipedia website

url = "https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Biography/" \
    "Core_biographies/list"

r = requests.get(url)
df_list = pd.read_html(r.text)
df = df_list[0]
df.to_csv('core_biographies.csv', index=False)
