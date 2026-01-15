import pandas as pd

df = pd.read_csv('../data/market_research.csv')

best_markets = df.sort_values(by='Annual_Growth_Rate', ascending=False)

print("High-Growth Markets for Expansion:")
print(best_markets)
