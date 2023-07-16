# Online Shop Analytics Project

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
This repository contains a comprehensive Python-based analysis project focused on an online shop. The idea is to provide significant business insights in the form of a SWOT analysis, and to develop and deploy useful tools for the business to navigate the future guided by data. 

The shop is based in the UK and sells unique all-ocassion gifts to both wholesale and retail customers in 34 different countries.

**The dataset is the Online Retail Dataset II, and is comprised of:**
- 1.067.000 rows.
- 8 columns each accounting for a transaction.
- Time period ranging from 01-12-2009 to 09-12-2011 (540 days).
- 5800 customers.

**The project involved the following:**

1. Cleaning data and learning from its errors.
2. Exploratory search for business insights. 
4. Investigating into product and customer spending.
5. RFM and kmeans analysis.
7. A prior analysis and user-based collaborative filtering.
9. Stock and customer spending prediction with Deep Learning.
10. Developing Webapp for shop team to predict, plan, execute, and monitor improvements in the future.


---

## SWOT:
**Cleaning data and learning from its errors:**   
- 70.000 rows were cleared.  
- 3.000 which were not marked as cancelled o negative, but had not been taken off the dataset. They artificially inflated the dataset 5%. If the shop counted them as real they would have much false hopes.   
- 6.4% of invoices, (570.000) products were not shipped because of human error.   
The shop can expect 75.000£ in bad debts for the year 2012.

**Understanding the Dataset** 
- Managed to identify wholesale and retail customers. Helpful for prior analysis.
Thanks to this, it was discovered that some wholesale customers are not registering to the shop, therefore the shop can't track and increase loyalty and hand offers.

**Investigating Cancellations:** 
- 17% invoices (733.000) products wer cancelled.
- Found harmful customers with hgih % of cancellations to look at by marketing team.
- Developed a model that can predict future cancellations with 95% accuracy. It will hopefully help the shop run more efficiently.
- Saw a small relationship between country distance and cancellations.
- Obtained a list of countries to investigate (USA 30% invoices cancelled...)

**Digging into customer spending:**
- Saw few customers accounted for most of the sales. Ex. Top 500/5800 accounted to almost half the sales and products bought.
- Saw that more products != more sales for top customers. Needs more investigation.

**Delving into product performance:**
- Saw that stock could be managed much more efficiently. Ex. 1000/5000 products account for just 0.6% of sales. 2.500 products could be removed from stock without major impact. - - Should focus more on top selling products and their variations.

**RFM and Clustering:**
- Identified and classified different customer segments.
- Top customers for RFM and Kmeans agreed, rest different possibilities.
- Will likely stick to RFM to hand classification to marketing team.

**A priori:** 
- Used A priori to find relationships between products and specially saw how product variations were bought together greatly. Sign of wholesale cuswtomers. Good idea to hand offers or sell in packs.
- Need to investigate more to see how those nodes of product variations connect with others for pack cross-selling.

**Recommendation Engine:** 
- Used collaborative filtering for top customers to obtain a list of top ten products to recommend them.
- Together with A priori findings should give marketing team good insights for increasing top customers spend.

## SWOT Results:

###**Strenghts:** 
- Shop has a small group of top clients driving sales.
- 18% of customers = 71% of sales.
- Identified profile for business development with similar customers/companies.
- Identified which customers to prioritise and target with offers.
- Identified group of cutomers with potential to become top spenders and increase sales.
- Very strong base country in UK (85% of sales).

###**Weaknesses:** 
- 9.4% of orders was cancelled due to human error. (569.314 products not shipped).
- Human error cancellations were highest in springbreak sales peak and stocking months, however not on peak christmas sales months. Shop probably prepares well for christmas activity but doesn't do a good job the rest of the months underestimating the workload.
- Stock inneficiencies / Too many products in stock - Top 2000 products account for 92% of sales, 3395 are almost always on the digital shelf and cost the shop both time and money. Recalibrating stock would greatly optimise performance.
- Missed client opportunities - Managed to identify and differentiate wholesale and retail. Thanks to that and some data not making sense and its investigation, it was found that 11%  were top quality clients who where not registering as wholesale and were therefore being lost in terms of fidelisation, targeting for offers, and growth. Shop should facilitate the sign up, investigate why they are not registering, and offer direct benefits of registering as wholesale. Biggest unregistered basket was 14.000 products...
- Potential artificial self-perception - Managed to match records and find that 1365 cancelled invoices had not had their cuonterparts removed (344.714 products), including the shops 2 biggest transactions. If the shop was accounting for these sales an insidious artificial self perception was weakening it.
- Bad Debts - Found bad depts and estimated 75.000 pounds for 2012.

###**Threats:** 

Cancellations:
      - 16.9% of invoices were eventually cancelled.
      - 97% were done by wholesale customers. Coincidently big baskets were the most cancelled ones. There could be possible problems like slow processes in order preparation when they become too big. It should be investigated thoroughly as most valuable baskets are being lost.
      - Found group of customers with high number of cancellations to be aware of. Top cancelling customer cancelled 95 orders (could be investigated to learn possible patterns). 
      - Group of customers with at least 1 cancellation have cancelled 30% of their orders.
      - Found group of countries with high percentage of cancellations to investigate (For example USA 31%, Japan 21% and Korea 19%).
      - Found small relationship between country distance and cancellations.
Shipping, order response, and customer support reaction times should be investigated and worked on to reduce cancellations. Possible problems with customs and generated expectations should be taken a look at as well.
      
###**Opportunities:** 

- Cancellations - Developed model for a cancellation detector seeking a smoother running of the shop. It was incorporated into the webapp for team testing.
- A priori analysis - Found signs of wholesale activity purchasing in bulk. Found tightly knit groups of product variations to sell in packs for sales increase. The processed relationships between products where uploaded to the webapp.
- Recommendation Engine - Recommending products the customer had not bought previously based on closest neighbour/customer. Opening new cross-selling possibilities. Incorporated product recommendations per customer in webapp.
- Stock and Sales prediction (Deep Learning) - Useful for monitoring customer spending and setting alarms calling for action when sale decreased below a certain threshhold. Also for efficienting stock planning, optimizing logistics and decreasing human error. Incorporated into Webapp.
- Customer Statistics - Incorporated profiles per customer including his/her quality and various stats which will help define, understand and look after customers better.


---

## Deep Learning
Used Deep Learning for stock and customer spending prediction. Files not available due to copyright. 

Model used:
- Sequential
       - Input LSTM layer with 98 neurons.
       - Middle dense 10 neuron layer.
       - Final dense 1 neuron layer.
       - 50 epocs.
       - 70% accuracy. Work to be done yet.

---

## Webapp
An interactive dashboard was created using Streamlit. This webapp allows the shop's team to easily navigate through the data, visualizing insights and tracking shop performance. 

Appart from mentioned tools, webapp has:

- A dashboard tracking shop performance.
- A customer profile with various different stats.

[![Video Demo](https://drive.google.com/uc?export=view&id=1u_kL-3Cm6bmjS0-WY5HvdGoIl4nVlCHZ)](http://www.youtube.com/watch?v=lbs-DYDiUv8 "Video Demo")

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
