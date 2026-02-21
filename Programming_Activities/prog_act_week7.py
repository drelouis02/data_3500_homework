import random


# Activity 1
def activity_1():
    colors = ["blue", "black", "green"]
    for c in colors:
        print(c)


# Activity 2
def activity_2():
    colors = ["blue", "black", "green"]
    for color in colors:
        print(f"\nColor: {color}")
        for ch in color:
            print(ch)


# Activity 3
def activity_3():
    nums = []
    for _ in range(10):
        nums.append(random.randint(1, 100))
    return nums


# Activity 4
def activity_4(nums):
    for i in range(len(nums) - 1):
        if nums[i] % 2 == 0 and nums[i + 1] % 2 == 0:
            print(f"Two evens in a row: {nums[i]}, {nums[i + 1]}")


def read_prices_from_file(filename):
    prices = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) >= 6:
                try:
                    prices.append(float(parts[4]))
                    continue
                except ValueError:
                    pass

            try:
                prices.append(float(line))
            except ValueError:
                continue
    return prices


def avg(values):
    return sum(values) / len(values) if values else 0.0


# Activity 5
def activity_5(filename="AAPL.2023.txt"):
    prices = read_prices_from_file(filename)
    overall_avg = avg(prices)
    first_5_avg = avg(prices[:5])

    print(f"Total days: {len(prices)}")
    print(f"Average (all): {overall_avg}")
    print(f"Average (first 5): {first_5_avg}")
    return prices


# Activity 5.2
def activity_5_2(filename="AAPL.2023.txt"):
    prices = read_prices_from_file(filename)

    first_4_avg = avg(prices[:4])
    last_4_avg = avg(prices[-4:])

    print(f"First 4-day average: {first_4_avg}")
    print(f"Last 4-day average: {last_4_avg}")

    cash = 0.0
    shares = 0

    for i in range(4, len(prices)):
        today_price = prices[i]
        today_sma = avg(prices[i - 3:i + 1])
        yesterday_price = prices[i - 1]
        yesterday_sma = avg(prices[i - 4:i])

        cross_up = yesterday_price <= yesterday_sma and today_price > today_sma
        cross_down = yesterday_price >= yesterday_sma and today_price < today_sma

        if cross_up and shares == 0:
            shares = 1
            cash -= today_price
        elif cross_down and shares == 1:
            shares = 0
            cash += today_price

    if shares == 1:
        cash += prices[-1]

    print(f"Profit from SMA strategy: {cash}")


def main():
    print("=== Activity 1 ===")
    activity_1()

    print("\n=== Activity 2 ===")
    activity_2()

    print("\n=== Activity 3 ===")
    nums = activity_3()
    print(nums)

    print("\n=== Activity 4 ===")
    activity_4(nums)

    print("\n=== Activity 5 ===")
    activity_5("AAPL.2023.txt")

    print("\n=== Activity 5.2 ===")
    activity_5_2("AAPL.2023.txt")


if __name__ == "__main__":
    main()
