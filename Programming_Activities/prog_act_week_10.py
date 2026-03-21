# HW4 - Stock Market Trading
# This program reads Tesla stock prices from a text file,
# calculates a 5-day moving average, and applies a mean
# reversion trading strategy.
#
# Strategy:
# - Buy when current price is less than 98% of the 5-day average
# - Sell when current price is greater than 102% of the 5-day average
# - Track profit for each completed trade
# - Print total profit, first buy, and percent return


file = open("TSLA.txt")
lines = file.readlines()
file.close()

price_list = []

for line in lines:
    price = float(line)
    price = round(price, 2)
    price_list.append(price)

buy_price = 0
first_buy = 0
total_profit = 0
holding_stock = False

print("TSLA Mean Reversion Strategy Output: 2025 - 2026 Data")

for i in range(5, len(price_list)):
    current_price = round(price_list[i], 2)
    previous_five_days = price_list[i - 5:i]
    average_price = round(sum(previous_five_days) / 5, 2)

    if current_price < average_price * 0.98 and holding_stock == False:
        buy_price = current_price
        holding_stock = True

        if first_buy == 0:
            first_buy = buy_price

        print(f"buying at:       {buy_price:.2f}")

    elif current_price > average_price * 1.02 and holding_stock == True:
        sell_price = current_price
        trade_profit = round(sell_price - buy_price, 2)
        total_profit = round(total_profit + trade_profit, 2)
        holding_stock = False

        print(f"selling at:      {sell_price:.2f}")
        print(f"trade profit:    {trade_profit:.2f}")

    else:
        pass

print("-----------------------")
print(f"Total profit:    {total_profit:.2f}")
print(f"First buy:       {first_buy:.2f}")

if first_buy != 0:
    final_profit_percentage = round((total_profit / first_buy) * 100, 2)
    print(f"% return:        {final_profit_percentage:.2f}%")
else:
    print("% return:        0.00%")
