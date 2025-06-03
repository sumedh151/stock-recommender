
import json
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd 



df = pd.read_csv(r'E:\IS688\stock-recommender\baseline_financial_data.csv')
df = df[(df['stonk'] != 'MAN') & (df['stonk'] != 'ING') & (df['stonk'] != 'SEE') & (df['stonk'] != 'CAN') & (df['stonk'] != 'IRS') & (df['stonk'] != 'ANY') & (df['stonk'] != 'NYT') & (df['stonk'] != 'TOP')]
financials = df.iloc[:,0:10]

price = df.iloc[:,10:len(df.columns) - 1]

price['stonk'] = df['stonk']


financials = financials.drop(columns=['sharesShortPreviousMonthDate', 'revenueQuarterlyGrowth'])


X = financials.drop(columns=['stonk'])

scaler = StandardScaler()

X = scaler.fit_transform(X)


db = DBSCAN(eps=.9, min_samples=2).fit(X)

financials['financialLabels'] = db.	

from collections import Counter
print(Counter(db.labels_))

print(financials[financials['stonk'] == 'GME'][['stonk', 'financialLabels']])


X = price.drop(columns=['stonk'])

scaler = StandardScaler()

X = scaler.fit_transform(X)


db = DBSCAN(eps=.4, min_samples=3).fit(X)

price['priceLabels'] =db.labels_


print(Counter(db.labels_))

print(price[price['stonk'] == 'GME'][['stonk', 'priceLabels']])

df['financialLabels'] = financials['financialLabels']
df['priceLabels'] = price['priceLabels']


df.rename(columns={'labels':'allDataLabels'}, inplace=True)



df.to_csv(r'E:\IS688\stock-recommender\clustering_outcomes_analysis.csv', index=False)

tickers = df['stonk'].tolist()

with open(r'E:\IS688\stock-recommender\bets_data.json', 'r') as f:
	js = json.load(f)



text_set = []

for item in js:
	text_set.append(item['title']+ ' ' + item['body'])

text = ' '.join(text_set)

df_b = []
for stock in tickers:
	frame = {}
	frame['stock'] = stock
	frame['occurence'] = text.count(stock)
	df_b.append(frame)


df_b = pd.DataFrame(df_b)

df_b.to_csv(r'E:\IS688\stock-recommender\stock_occurences.csv', index=False)
