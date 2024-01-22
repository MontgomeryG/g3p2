import config, requests
from datetime import datetime
import pandas as pd

holdings = pd.read_csv('C:\\Users\\Alex\\Desktop\\FinTech-CourseWork\\Projects\\Project_2\\g3p2\\g3p2_atb\\marketDataFetcher\\backend\\data\\qqq.csv')
for holding in holdings:
    print(holding)

symbols = holdings['Holding Ticker']
symbols = ",".join(symbols)

day_bars_url = '{}/day?symbols={}&limit=1000'.format(config.BARS_URL, symbols)

request = requests.get(config.BARS_URL, headers=config.HEADERS)
data = request.json()

for symbol in data:
    filename = 'C:\\Users\\Alex\\Desktop\\FinTech-CourseWork\\Projects\\Project_2\\g3p2\\g3p2_atb\\marketDataFetcher\\backend\\data\\ohlc\\message.txt'.format(symbol)
    f = open(filename, 'w+')
    f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')

    for bar in data[symbol]:
        t = datetime.fromtimestamp(bar['t'])
        day = t.strftime('%Y-%m-%d')
        
        line = '{},{},{},{},{},{},{}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
        f.write(line)