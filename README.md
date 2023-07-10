# Online Shop Analytics Project

---

[![Video Demo](https://drive.google.com/uc?export=view&id=1u_kL-3Cm6bmjS0-WY5HvdGoIl4nVlCHZ)](http://www.youtube.com/watch?v=lbs-DYDiUv8 "Video Demo")

---

## Table of Contents
1. [Project Description](#project-description)
2. [Technologies](#technologies)
3. [Insights](#insights)
4. [Models Used](#models-used)
5. [Webapp](#webapp)
6. [Installation Guide](#installation-guide)
7. [Usage](#usage)
8. [Contributions](#contributions)
9. [Contact Information](#contact-information)

---

## Project Description
This repository contains a comprehensive Python-based analysis project focused on providing significant insights into the data of an online shop. A SWOT analysis was performed on the shop by undergoing a deep exploratory search into its sales data from December 2009 to November 2011.
A plan was developed on the basis of it and a dashboard was developed to help the team understand the company better and be able to navigate through it. 

---

## Exploratory:
**DATA CLEANING INSIGHTS:**   
- 70.000 rows were cleared.  
- 3.000 which were not marked as cancelled o negative, but had not been taken off the dataset. They artificially inflated the dataset 5%. If the shop counted them as real they would have much false hopes.   
- 6.4% of invoices, (570.000) products were not shipped because of human error.   
The shop can expect 75.000£ in bad debts for the year 2012.   

**CANCELLATIONS:** 
- 17% invoices (733.000 products wer cancelled.
- Found harmful customers with hgih % of cancellations to look at by marketing team.
- Developed a model that can predict future cancellations with 95% accuracy. It will hopefully help the shop run more efficiently.
- Saw a small relationship between country distance and cancellations.
- Obtained a list of countries to investigate (USA 30% invoices cancelled...)

**UNDERSTANDING DATASET** 
- Managed to identify wholesale and retail customers. Helpful for prior analysis.
Thanks to this, it was discovered that some wholesale customers are not registering to the shop, therefore the shope can't track and increase loyalty and hand offers.

**CUSTOMER SPENDING:**
- Saw few customers accounted for most of the sales. Ex. Top 500/5800 accounted to almost half the sales and products bought.
- Saw that more products != more sales for top customers. Needs more investigation.

**PRODUCTS:**
- Saw that stock could be managed much more efficiently. Ex. 1000/5000 products account for just 0.6% of sales. 2.500 products could be removed from stock without major impact. - - Should focus more on top selling products and their variations.

**RFM AND CLUSTERING:**
- Identified and classified different customer segments.
- Top customers for RFM and Kmeans agreed, rest different possibilities.
- Will likely stick to RFM to hand classification to marketing team.

**A PRIORI:** 
- Used A priori to find relationships between products and specially saw how product variations were bought together greatly. Sign of wholesale cuswtomers. Good idea to hand offers or sell in packs.
- Need to investigate more to see how those nodes of product variations connect with others for pack cross-selling.

**RECOMMENDATION ENGINE:** 
- Used collaborative filtering for top customers to obtain a list of top ten products to recommend them.
- Together with A priori findings should give marketing team good insights for increasing top customers spend.

---

## Deep Learning
Used Deep Learning for stock and customer spending prediction. Files not available due to copyright. 

---

## Webapp
An interactive dashboard was created using Streamlit. This webapp allows the shop's team to easily navigate through the data, visualizing insights and tracking shop performance. 

---

## Technologies
This project was developed with the following technologies:
* Python
* Streamlit
* Various data analysis libraries such as Pandas, NumPy, and Matplotlib

---

## Installation Guide
Please follow these steps to install the project:

1. Clone this repository: `git clone [repo link]`
2. Install the necessary libraries: `pip install -r requirements.txt`

---

## Usage
After installation, you can run the Streamlit app by using the command: `streamlit run app.py`

This will launch the Streamlit server, and you can view the dashboard in your web browser at the provided localhost URL.

---

## Contributions
Contributions, issues, and feature requests are welcome! 

---

## Contact Information
If you have any questions, issues or you need assistance, feel free to contact us at:

* [Email](mailto:"luisalarconriva@gmail.com")
* [LinkedIn](https://www.linkedin.com/in/luis-alarc%C3%B3n-de-la-lastra-810113122/)
