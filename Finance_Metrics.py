import numpy as np
import pandas as pd
import yfinance as yf
from datetime import date

def beta_calculator(returns):
    stocks_cov = returns.cov()[composite]
    mkt_var = returns[composite].var()
    beta = stocks_cov/mkt_var
    return beta
def cleaner(string):
    string = str(string)
    for character in characters_to_remove:
          string = string.replace(character, "")
    return string
characters_to_remove = "['']"

portfolio = []
composite = []

portfolio = [item for item in input("Enter the list of stocks: ").split()]
composite = [item for item in input("Enter the composite: ").split()]
Risk_Free_Rate = float(input("Enter the risk free rate: "))
Shares = int(input("Enter the shares quantity: "))
Year = int(input("Enter the years to calculate: "))

today = date.today()
start = today.replace(year=today.year - Year)

prices = yf.download(portfolio, start = start, end = today, interval="1d" )['Adj Close']
prices[composite] = yf.download(composite, start = start, end = today, interval="1d" )['Adj Close']
prices = prices.fillna(method='bfill')
prices = prices.fillna(prices.mean())
net_returns = prices.pct_change()
Last_price = yf.download(portfolio, today)['Adj Close']

Market_Value = Last_price * Shares
Total_Market_Value = Market_Value.sum(axis=1)
Ponderation = (Market_Value.apply(lambda x: x/Total_Market_Value, 0)).to_numpy()
Daily_Composite_Return = (net_returns[composite].mean()).to_numpy()
Average_Daily_Return = (net_returns[portfolio].mean()).to_numpy()
Portfolio_Daily_Return = np.dot(np.squeeze(Average_Daily_Return),np.squeeze(Ponderation.T))
Portfolio_Annual_Return = ((1 + Portfolio_Daily_Return)**252)-1
Cov_Matrix = (net_returns[portfolio].cov()[portfolio])
Portfolio_Daily_Risk = (np.sqrt(np.matmul(Ponderation,np.matmul(Cov_Matrix,Ponderation.T)))).to_numpy()
Portfolio_Annual_Risk = Portfolio_Daily_Risk * np.sqrt(252)
Stock_Beta = pd.DataFrame(beta_calculator(net_returns)).drop(composite,axis=0)
Portfolio_Beta = np.dot(Stock_Beta.T,Ponderation.T)
Market_Return = ((1 + Daily_Composite_Return)**252)-1
CAPM = Risk_Free_Rate + Stock_Beta * (Market_Return - Risk_Free_Rate)
Portfolio_CAPM = Risk_Free_Rate + Portfolio_Beta * (Market_Return - Risk_Free_Rate)
PDR = round((float(cleaner(Portfolio_Daily_Risk)) * 100),2)
PAR = round((float(cleaner(Portfolio_Annual_Risk)) * 100),2)
PB = round(float(cleaner(Portfolio_Beta)),2)
MR = round((float(cleaner(Market_Return)) * 100),2)
PCAPM = round((float(cleaner(Portfolio_CAPM)) * 100),2)

print(f"Riesgo diario del portafolio: {PDR} %")
print(f"Riesgo anual del portafolio: {PAR} %")
print(f"Beta del portafolio: {PB}")
print(f"Rendimiento del mercado: {MR} %")
print(f"CAPM del portafolio: {PCAPM} %")
