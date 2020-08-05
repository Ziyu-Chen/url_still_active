import pandas as pd
from generate_indicator import generate_indicator
from generate_stopper import generate_stopper
from get_html import get_html
from requests.exceptions import ConnectionError
from requests.exceptions import ChunkedEncodingError
import time

website = 'lazada'
file_path = '/Users/ziyu/Desktop/lego/listings.csv'
column = 'Listing URL'
sleep_time = 5

indicator = generate_indicator(website)
stopper = generate_stopper(website)
data = pd.read_csv(file_path)
i = 0
while i < len(data):
    if str(data.iloc[i][column + ' still active']) != 'nan':
        i += 1
        continue
    url = data.iloc[i][column]
    try:
        html = get_html(url)
        if stopper in html:
            print('The anti-webscrapping mechanism of this website is on.')
            break
        has_indicator = indicator in html
        data.at[i, column + ' still active'] = 1 if has_indicator else 0
        if i % 10 == 9:
            data.to_csv(file_path, encoding='utf-8')
        print('Finished No. %d' % i)
        i += 1
        time.sleep(sleep_time)
    except ConnectionError:
        time.sleep(sleep_time)
        continue
    except ChunkedEncodingError:
        time.sleep(sleep_time)
        continue
    except Exception:
        break

data.to_csv(file_path, encoding='utf-8')
