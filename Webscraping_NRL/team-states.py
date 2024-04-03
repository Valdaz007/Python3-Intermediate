from bs4 import BeautifulSoup
import requests
import json

# Arguments
import argparse
argsCon = argparse.ArgumentParser()
argsCon.add_argument('round', metavar='round', type=int, help='Current round')
argsCon.add_argument('team', metavar='team', type=int, help='Team')
args = argsCon.parse_args()
round = args.round
team = args.team

# Subprocess
import subprocess

#? CONSOLE PRINT STYLE
from rich.table import Table
from rich.console import Console

# GET CURRENT ROUND TEAM DRAWS
def get_Round_Draw(season:int, round:int) -> list:
    pg = requests.get(f"https://www.nrl.com/draw/?competition=111&round={round}&season={season}").text
    pg_draw = BeautifulSoup(pg, "html.parser").find('div', id="vue-draw")
    roundDraw = pg_draw.attrs['q-data']
    dictRound = json.loads(roundDraw)
    return [f"{i['homeTeam']['nickName']}-v-{i['awayTeam']['nickName']}".lower() for i in dictRound['fixtures']]

# GET CURRENT ROUND TEAM STATS
def get_Team_Stats(teams:str, round:int) -> dict:
    pg = requests.get(f"https://www.nrl.com/draw/nrl-premiership/2024/round-{round}/{teams.replace(' ', '-')}/#tab-match-center-2'").text
    pg_stats = BeautifulSoup(pg, "html.parser").find('div', id="vue-match-centre")
    return json.loads(pg_stats.attrs['q-data'])

# CONSOLE PRINT TABLE DISPLAY
def get_Team_Form(stats_Dict:dict) -> None:
    homeTable = Table()
    homeTable.add_column('Result')
    homeTable.add_column('Opposition')
    homeTable.add_column('Score')


    for i in stats_Dict['match']['homeTeam']['recentForm']:
        homeTable.add_row(i['result'], i['summary'], i['score'])

    awayTable = Table()
    awayTable.add_column('Result')
    awayTable.add_column('Opposition')
    awayTable.add_column('Score')


    for i in stats_Dict['match']['awayTeam']['recentForm']:
        awayTable.add_row(i['result'], i['summary'], i['score'])
    
    formConsole = Console()
    vsTable = Table()
    vsTable.add_column(f"{stats_Dict['match']['homeTeam']['nickName']} {stats_Dict['match']['homeTeam']['odds']}")
    vsTable.add_column(f"{stats_Dict['match']['awayTeam']['nickName']} {stats_Dict['match']['awayTeam']['odds']}")
    vsTable.add_row(homeTable, awayTable)
    formConsole.print(vsTable)

if __name__ == "__main__":
    teams_Match = get_Round_Draw(2024, round)
    while True:
        dict_Stats = get_Team_Stats(teams_Match[team], round)
        get_Team_Form(dict_Stats)
        inp = input('Press Enter to Continue or Q to Quit: ')
        subprocess.run('cls', shell=True)
        if inp=='Q' or inp=='q': break
        elif team == 7: team = 0
        else: team+=1
