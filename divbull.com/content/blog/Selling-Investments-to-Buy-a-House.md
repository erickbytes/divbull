Title: Selling Investments to Buy a House 
Date: 2025-08-16 4:20 
Category: Essay


Up to this point in my life, 97% of my net worth has been invested in stocks and crypto. I've begun planning for my
first home purchase. It is a strategic move to hopefully save money vs. renting and bring more stability
for my wife and I. In this post, I'll share some key calculations I made to assess if I could do this.

After looking at houses in our local market with my wife, I've determined I can buy the house in cash. It is about 
33% of my net worth including all furnishings. The house is abroad, in my wife's native country. So it benefits from lower 
housing prices and cost of living, which makes it easier for me to buy. 

I want to pay in cash because interest rates on a loan are relatively high. I don't want to make a monthly payment 
on a mortgage. I don't want to pay thousands of extra dollars in interest on borrowed loan money. Therefore, I've 
decided to convert part of my stock portfolio into a house. I might be able to secure a loan and achieve an investment 
return higher than the loan interest. However, cash helps facilitate a deal and moves us into the house faster also.

Sadly, this means I will need to part ways with some of my most favorite companies, or at least downsize 
how many shares I'm holding significantly. I plan to trim my most bullish long holds like Nvidia, Microsoft, Tesla, Spotify 
and Cloudflare. I'm going to liquidate parts of my Bitcoin, Ethereum, Solana, Dogecoin and Cardano longs. These assets will continue 
to be in my portfolio, but reduced approximately 10-50%. However, I believe this is ultimately a good exercise for me 
not to fall in love with my stocks, book some profits and diversify elsewhere. I realize that the best returns tend to come 
from holding assets over time, but sometimes life is not about seeking the optimal return. A home brings obvious benefits like a place 
to live or a source of rental income. With that said, there is substantial risk that I will regret selling the stocks if the 
stock market continues to rise. Historical data says it likely will.The opportunity cost of taking money from stocks to invest 
in real estate may be huge. If that is the case, at least I'll still have 66% of my stocks in the game.

**Liquid vs. Non-Liquid Assets**

First, I did some calculations of my "liquid" vs. "non-liquid" assets to assess if I could actually buy a house without
emptying all of my current liquid investments. After tallying up my retirement funds and IRAs, I found that 24% of my net worth is not 
available without invoking a substantial penalty. Therefore, I consider these funds to be not accessible at all. I plan to roll over the
401(K) into my custody later this year. Additionally, my managed Roth IRA will likely be rolled over within the next few years.

| Non-Liquid Assets | % of Total Assets |
|:---|:---|
| Managed 401(k) | 8.24% |
| Self-Directed Roth IRA | 10.26% |
| Managed Roth IRA | 3.32% |
| HSA | 1.78% |
| Self-Directed Traditional IRA | 0.32% |
| **Total Non-Liquid Assets** | **24%** |

Next, I tallied up my liquid assets, which consisted of two sources: my investment brokerage and cryptocurrency holdings. 
In total, they represent 76% of my net worth.

| Liquid Assets | % of Total Assets |
|:---|:---|
| Investment Brokerage | 64.41% |
| Cryptocurrency | 11.68% |
| **Total Liquid Assets** | **76%** |

**Confidence Ranking My Portfolio**

Second, I made a confidence ranking of all the liquid assets I'm holding in my brokerage account and cryptocurrencies.
This simply means a list of each asset in a single column. Then in a 2nd column, assigning a number starting with 1,2,3 
for my highest conviction 3 holdings for example, continuing to assign a number until all assets are ranked. In a third 
new column, list each corresponding asset's current market value.

In a fourth column, I applied a Google Sheets nested IF formula to assign a sell weight based on my conviction rank in each asset:

```
=IF(B2<15, 0.25*C2, IF(B2<30, 0.5*C2, 0.75*C2))
```

This formula applies a weighted ratio based on the confidence rank (cell B2). It applies a heavier weight to the assets
I have lower confidence in. In this example, C2 represents the market value of the asset in my portfolio as of today.
The formula is applied to all my assets by "dragging down" the formula into a column with a reference to each of my assets'
market value and confidence rank.

I shifted the weights and confidence intervals around in different columns, then summed up the resulting market values.
So each column becomes a new projection of what I can sell from each asset and the total amount raised.
I've estimated nearly all my costs, so I know approximately how much we'll need get the house set up.

**Major Portfolio Changes Coming**

This will be a tough exercise to complete. Up until this point, I've been very slow to make changes in my portfolio. 
Typically, I would only sell the minimum amount needed to cover a necessary large expense or taxes. Therefore, I will 
need to chop some positions down substantially. Many or all of the positions I've shared in the past will likely be 
significantly reduced in orderto raise the funds to buy the house. This is a sacrifice I have decided I want to make 
in order to improve my quality of life, reduce annual rent and eliminate moving expenses.

In some cases, I might sell 100% of an asset, but I prefer to distribute the impact across my entire portfolio. I want 
to keep exposure in as many of my holdings as possible. However, the benefit of the confidence ranking is that it shows 
your conviction in hierarchical format. The lower conviction holdings are more likely to be sold off. The Google Sheets 
formula I used applies this desire progressively across my entire portfolio, based on my conviction. 

I might regret making a big move like this someday. Or maybe I'll be satisfied with how it all works out in the end.
After thinking it through and crunching the numbers, I think I'm ready to buy a house.











