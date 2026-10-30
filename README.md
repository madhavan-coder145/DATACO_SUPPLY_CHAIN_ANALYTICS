# 🚀 DataCo Supply Chain Analytics - End to End Project

## 📌 Project Overview
Analyzed **180,519 orders** of DataCo Global Supply Chain dataset to solve late delivery issues and improve profit.

## 🎯 Problem Statement
- 55% orders are late delivered
- Standard Class shipping = 58% late
- Company losing profit & customers

## 🧹 Data Cleaning Done (Important for Interview)
1.  Customer Email, Password, Product Description = `XXXX` masked (Privacy)
2.  Order Zipcode = All empty/null - Removed column
3.  Duplicate rows checked
4.  Date format fixed (order_date, shipping_date)

## 📊 Tools Used
- **Excel:** Initial data profiling, Pivot tables
- **SQL:** 15+ Business questions (MySQL)
- **Python:** EDA, Late Delivery Prediction (Random Forest 91% Accuracy)
- **Power BI:** Interactive Dashboard with 8 KPIs

## 🔍 Key Insights Found
- **Shipping Mode:** Standard Class 58% Late vs Same Day 95% On-Time
- **Region:** South America & Eastern Europe Highest Late
- **Department:** Fan Shop worst affected
- **Profit Loss:** Late orders = $2.3M less profit

## 💡 Business Recommendations
1. Stop Standard Class for critical regions, push Express
2. Increase warehouse in South America
3. Alert system for predicted late orders using ML model

## 📁 Files in Repo
- `data_cleaning.py` - Full cleaning code
- `sql_queries.sql` - All 15 business queries
- `powerbi_dashboard.pbix` - Dashboard file
- `ml_model.py` - Late delivery prediction

## 👨‍💻 Author
Madhavan | Aspiring Data Analyst | Python, SQL, Power BI