# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:19:05 2024

@author: sunie
"""

import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

st.title('Stock Price Prediction')
data=pd.read_csv("WIPRON.csv")
st.write(data)

st.header("Data Visualization")
st.subheader("Plot of the Data")
fig=px.line(data,y="Close",title="Closing price of the stock")
st.plotly_chart(fig)


with open('stock_mkt_analysis.sav',mode = 'rb') as f:
    pred = pickle.load(f)
    prediction=pred
    st.title("Predicted Value for Next 12 Period")
    st.write(prediction)
    fig=px.line(prediction)
    st.plotly_chart(fig)
