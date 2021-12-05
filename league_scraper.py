import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

#For now, enter one of these into the stats_type variable
#totals-team, advanced-team, per_game-team, per_poss-team, shooting-team, all_awards

stats_type = "per_poss-team"

start_year = int(input("Enter year to begin scraping from. Begins from 1950. Data will include this year: "))
while start_year < 1950 or start_year > 2022:
    start_year = int(input("Invalid year. Try again between 1950 and 2022: "))

end_year = int(input("Enter end year of scraping. Ends at 2023. Data will not include this year: "))
while end_year < 1950 or end_year > 2023:
    end_year = int(input("Invalid year. Try again between 1950 and 2022: "))



for year in range(start_year, end_year):
    url = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{year}.html&div=div_{stats_type}'
    page = requests.get(url)

    if page.status_code==200:
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')
    elif page.status_code==404:
        print("Data does not exist")
        
df = pd.read_html(str(table))[0]

#A csv file containing the data scraped will be created in this working directory
df.to_csv(f"{year} {stats_type} totals.csv")




