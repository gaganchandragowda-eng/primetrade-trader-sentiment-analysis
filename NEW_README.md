# Primetrade Trader Sentiment Analysis

This repository contains my submission for the Primetrade.ai Round-0 Data Science / Analytics Internship assignment.

## Project Goal

The objective of this task is to study how Bitcoin market sentiment (Fear / Greed) affects trader performance and behavior on Hyperliquid.

## Datasets Used

1. fear_greed_index.xlsx  
Daily Bitcoin market sentiment data.

2. historical_data.csv  
Historical trader transaction data including pnl, trade size, fees, account activity and timestamps.

## What I Did

- Loaded both datasets using Python
- Cleaned duplicate and missing values
- Converted timestamps into proper date format
- Merged both datasets using date
- Calculated important metrics like PnL, win rate and trade count
- Compared trader results during Fear and Greed days
- Segmented traders into groups
- Created charts for better understanding
- Suggested practical trading strategies

## Main Findings

- Market sentiment has impact on profitability
- Traders tend to take larger positions during Greed periods
- More trading activity does not always mean more profit
- Risk management is important during emotional market phases

## Files Included

- Primetrade_Assignment.py
- Primetrade_Assignment.ipynb
- summary.md
- requirements.txt

## How to Run

Install packages:

pip install -r requirements.txt

Run the script:

python Primetrade_Assignment.py

## Tools Used

Python, Pandas, Matplotlib, Seaborn, Scikit-learn
