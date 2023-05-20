#https://luisao8-online-shop-analytics-webapp-dashboard-k431ov.streamlit.app/
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

pd.set_option('display.max_columns', None)



#HEADER
st.title("Overview")
st.write("Ready for some analytics?")
# data = pd.read_pickle("Hola.pkl")
# data.to_feather("SalesPredictions.feather")
# data = pd.read_feather("CompleteFinalDF.feather")
# print(data)
#######
#
#
# #SALES TIMESERIES - WORKING
# SalesDF = data.set_index("Date")
# DFforSalesTimeSeries = SalesDF.resample('W-MON', origin='start_day', offset='1D').sum(numeric_only=True).reset_index()
# fig = px.line(DFforSalesTimeSeries, x='Date', y='Sales', title='Time Series with Range Slider and Selectors')
#
# fig.update_xaxes(
#     rangeslider_visible=True,
#     rangeselector=dict(
#         buttons=list([
#             dict(count=1, label="1m", step="month", stepmode="backward"),
#             dict(count=6, label="6m", step="month", stepmode="backward"),
#             dict(count=1, label="YTD", step="year", stepmode="todate"),
#             dict(count=1, label="1y", step="year", stepmode="backward"),
#             dict(step="all")
#         ])
#     )
# )
#
# st.plotly_chart(fig, use_container_width=True)
#
#
# #QUANTITY/SALES/INVOICE PER YEAR
# DFbyYear = data.groupby("Year").agg({"Sales":"sum", "Quantity": "sum", "Invoice": "count"}).reset_index()
# fig = px.bar(DFbyYear, x='Year', y=['Sales','Quantity', 'Invoice'])
# st.plotly_chart(fig, use_container_width=True)
#
#
#
#
#


