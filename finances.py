import json
import yfinance as yf


class Finance:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)
        self._information = None

    @property
    def information(self):
        if self._information is None:
            self._information = self.ticker.info
        return self._information
    

    def historical_stock(self):
        return self.ticker.history(period="max").reset_index()

    def financial_distance(self):
        inf = self.information
        shortRatio = inf.get('shortRatio', 0)
        entToRev = inf.get('enterpriseToRevenue', 0)
        profitMargins = inf.get('profitMargins', 0)
        enterpriseToEbitda = inf.get('enterpriseToEbitda', 0)
        revenueQuarterlyGrowth = inf.get('revenueQuarterlyGrowth', 0)
        sharesShortPreviousMonthDate = inf.get('sharesShortPreviousMonthDate', 0)
        enterpriseValue = inf.get('enterpriseValue', 0)
        sharesShort = inf.get('sharesShort', 0)
        fiftyTwoWeekLow = inf.get('fiftyTwoWeekLow', 0)
        # fiftyTwoWeekHigh = inf.get('fiftyTwoWeekHigh', 0)
        output = [shortRatio, entToRev, profitMargins, enterpriseToEbitda, revenueQuarterlyGrowth,
        sharesShortPreviousMonthDate, enterpriseValue, sharesShort, fiftyTwoWeekLow, fiftyTwoWeekLow]
        return [0 if v is None else v for v in output]


    def stock_distance(self, year='2020'):
        data = self.historical_stock()
        data['Date'] = data['Date'].astype(str)
        data = data[data['Date'].str.contains(year)]

        data[['year', 'month', 'day']] = data['Date'].str.split('-', expand=True)

        dfg = data.groupby('month').agg({'High':'mean'}).reset_index()
        return dfg['High'].tolist()


    def company_desc(self):
        return self.information.get('longBusinessSummary', 'Nothing')
    

r = Finance('BBY')

# print(r.stock_distance())