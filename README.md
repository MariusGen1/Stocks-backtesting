# Crypto-investment-methods-backtesting
A tool that allows to check whether certain data can be used to predict a price evolution

# Working principle
Downloads historical data from a list of stocks, and tests whether certain data may allow to predict the price thanks to a polynomial regression where the data in question is compared to the price a set amount of days later. The user can modify the program to print only the datasets that gave an R^2 value above a certain threshold.

# Results
Running the program on this list of stocks: ['AMD','ADBE','ALGN','AMZN','AAPL','AMAT','ASML','TEAM','ADSK','GOOG','GOOGL'], with data since January 1st 2016 and comparing the initial price with the price two days later, the regressions with the highest R^2 for each stock are the following: 


ADBE stock compared with the Low 2nd Derivate gave an R^2 of 0.0166

AMD stock compared with the 3 Day Mean Volume gave an R^2 of 0.0138

GOOG stock compared with the 2 Day Mean Volume gave an R^2 of 0.0134

GOOGL stock compared with the 2 Day Mean Volume gave an R^2 of 0.0114

ASML stock compared with the Open 2nd Derivate gave an R^2 of 0.01

AMAT stock compared with the Open 2nd Derivate gave an R^2 of 0.0085

AAPL stock compared with the Close 2nd Derivate gave an R^2 of 0.0078

ALGN stock compared with the Spread gave an R^2 of 0.007

AMZN stock compared with the Open gave an R^2 of 0.0066

ADSK stock compared with the Close gave an R^2 of 0.0064

TEAM stock compared with the Low 2nd Derivate gave an R^2 of 0.0055





# Conclusion
The R^2 values obtained are very low and indicate that there is little to none direct correlation between the price and the factors the program has tested against.


You are free to download and run the program yourself and make any improvements you may like.
