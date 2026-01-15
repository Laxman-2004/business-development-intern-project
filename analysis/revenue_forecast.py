import pandas as pd

leads_df = pd.read_csv('../data/lead_generation.csv')

average_deal_size = 15000  # INR

leads_df['Expected_Revenue'] = (
    leads_df['Monthly_Leads'] *
    leads_df['Conversion_Rate'] *
    average_deal_size
)

monthly_revenue = leads_df['Expected_Revenue'].sum()
six_month_revenue = monthly_revenue * 6

print("Estimated Monthly Revenue (INR):", int(monthly_revenue))
print("Estimated 6-Month Revenue (INR):", int(six_month_revenue))
