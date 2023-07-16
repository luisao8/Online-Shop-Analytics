import plotly.express as px
import altair as alt
import plotly.graph_objects as go
import streamlit as st
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import accuracy_score

pd.set_option('display.max_columns', None)

st.header("Cancellations:")

cancellations = pd.read_pickle("CancellationsDF.pkl")
EliminatedPositiveDF = pd.read_pickle("EliminatedPositiveMirrorTransactions.pkl")
# dfForPrediction = pd.read_pickle("CompleteDFwithRFMLabels.pkl")
dfForPrediction = pd.read_feather("CompleteFinalDF.feather")




st.subheader("Highest cancelling customers:")


custCanc = cancellations.groupby("Customer ID").agg({"Sales":"sum", "Quantity": "sum", "Invoice":"count"}).reset_index()

option = st.selectbox(
    'How would you like to sort the DF?',
    ('Sales', 'Quantity', 'Invoice'), key="option_1")

custCanc = custCanc.sort_values(option, ascending=True)

st.dataframe(custCanc)


st.subheader("Highest cancelling Countries:")

countryCanc = cancellations.groupby("Country").agg({"Sales":"sum", "Quantity": "sum", "Invoice":"count"}).reset_index()

option2 = st.selectbox(
    'How would you like to sort the DF?',
    ('Sales', 'Quantity', 'Invoice'), key="option_2")

countryCanc = countryCanc.sort_values(option, ascending=True)

st.dataframe(countryCanc)


# st.subheader("Cancellation Prediction:")

# month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
# dfForPrediction['month_num'] = dfForPrediction['Month'].map(month_dict)
#
#
# month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
# EliminatedPositiveDF['month_num'] = EliminatedPositiveDF['Month'].map(month_dict)
#
# # Map day names to numerical values
# day_dict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
# EliminatedPositiveDF['day_num'] = EliminatedPositiveDF['Day'].map(day_dict)
#
# day_dict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
# dfForPrediction['day_num'] = dfForPrediction['Day'].map(day_dict)
#
#
# month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
# dfForPrediction['month_num'] = dfForPrediction['Month'].map(month_dict)
#
# month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
# EliminatedPositiveDF['month_num'] = EliminatedPositiveDF['Month'].map(month_dict)
#
# # Map day names to numerical values
#
#
# EliminatedPositiveDF['month_sin'] = np.sin(2 * np.pi * EliminatedPositiveDF['month_num'] / 12)
# EliminatedPositiveDF['month_cos'] = np.cos(2 * np.pi * EliminatedPositiveDF['month_num'] / 12)
#
# EliminatedPositiveDF['day_sin'] = np.sin(2 * np.pi * EliminatedPositiveDF['day_num'] / 7)
# EliminatedPositiveDF['day_cos'] = np.cos(2 * np.pi * EliminatedPositiveDF['day_num'] / 7)
#
# EliminatedPositiveDF['hour_sin'] = np.sin(2 * np.pi * EliminatedPositiveDF['hour'] / 24)
# EliminatedPositiveDF['hour_cos'] = np.cos(2 * np.pi * EliminatedPositiveDF['hour'] / 24)
#
# dfForPrediction['month_sin'] = np.sin(2 * np.pi * dfForPrediction['month_num'] / 12)
# dfForPrediction['month_cos'] = np.cos(2 * np.pi * dfForPrediction['month_num'] / 12)
#
# dfForPrediction['day_sin'] = np.sin(2 * np.pi * dfForPrediction['day_num'] / 7)
# dfForPrediction['day_cos'] = np.cos(2 * np.pi * dfForPrediction['day_num'] / 7)
#
# dfForPrediction['hour_sin'] = np.sin(2 * np.pi * dfForPrediction['hour'] / 24)
# dfForPrediction['hour_cos'] = np.cos(2 * np.pi * dfForPrediction['hour'] / 24)
#
# EliminatedPositiveDF = EliminatedPositiveDF.groupby("Invoice").agg({"Customer ID":"first",
#                                                                     "Description":"count",
#                                                                     "Quantity": "sum",
#                                                                     "Sales": "sum",
#                                                                     "month_sin":"first",
#                                                                     "month_cos":"first",
#                                                                     "day_sin": "first",
#                                                                     "day_cos": "first",
#                                                                     "hour_sin": "first",
#                                                                     "hour_cos": "first",}).reset_index()
#
# dfForPrediction = dfForPrediction.groupby("Invoice").agg({"Customer ID":"first",
#                                                           "Description":"count",
#                                                           "Quantity": "sum",
#                                                           "Sales": "sum",
#                                                           "month_sin":"first",
#                                                           "month_cos":"first",
#                                                           "day_sin": "first",
#                                                           "day_cos": "first",
#                                                           "hour_sin": "first",
#                                                           "hour_cos": "first",
#                                                           "% cancellations":"first"}).reset_index()
#
# dfForPrediction = dfForPrediction.loc[(~dfForPrediction['Customer ID'].isnull())]
#
# IDsForMatching = dfForPrediction.groupby("Customer ID").agg({"% cancellations":"first"}).reset_index()
# merged_df = pd.merge(EliminatedPositiveDF, IDsForMatching, on='Customer ID', how="left")
# merged_df["Cancelled"] = 1
#
# dfForPrediction["Cancelled"] = 0
# result = pd.concat([dfForPrediction, merged_df], axis=0)
# result = result.drop(columns=['Invoice', 'Customer ID'])
# result = result.fillna(0)
#
# X = result.drop(columns=['Cancelled'])
# y = result['Cancelled']
#
# smote = SMOTE()
# X_resampled, y_resampled = smote.fit_resample(X, y)
#
# # Split the dataset into a training set and a testing set
# X_train, X_test, y_train, y_test = train_test_split(X_resampled,y_resampled , test_size=0.2, random_state=200)
#
#
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# st.write(f"Accuracy: {accuracy:.2f}")












