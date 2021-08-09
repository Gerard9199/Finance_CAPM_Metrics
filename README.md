# Finance_CAPM_Metrics

This code is for finance metrics, you will be able to calculate the Market Value, Average Daily Return, Portfolio Daily Return, Portfolio Annual Return, Portfolio Daily Risk, Portfolio Annual Risk, Portfolio Beta, Market Return, and the CAPM for the assets or the portfolio.

First, you need to install de yahoo finance library (https://pypi.org/project/yfinance/).
With this lib, you will be able to download historical data from different stocks around the world. If you want to know want to know more about it, read the documentation.
Another lib that we will use is datatime.
Pandas will bring us the facility for the data managment, that is why we use de DataFrames in the code.

The function cleaner is for remove "[]" that appear in the final summary.
If you want to use stocks from other country (not US) you need to put the ticker like that: 'WALMEX.MX' (using "." and adding the country identifier). 
WALMEX.MX is for Walmart Mexico which is standing in the mexican composite called '^MXX' (in every composite you will use "^" at the begining).

This code is for the same shares quantity for all the stocks. I'm working to add an implement for the quantity shares.

For the free risk rate, you can google it. In US the free risk rate is the Treasury rate, in Mexico is the Cete rate.

Thanks for using this code.
