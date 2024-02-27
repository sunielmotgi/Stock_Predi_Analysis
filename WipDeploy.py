# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 22:10:51 2024

@author: sunie
"""


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
from PIL import Image
import os

st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')


df= pd.read_csv("WiproN.csv")
df

fig = px.line(df, x=df.index,y=df['Adj Close'], title= ticker)
st.plotly_chart(fig)

pricing_data, fundamental_data, news = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

with pricing_data:
    st.header('Price Movements')
    df1 = df
    df1['% Change']= df['Adj Close'] / df['Adj Close'].shift(1) - 1
    df1.dropna(inplace = True)
    st.write(df1)
    annual_return = df1['% Change'].mean()*252*100
    st.write('Annual Return is ', annual_return, '%')
    stdev = np.std(df1['% Change'])*np.sqrt(252)
    st.write('Standard Deviation is ', stdev*100, '%')
    st.write('Risk Adj.Return is ', annual_return/(stdev*100))

# from alpha_vantage.fundamentaldata import FundamentalData
# with fundamental_data:
#     key = 'VJ7FC0DOLGGK77T1'
#     fd = FundamentalData(key,output_format='pandas')
#     st.subheader('Balance Sheet')
#     balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
#     bs= balance_sheet.T[2:]
#     bs.columns = list(balance_sheet.T.iloc[0])
#     st.write(bs)
#     st.subheader ('Income Statement')
#     income_statement = fd.get_income_statement_annual(ticker)[0]
#     is1 = income_statement.T[2:]
#     is1.columns = list(income_statement.T.iloc[0])
#     st.write(is1)
#     st.subheader('Cash Flow Statement')
#     cash_flow = fd.get_cash_flow_annual(ticker)[0]
#     cf = cash_flow.T[2:]
#     cf.columns = list (cash_flow.Tiloc[0])
    
from stocknews import StockNews
with news:
    st.header(f'News of {ticker}')
    sn= StockNews(ticker,save_news=False)
    df2_news= sn.read_rss()
    for i in range(10):
        st.subheader(f'News {i+1}')
        st.write(df2_news['published'][i])
        st.write(df2_news['title'][i])
        st.write(df2_news['summary'][i])
        title_sentiment = df2_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment = df2_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')
    #st.write('News')

                               