#https://luisao8-online-shop-analytics-webapp-dashboard-k431ov.streamlit.app/
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt
import plotly.graph_objects as go
from surprise import Reader, Dataset, KNNBasic

pd.set_option('display.max_columns', None)




#HEADER
st.title("Customer Information")
data = pd.read_feather("CompleteFinalDF.feather")
# data = pd.read_pickle("CompleteDFwithRFMLabels.pkl")
clusters = pd.read_pickle("Clusters.pkl")

# data = data.rename(columns={'% cancellations': 'percent_cancellations'})


color_dict = {0: 'red', 1: 'blue', 2: 'green', 3: 'black' }
fig = go.Figure(data=[go.Scatter3d(
    x=clusters['Recency'],
    y=clusters['Frequency'],
    z=clusters['Monetary'],
    mode='markers',
    text=clusters.index,
    marker=dict(
        size=8,
        color=[color_dict[c] for c in clusters["label"]],
        opacity=0.8
    )
)])

# set axis titles and layout
fig.update_layout(scene=dict(xaxis_title='Recency', yaxis_title='Frequency', zaxis_title='Monetary'))

# show the plot
st.plotly_chart(fig, use_container_width=True)




st.subheader("Discover customers:")
text_input = st.text_input("Insert customer ID:",key="customer_idOriginal")






col1, spacer, col2 = st.columns([4, 2, 4])

customer_info = data[data["Customer ID"] == text_input].reset_index()
customer_info = customer_info.drop("index", axis=1)
# activityTimeSeries = SalesDF.resample('W-MON', origin='start_day', offset='1D').sum(numeric_only=True).reset_index()
fig = px.line(customer_info, x='Date', y='Sales', title='Sales')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
invoice_information = customer_info.groupby("Invoice").agg({"Sales": "sum",
                                                            "Quantity": "sum",
                                                            "Description": "count"}).reset_index()
avg_InvSales = invoice_information["Sales"].mean()
avg_InvQuantity = invoice_information["Quantity"].mean()
avg_InvProds = invoice_information["Description"].mean()

product_information = customer_info.groupby("Description").agg({"Sales": "sum",
                                                                "Quantity": "sum"}).reset_index()
top5products = product_information.sort_values("Sales", ascending=False)[0:5]





customer_information = customer_info.groupby("Customer ID").agg({"Sales": "sum",
                                                                 "Quantity": "sum",
                                                                 "Invoice": "count",
                                                                 "InvoiceDate": "max",
                                                                 "% cancellations": "first",
                                                                 "RFM_Label": "first"}).reset_index()
# st.dataframe(data)
reference_date = pd.Timestamp('2011-12-09')
customer_information["Recency"] = reference_date - customer_information["InvoiceDate"]
customer_information["Recency"] = customer_information["Recency"].dt.days


if not customer_info.empty:
    salesTotal = customer_information.loc[0, 'Sales']
    quantityTotal = customer_information.loc[0, 'Quantity']
    invoiceTotal = customer_information.loc[0, 'Invoice']
    date = customer_information.loc[0, 'Recency']
    cancellations = customer_information.loc[0, '% cancellations']
    RFM_Label = customer_information.loc[0, 'RFM_Label']

    with col1:
        if date < 0:
            date = 0

        st.subheader("Global Information:")

        st.write(f"Total sales: {salesTotal:,.0f}£")
        st.write(f"Total products: {quantityTotal:,.0f}")
        st.write(f"Total invoices: {invoiceTotal:,.0f}")
        st.write(f"Customer Quality: {RFM_Label}")
        st.write(f"% Invoices cancelled: {cancellations:,.0f}%")
        st.write(f" ")
        st.write(f" ")

        st.subheader("Basket Information:")
        st.write(f" ")
        st.write(f"Average basket size: {avg_InvSales:,.0f}£")
        st.write(f"Average total products purchased: {avg_InvQuantity:,.0f}")
        st.write(f"Average individual products: {avg_InvProds:,.0f}")
        st.write(f"Days since last purchase: {date}")

    with col2:
        st.subheader("Top 5 products:")
        st.dataframe(top5products)

        st.subheader("Sales evolution:")
        st.plotly_chart(fig, use_container_width=True)


st.subheader("Recommended Products:")


dataForEngine = data[data["RFM_Label"] == "Top_client" ]
dataForEngine = dataForEngine.filter(["Customer ID", "Description", "Sales"])

reader = Reader(rating_scale=(dataForEngine['Sales'].min(), dataForEngine['Sales'].max()))
data2 = Dataset.load_from_df(dataForEngine, reader)

sim_options = {
    'name': 'cosine',
    'user_based': True
}

trainset = data2.build_full_trainset()
algo = KNNBasic(sim_options=sim_options)
algo.fit(trainset)



# Your function logic here

user_id = text_input
user_interacted_items = dataForEngine[dataForEngine['Customer ID'] == user_id]['Description'].unique()
all_items = dataForEngine['Description'].unique()
items_to_predict = set(all_items) - set(user_interacted_items)

predictions = []
for item_id in all_items:
    pred = algo.predict(user_id, item_id)
    predictions.append((item_id, pred.est))

ranked_items = sorted(predictions, key=lambda x: x[1], reverse=True)

top_n_recommendations = 10
st.write(f"Top {top_n_recommendations} recommendations for user {user_id}:")
data = {'Ranking': [],
        'Product': [],
        'Predicted Sales': []}
df_stats = pd.DataFrame(data)

for i, (item_id, est) in enumerate(ranked_items[:top_n_recommendations]):
    df_stats.loc[i] = [i + 1, item_id, f"{est:.2f}"]

st.table(df_stats)































