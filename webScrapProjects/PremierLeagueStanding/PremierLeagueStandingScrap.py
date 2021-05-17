import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

#url="https://www.skysports.com/premier-league-table"
def get_league_table(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    tablelist = []
    league_table=soup.find("table",class_="standing-table__table callfn")

    for team in league_table.find_all("tbody"):
        rows = team.find_all("tr")
        for row in rows:
          pl_team=row.find("td",class_="standing-table__cell standing-table__cell--name").text.strip()
          pl_position=row.find_all("td",class_="standing-table__cell")[0].text
          pl_playedMatch=row.find_all("td",class_="standing-table__cell")[2].text
          pl_won=row.find_all("td",class_="standing-table__cell")[3].text
          pl_drawn=row.find_all("td",class_="standing-table__cell")[4].text
          pl_lost=row.find_all("td",class_="standing-table__cell")[5].text
          goals_for=row.find_all("td",class_="standing-table__cell")[6].text
          goals_against=row.find_all("td",class_="standing-table__cell")[7].text
          goal_difference=row.find_all("td",class_="standing-table__cell")[8].text
          pl_points = row.find_all("td", class_="standing-table__cell")[9].text

          teamInLeague={
              "position":pl_position,
              "name":pl_team,
              "playedMatch":pl_playedMatch,
              "won":pl_won,
              "drawn":pl_drawn,
              "lost":pl_lost,
              "goalsFor":goals_for,
              "goalsAgainst":goals_against,
              "goalDifference":goal_difference,
              "points":pl_points
          }
          tablelist.append(teamInLeague)
    return tablelist

data=get_league_table("https://www.skysports.com/premier-league-table")

df=pd.DataFrame(data)
df.to_csv("plleaguetable.csv")
df.to_excel("plleaguetable.xlsx")
print("saved to file")