5import json


def meanReversionStrategy(prices):
    """
    Runs a mean reversion trading strategy.
    Buys when price is below 98% of the 5-day average.
    Sells when price is above 102% of the 5-day average.
    Returns total profit and percent return.
    """
    holding_stock = False
    buy_price = 0.0
    first_buy_price = 0.0
    total_profit = 0.0

    for index in range(5, len(prices)):
        price = round(prices[index], 2)
        avg = round(sum(prices[index - 5:index]) / 5, 2)

        if not holding_stock and price < avg * 0.98:
            buy_price = price
            if first_buy_price == 0.0:
                first_buy_price = buy_price
            holding_stock = True
            print(f"buying at:       {buy_price:.2f}")

        elif holding_stock and price > avg * 1.02:
            sell_price = price
            trade_profit = round(sell_price - buy_price, 2)
            total_profit = round(total_profit + trade_profit, 2)
            holding_stock = False
            print(f"selling at:      {sell_price:.2f}")
            print(f"trade profit:    {trade_profit:.2f}")

    print("-----------------------")
    print(f"Total profit:    {total_profit:.2f}")

    if first_buy_price > 0:
        percent_return = round((total_profit / first_buy_price) * 100, 2)
        print(f"First buy:       {first_buy_price:.2f}")
        print(f"Percent return:  {percent_return:.2f}%")
    else:
        percent_return = 0.0
        print("First buy:       None")
        print("Percent return:  0.00%")

    return total_profit, percent_return


def simpleMovingAverageStrategy(prices):
    """
    Runs a simple moving average trading strategy.
    Buys when price is above the 5-day average.
    Sells when price is below the 5-day average.
    Returns total profit and percent return.
    """
    holding_stock = False
    buy_price = 0.0
    first_buy_price = 0.0
    total_profit = 0.0

    for index in range(5, len(prices)):
        price = round(prices[index], 2)
        avg = round(sum(prices[index - 5:index]) / 5, 2)

        if not holding_stock and price > avg:
            buy_price = price
            if first_buy_price == 0.0:
                first_buy_price = buy_price
            holding_stock = True
            print(f"buying at:       {buy_price:.2f}")

        elif holding_stock and price < avg:
            sell_price = price
            trade_profit = round(sell_price - buy_price, 2)
            total_profit = round(total_profit + trade_profit, 2)
            holding_stock = False
            print(f"selling at:      {sell_price:.2f}")
            print(f"trade profit:    {trade_profit:.2f}")

    print("-----------------------")
    print(f"Total profit:    {total_profit:.2f}")

    if first_buy_price > 0:
        percent_return = round((total_profit / first_buy_price) * 100, 2)
        print(f"First buy:       {first_buy_price:.2f}")
        print(f"Percent return:  {percent_return:.2f}%")
    else:
        percent_return = 0.0
        print("First buy:       None")
        print("Percent return:  0.00%")

    return total_profit, percent_return


def saveResults(results):
    """
    Saves the results dictionary to results.json.
    """
    with open("results.json", "w") as json_file:
        json.dump(results, json_file, indent=4)


def loadPrices(filename):
    """
    Reads stock prices from a text file and returns them as a list of floats.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        prices = [round(float(line.strip()), 2) for line in lines]
    return prices


def main():
    # Required stocks plus 7 of your choice
    tickers = [
        "AAPL",
        "GOOG",
        "ADBE",
        "TSLA",
        "MSFT",
        "AMZN",
        "JPM",
        "CSCO",
        "CMCSA",
        "CVX"
    ]

    results = {}

    for ticker in tickers:
        filename = f"{ticker}.txt"
        prices = loadPrices(filename)

        results[f"{ticker}_prices"] = prices

        print(f"\n{ticker} Simple Moving Average Strategy Output:")
        sma_profit, sma_returns = simpleMovingAverageStrategy(prices)
        results[f"{ticker}_sma_profit"] = sma_profit
        results[f"{ticker}_sma_returns"] = sma_returns

        print(f"\n{ticker} Mean Reversion Strategy Output:")
        mr_profit, mr_returns = meanReversionStrategy(prices)
        results[f"{ticker}_mr_profit"] = mr_profit
        results[f"{ticker}_mr_returns"] = mr_returns

    saveResults(results)
    print("\nresults.json has been created successfully.")


main()
