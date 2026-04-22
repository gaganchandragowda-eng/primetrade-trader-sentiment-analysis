import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read files
sentiment = pd.read_excel("fear_greed_index.xlsx")
trades = pd.read_csv("historical_data.csv")

# basic info
print("Sentiment Shape:", sentiment.shape)
print("Trades Shape:", trades.shape)

print(sentiment.head())
print(trades.head())

# remove duplicates
sentiment = sentiment.drop_duplicates()
trades = trades.drop_duplicates()

# convert dates
sentiment["date"] = pd.to_datetime(sentiment["date"])

trades["Timestamp IST"] = pd.to_datetime(
    trades["Timestamp IST"],
    errors="coerce"
)

trades["date"] = trades["Timestamp IST"].dt.date
trades["date"] = pd.to_datetime(trades["date"])

# convert numeric columns
trades["Closed PnL"] = pd.to_numeric(
    trades["Closed PnL"],
    errors="coerce"
)

trades["Size USD"] = pd.to_numeric(
    trades["Size USD"],
    errors="coerce"
)

trades["Fee"] = pd.to_numeric(
    trades["Fee"],
    errors="coerce"
)

# merge data
data = pd.merge(
    trades,
    sentiment,
    on="date",
    how="left"
)

print(data.head())

# create win column
data["win"] = 0
data.loc[data["Closed PnL"] > 0, "win"] = 1

# daily summary
daily = data.groupby(
    ["date", "classification"]
).agg({
    "Closed PnL": "mean",
    "win": "mean",
    "Size USD": "mean",
    "Account": "count"
}).reset_index()

daily.columns = [
    "date",
    "classification",
    "avg_pnl",
    "win_rate",
    "avg_trade_size",
    "trade_count"
]

print(daily.head())

# summary by sentiment
result = daily.groupby("classification").mean(
    numeric_only=True
)

print(result)

# pnl chart
plt.figure(figsize=(9,5))
sns.barplot(
    x="classification",
    y="avg_pnl",
    data=daily
)
plt.xticks(rotation=45)
plt.title("Average PnL by Sentiment")
plt.tight_layout()
plt.show()

# trade size chart
plt.figure(figsize=(9,5))
sns.barplot(
    x="classification",
    y="avg_trade_size",
    data=daily
)
plt.xticks(rotation=45)
plt.title("Average Trade Size by Sentiment")
plt.tight_layout()
plt.show()

# trader analysis
trader = data.groupby("Account").agg({
    "Closed PnL":"sum",
    "Account":"count",
    "Size USD":"mean"
}).reset_index()

trader.columns = [
    "Account",
    "total_pnl",
    "trades",
    "avg_size"
]

# segment traders
mid = trader["trades"].median()

trader["type"] = "Infrequent"
trader.loc[
    trader["trades"] >= mid,
    "type"
] = "Frequent"

print(trader.head())

# segment results
print(
    trader.groupby("type")["total_pnl"].mean()
)

# top traders
top = trader.sort_values(
    "total_pnl",
    ascending=False
).head(10)

plt.figure(figsize=(10,6))
sns.barplot(
    x="total_pnl",
    y="Account",
    data=top
)
plt.title("Top 10 Traders")
plt.tight_layout()
plt.show()

# final insights
print("\nInsights")
print("1. Profit changes across Fear and Greed days.")
print("2. Traders take different position sizes based on sentiment.")
print("3. Frequent traders trade more but profits are mixed.")

print("\nRecommendations")
print("1. Reduce risk during Fear days.")
print("2. Use strict stop loss during Greed days.")
print("3. Avoid overtrading.")
