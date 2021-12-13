###This scraper works to collect the league wide stats for each team per season. This data is compiled into a csv with each column
###as one statistic, and a row for each team.
###
###all_awards is the only exception, this collects the winners of the highest league awards, MVP, DPOTY, etc...

import requests
from bs4 import BeautifulSoup
import pandas as pd

#For now, enter one of these into the stats_type variable
#totals-team, advanced-team, per_game-team, per_poss-team, shooting-team, all_awards

stat_to_track = int(input(
    "What statistics would you like to track? Enter 1 for totals. 2 for advanced. 3 for per-game. 4 for per-100 possessions. 5 for shooting. 6 for awards. "
    ))

while stat_to_track != 1 and stat_to_track != 2 and stat_to_track != 3 and stat_to_track != 4 and stat_to_track != 5 and stat_to_track != 6:
    stat_to_track = int(input("Let's try that again. Enter a valid choice between 1 and 6."))

if stat_to_track == 1:
    stats_type = "totals-team"
elif stat_to_track == 2:
    stats_type = "advanced-team"
elif stat_to_track == 3:
    stats_type = "per_game-team"
elif stat_to_track == 4:
    stats_type = "per_poss-team"
elif stat_to_track == 5:
    stats_type = "shooting-team"
elif stat_to_track == 6:
    stats_type = "all_awards"
while stat_to_track != 1 and stat_to_track != 2 and stat_to_track != 3 and stat_to_track != 4 and stat_to_track != 5 and stat_to_track != 6:
    stat_to_track = int(input("Let's try that again. Enter a valid choice between 1 and 6: "))


start_year = int(input("Enter year to begin scraping from. Begins from 1950. Data will include this year: "))
while start_year < 1950 or start_year > 2022:
    start_year = int(input("Invalid year. Try again between 1950 and 2022: "))

end_year = int(input("Enter end year of scraping. Ends at 2023. Data will not include this year: "))
while end_year < 1950 or end_year > 2023 or end_year < start_year:
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
    df.to_csv(f"NBA{year} {stats_type} totals.csv")




