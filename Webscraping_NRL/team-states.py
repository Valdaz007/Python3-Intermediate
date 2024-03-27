from bs4 import BeautifulSoup
import requests
import json

#? CONSOLE PRINT STYLE
from rich.table import Table
from rich.console import Console

def get_Round_Draw(season:int, round:int) -> list:
    pg = requests.get(f"https://www.nrl.com/draw/?competition=111&round={round}&season={season}").text
    pg_draw = BeautifulSoup(pg, "html.parser").find('div', id="vue-draw")
    round4 = pg_draw.attrs['q-data']
    dictround4 = json.loads(round4)
    return [f"{i['homeTeam']['nickName']}-v-{i['awayTeam']['nickName']}".lower() for i in dictround4['fixtures']]

def get_Team_Stats(teams:str) -> dict:
    pg = requests.get(f"https://www.nrl.com/draw/nrl-premiership/2024/round-4/{teams}/#tab-team-stats'").text
    pg_stats = BeautifulSoup(pg, "html.parser").find('div', id="vue-match-centre")
    return json.loads(pg_stats.attrs['q-data'])

def get_Team_Form(stats_Dict:dict) -> None:
    formTable = Table(title=dict_Stats['match']['homeTeam']['nickName'])
    formTable.add_column('Result')
    formTable.add_column('Opposition')
    formTable.add_column('Score')


    for i in dict_Stats['match']['homeTeam']['recentForm']:
        formTable.add_row(i['result'], i['summary'], i['score'])
    
    formConsole = Console()
    formConsole.print(formTable)
    

if __name__ == "__main__":
    teams_Match = get_Round_Draw(2024, 4)
    dict_Stats = get_Team_Stats(teams_Match[0])
    # print(dict_Stats['match']['homeTeam']['recentForm'])
    get_Team_Form(dict_Stats)