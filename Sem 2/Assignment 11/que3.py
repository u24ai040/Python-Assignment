#QUESTION 3

import pandas as pd

n = int(input("Enter number of deals: "))

asking_prices = []
fair_prices = []

for i in range(n):
    print("\nDeal ", i + 1)
    asking = int(input("Asking price: "))
    fair = int(input("Fair price: "))
    asking_prices.append(asking)
    fair_prices.append(fair)


asking_series = pd.Series(asking_prices)
fair_series = pd.Series(fair_prices)


good_deal_indices = []
for i in range(n):
    if asking_series[i] < fair_series[i]:
        good_deal_indices.append(i)
        print(f"Deal {i + 1}: Asking price {asking_series[i]}, Fair price {fair_series[i]} - Good deal!")

print("\nGood deals are at indices:", good_deal_indices)
