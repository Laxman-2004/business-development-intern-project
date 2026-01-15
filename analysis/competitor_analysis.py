import pandas as pd

df = pd.read_csv('../data/competitor_analysis.csv')

print("Competitor Landscape:")
print(df)

print("\nInsight: Mid-priced competitors focus on support, while low-priced target SMEs.")
