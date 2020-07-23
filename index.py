import pandas as pd
from generate_indicator import generate_indicator
from generate_stopper import generate_stopper
from get_html import get_html
import time

website = 'lazada'
file_path = '/Users/ziyu/Desktop/lego/listings.csv'
column = 'Listing URL'
sleep_time = 10

indicator = generate_indicator(website)
stopper = generate_stopper(website)
data = pd.read_csv(file_path)
for i in range(len(data)):
    if str(data.iloc[i][column + ' still active']) != 'nan':
        continue
    url = data.iloc[i][column]
    html = get_html(url)
    if stopper in html:
        break
    has_indicator = indicator in html
    data.at[i, column + ' still active'] = 1 if has_indicator else 0
    if i % 10 == 9:
        data.to_csv(file_path, encoding='utf-8')
    print('Finished No. %d' % i)
    time.sleep(sleep_time)

data.to_csv(file_path, encoding='utf-8')
