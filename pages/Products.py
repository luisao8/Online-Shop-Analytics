#https://luisao8-online-shop-analytics-webapp-dashboard-k431ov.streamlit.app/
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt
import plotly.graph_objects as go
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

pd.set_option('display.max_columns', None)

data = pd.read_feather("CompleteFinalDF.feather")
# data = pd.read_pickle("CompleteDFwithRFMLabels.pkl")
Apriori = pd.read_pickle("ForApriori.pkl")



st.title("Products")

col1, spacer, col2 = st.columns([4, 2, 4])


with col1:
    st.subheader("A priori dataframe:")
    st.dataframe(Apriori)


with col2:
    st.subheader("Top selling products:")
    data = data.groupby("Description").agg({"Sales": "sum",
                                            "Quantity": "sum",
                                            "StockCode": "count",
                                            "Customer ID": "count"}).sort_values("Quantity", ascending=False).reset_index()
    st.dataframe(data)




# with col1:
#     @st.cache
#     def calculate_aPriori():
#         df_Apriori = data[['Invoice', 'Description', 'Quantity']]
#
#         def return_one(x):
#             return 1
#
#         table = pd.pivot_table(df_Apriori, values='Quantity', index=['Invoice'], columns=['Description'],
#                                aggfunc=return_one, fill_value=0)
#
#         frequent_itemsets = apriori(table, min_support=0.01, use_colnames=True)
#
#         return frequent_itemsets
#
#
#     frequent_itemsets = calculate_aPriori()
#
#     st.dataframe(frequent_itemsets)




# option = st.selectbox(
#     'What metric do you want to sort by?:',
#     ('lift', 'confidence', 'leverage'))
#
#
#
# rules = association_rules(frequent_itemsets, metric="lift", min_threshold=3)
#
#
#
# rules_df = rules.sort_values(["lift"], ascending= False)
#
#
#
# st.dataframe(rules_df)

