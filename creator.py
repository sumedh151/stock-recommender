import json

from finances import Finance
from vectors import term_vectorizer_fit, vectorizer_transform
import pandas as pd

# with open(r'E:\IS688\stock-recommender\baseline_price.json', 'r') as f:
with open(r'baseline_price.json', 'r') as f:
    js = json.load(f)


new_set = []

for item  in js:
    frame = {}
    key = list(item.keys())[0]
    value = list(item.values())[0]
    frame['stonk'] = key
    counter = 0
    for v in value:
        counter += 1
        frame['m'+ str(counter)] = v
    new_set.append(frame)

# print(new_set)

stock =pd.DataFrame(new_set)

# with open(r'E:\IS688\stock-recommender\baseline_financials.json', 'r') as f:
with open(r'baseline_financials.json', 'r') as f:
    js = json.load(f)


new_set = []

for item  in js:
    frame = {}
    key = list(item.keys())[0]
    value = list(item.values())[0]
    frame['stonk'] = key
    frame['shortRatio'] = value[0]
    frame['entToRev'] = value[1]
    frame['profitMargin'] = value[2]
    frame['enterpriseToEbitda'] = value[3]
    frame['revenueQuarterlyGrowth'] = value[4]
    frame['sharesShortPreviousMonthDate'] = value[5]
    frame['enterpriseValue'] = value[6]
    frame['sharesShort'] = value[7]
    frame['fiftyTwoWeekLow'] = value[8]
    new_set.append(frame)

finance =pd.DataFrame(new_set)

df = finance.merge(stock, on='stonk', how='left')


df.fillna(0, inplace=True)
print(df)
# new_set= []
# for x in js:
#     if len(x['stonks']) > 1:
#         new_set.append(x)

# print(len(new_set))

# main = pd.read_csv(r'E:\IS688\stock-recommender\baseline_dataframe.csv')

# finance = pd.DataFrame(new_set)


# main_df = main.merge(finance, on='stonk', how='left').dropna()




# text = vectorizer_transform(main_df['text'], 'descriptions_vectors.pickle')

# print(main_df)


from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

X = df.drop(columns=['stonk'])

scaler = StandardScaler()

X = scaler.fit_transform(X)


db = DBSCAN(eps=1.1, min_samples=2).fit(X)

df['labels'] =db.labels_
from collections import Counter
print(Counter(db.labels_))

# df = df[df['stonk'] == 'NOK']
print(df[['stonk', 'labels']])

df.to_csv('baseline_financial_data.csv', index=False)
# print(new_set[0].keys())

# df_builder = []
# for item in new_set:
#     frame = {}
#     for val in item['stonks']:

#         frame['stonk'] = val
#         frame['text'] = item['title'] + item['body']

#         frame['score'] = item['score']
#         df_builder.append(frame)


# import pandas as pd

# df = pd.DataFrame(df_builder).drop_duplicates()

# df = df[df['stonk'] != 'CNN']
# print(df)

# df.to_csv('baseline_dataframe.csv', index=False)


# print(js)

# l = []
# for i in js:
#     # print(i.values())
#     for item in i.values():
#         l.append(item)

# # print(l)

# fit = term_vectorizer_fit(l)

# import pickle

# pickle.dump(fit, open(r"E:\IS688\stock-recommender\descriptions_vectors.pickle", "wb"))



# stonks = set()

# new_list = []
# for i in js:
#     for x in i['stonks']:
#         # for s in x['stonks']:
#         stonks.add(x)

# print(len(stonks))

# # print(stonks)

# price_base = []
# company_des = []
# company_fin = []
# i = 0
# for stock in stonks:
#     try:
#         # stock = 'MSFT'
#         f = Finance(stock)
#         company_fin.append({stock: f.financial_distance()})
#         company_des.append({stock: f.company_desc()})
#         price_base.append({stock: f.stock_distance()})
#     except:
#         pass
#     print(i, stock)
#     i = i + 1


# with open(r'E:\IS688\stock-recommender\baseline_price.json', 'w') as f:
#     f.write(json.dumps(price_base))

# with open(r'E:\IS688\stock-recommender\baseline_des.json', 'w') as f:
#     f.write(json.dumps(company_des))

# with open(r'E:\IS688\stock-recommender\baseline_financials.json', 'w') as f:
#     f.write(json.dumps(company_fin))


