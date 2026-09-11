import pandas as pd
df = pd.read_csv("Table data.csv")
df = df[df['Content'] != 'Total']
print(len(df))
df ['avg_view_duration_sec'] = (df['Watch time (hours)']*3600) / df['Views']
df ['avg_pct_viewed'] = (df['avg_view_duration_sec'] / df['Duration']) *100
print(df[['Video title','avg_pct_viewed' ]]. sort_values ('avg_pct_viewed', ascending = False))
daily = pd.read_csv("Chart data.csv")
totals = daily.groupby('Video title')['Views'].sum().sort_values(ascending= False)
print(totals)
daily_totals_df = totals.reset_index()
merged = daily_totals_df.merge(df, on= 'Video title')
print (merged.columns)
print (merged[['Video title', 'Views_x', 'Duration']])
import matplotlib.pyplot as plt
df_sorted = df.sort_values('avg_pct_viewed',ascending = False)
plt.figure(figsize=(10, 6))
plt.bar(df_sorted['Video title'], df_sorted['avg_pct_viewed'])
plt.xticks(rotation=90)
plt.ylabel('Avg % Viewed')
plt.title('Retention by Video')
plt.tight_layout()
plt.savefig('retention_chart.png')
print("Chart saved as retention_chart.png")


