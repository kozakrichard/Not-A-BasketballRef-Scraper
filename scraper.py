import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

#totals-team, per_game-team
stats_type = "totals-team"
#year = 1998

for year in range(2021, 2022):
    url = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{year}.html&div=div_{stats_type}'
    page = requests.get(url)

    if page.status_code==200:
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')
        
    df = pd.read_html(str(table))[0]
    #df['Champion'] = 0
    #print(df)
    df.to_csv(f"{year} totals_teams.csv")




