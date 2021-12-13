###This scraper works to collect the league wide stats for each team per season. This data is compiled into a csv with each column
###as one statistic, and a row for each team.
###
###

import requests
from bs4 import BeautifulSoup
import pandas as pd

#For now, enter one of these into the stats_type variable
#totals-team, advanced-team, per_game-team, per_poss-team, shooting-team, all_awards

team = input("What team would you like to track? Enter the 3 letter abbreviation: ")
team = team.upper()

stat_to_track = int(input(
    "What statistics would you like to track? Enter 1 for roster. Enter 2 for per-game. 3 for season totals. 4 for per-36 minutes. 5 for per-100 possessions. 6 for advanced. 7 for adjusted shooting. 8 for shooting (available from 1997). 9 for play-by-play (available from 1997).: "
    ))

while stat_to_track != 1 and stat_to_track != 2 and stat_to_track != 3 and stat_to_track != 4 and stat_to_track != 5 and stat_to_track != 6 and stat_to_track != 7 and stat_to_track != 8 and stat_to_track != 9:
    stat_to_track = int(input("Let's try that again. Enter a valid choice between 1 and 9."))

if stat_to_track == 1:
    stats_type = "roster"
elif stat_to_track == 2:
    stats_type = "per_game"
elif stat_to_track == 3:
    stats_type = "totals"
elif stat_to_track == 4:
    stats_type = "per_minute"
elif stat_to_track == 5:
    stats_type = "per_poss"
elif stat_to_track == 6:
    stats_type = "advanced"
elif stat_to_track == 7:
    stats_type = "adj_shooting"
elif stat_to_track == 8:
    stats_type = "shooting"
elif stat_to_track == 9:
    stats_type = "pbp"
while stat_to_track != 1 and stat_to_track != 2 and stat_to_track != 3 and stat_to_track != 4 and stat_to_track != 5 and stat_to_track != 6 and stat_to_track != 7 and stat_to_track != 8 and stat_to_track != 9 :
    stat_to_track = int(input("Let's try that again. Enter a valid choice between 1 and 9: "))


start_year = int(input("Enter year to begin scraping from. Begins from 1950. Data will include this year: "))
while start_year < 1950 or start_year > 2022:
    start_year = int(input("Invalid year. Try again between 1950 and 2022: "))

end_year = int(input("Enter end year of scraping. Ends at 2023. Data will not include this year: "))
while end_year < 1950 or end_year > 2023 or end_year < start_year:
    end_year = int(input("Invalid year. Try again between 1950 and 2022: "))



for year in range(start_year, end_year):
    url = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fteams%2F{team}%2F{year}.html&div=div_{stats_type}'
    page = requests.get(url)

    if page.status_code==200:
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')
    elif page.status_code==404:
        print("Data does not exist")
        
    df = pd.read_html(str(table))[0]

#A csv file containing the data scraped will be created in this working directory
    df.to_csv(f"{team}{year} {stats_type}.csv")




