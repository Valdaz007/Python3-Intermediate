from bs4 import BeautifulSoup
import requests
import json

#? STYLE
from rich.table import Table
from rich.console import Console

#? TABLE
table = Table(title='Round 4')
table.add_column('Home Team')
table.add_column('Placing')
table.add_column('vs')
table.add_column('Away Team')
table.add_column('Placing')


season = 2024
round = 4
url = f"https://www.nrl.com/draw/?competition=111&round={round}&season={season}"


pg = requests.get(url).text

doc = BeautifulSoup(pg, "html.parser")
pg_draw = doc.find('div', id="vue-draw")

round4 = pg_draw.attrs['q-data']
dictround4 = json.loads(round4)

for i in dictround4['fixtures']:
    table.add_row(i['homeTeam']['nickName'], i['homeTeam']['teamPosition'], ' ', i['awayTeam']['nickName'], i['awayTeam']['teamPosition'])

console = Console()
console.print(table)