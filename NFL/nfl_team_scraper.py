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
team = team.lower()

stat_to_track = int(input(
    "What statistics would you like to track? Enter 1 for team stats. Enter 2 for all games that season. 3 for team conversions. 4 for passing. 5 for rushing and receiving. 6 for returns. 7 for kicking. 8 for defense. 9 for scoring summary. 10 for team touchdown log. 11 for opponent's touchdown log.: "
    ))

while stat_to_track != 1 and stat_to_track != 2 and stat_to_track != 3 and stat_to_track != 4 and stat_to_track != 5 and stat_to_track != 6 and stat_to_track != 7 and stat_to_track != 8 and stat_to_track != 9 and stat_to_track != 10 and stat_to_track != 11:
    stat_to_track = int(input("Let's try that again. Enter a valid choice between 1 and 11."))

if stat_to_track == 1:
    stats_type = "team_stats"
elif stat_to_track == 2:
    stats_type = "games"
elif stat_to_track == 3:
    stats_type = "team_conversions"
elif stat_to_track == 4:
    stats_type = "passing"
elif stat_to_track == 5:
    stats_type = "rushing_and_receiving"
elif stat_to_track == 6:
    stats_type = "returns"
elif stat_to_track == 7:
    stats_type = "kicking"
elif stat_to_track == 8:
    stats_type = "defense"
elif stat_to_track == 9:
    stats_type = "scoring"
elif stat_to_track == 10:
    stats_type = "team_td_log"
elif stat_to_track == 11:
    stats_type = "opp_td_log"
while stat_to_track != 1 and stat_to_track != 2 and stat_to_track != 3 and stat_to_track != 4 and stat_to_track != 5 and stat_to_track != 6 and stat_to_track != 7 and stat_to_track != 8 and stat_to_track != 9 and stat_to_track != 10 and stat_to_track != 11 :
    stat_to_track = int(input("Let's try that again. Enter a valid choice between 1 and 11: "))

start_year = int(input("Enter year to begin scraping from. Begins from 1950. Data will include this year: "))
while start_year < 1950 or start_year > 2022:
    start_year = int(input("Invalid year. Try again between 1950 and 2022: "))

end_year = int(input("Enter end year of scraping. Ends at 2023. Data will not include this year: "))
while end_year < 1950 or end_year > 2023 or end_year < start_year:
    end_year = int(input("Invalid year. Try again between 1950 and 2022: "))


for year in range(start_year, end_year):
    url = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=pfr&url=%2Fteams%2F{team}%2F{year}.htm&div=div_{stats_type}'
    page = requests.get(url)

    if page.status_code==200:
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table')
    elif page.status_code==404:
        print("Data does not exist")
        
    df = pd.read_html(str(table))[0]

#A csv file containing the data scraped will be created in this working directory
    df.to_csv(f"{team}{year} {stats_type}.csv")




