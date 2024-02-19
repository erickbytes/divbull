Title: How to Automate Stock and Crypto Prices in Google Sheets 
Date: 2024-02-19 13:42 
Category: Essay


I recently discovered two great functions for tracking stocks and crypto. The [GOOGLEFINANCE() function](https://support.google.com/docs/answer/3093281?hl=en) can be used to import stocks and crypto prices. Additionally, the [IMPORTDATA() function](https://support.google.com/docs/answer/3093335?hl=en) is able to import cryptocurrency prices from cryptoprices.cc.

Here is the syntax that the Google Finance function expects:

    =GOOGLEFINANCE("{Exchange_Ticker}:{Stock_Ticker}")

Note that you can pass other attributes and dates to specify a time frame if required. Refer to the Google documentation links above for more advanced usage.

**Import Microsoft's Nasdaq Exchange Stock Price to Google Sheets**

```
=GOOGLEFINANCE("NASDAQ:MSFT")
```

**Import Snowflake's NYSE Exchange Stock Price to Google Sheets**

You'll want to make sure the ticker is the correct exchange the stock trades on:
```
=GOOGLEFINANCE("NYSE:SNOW")
```

**Import Charles Schwab's S&P 500 Mutual Fund Price to Google Sheets**

```
=GOOGLEFINANCE("MUTF:SWPPX")
```

Google Finance also has the ability to fetch crypto prices for assets like Bitcoin and Ethereum. However, these prices seemed to update less reliably than stocks. I then found the IMPORTDATA() function, which updates crypto prices more reliably in my experience. The website cryptoprices.cc has made the prices available via their website and this function.

**Import Bitcoin's Crypto Price to Google Sheets**
```
=IMPORTDATA("https://cryptoprices.cc/BTC")
```

**Import Ethereum's Crypto Price to Google Sheets**
```
=IMPORTDATA("https://cryptoprices.cc/ETH")
```

Once you have the prices of your assets auto-updating in Google Sheets, you can calculate the market value of your holdings by multiplying the price by the number of units, shares or coins you hold of an asset.

    (Price x Quantity = Market Value)
    =GOOGLEFINANCE("NASDAQ:MSFT") * {# Shares} = Market Value

Once you have your Market Value of your holding, you can subtract the cost basis to see your total profit or gain/loss:

    Market Value - Cost Basis = Profit

Once you calculate the profit, you can calculate the return on equity %:

    Profit / Cost Basis = ROE %

I am now tracking all my stocks, crypto and index funds in a single Google sheet with these functions. The prices tend to update at minimum every hour, but usually quicker. I'm impressed that Google has this functionality built-in, it's very useful!