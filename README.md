📊 Saudi Job Market Analysis (Jadarat Dataset)
📌 Overview

This project analyzes job postings from the Saudi Jadarat platform to understand hiring trends, salaries, regions, company sizes, and job titles.
The project also includes an interactive Streamlit dashboard that allows users to explore the data with filters.

🎯 Goals

Clean and prepare the dataset

Analyze salaries, experience levels, and job demand

Compare regions and company sizes

Identify top hiring companies and highest-paying job titles

Build a simple and interactive dashboard

🧹 Data Cleaning

Removed missing and duplicated rows

Converted columns to correct data types

Extracted month & year from job dates

Assigned numeric IDs to company names for visualization

🔍 Key Insights

Most salaries range between 4,000–9,000 SAR

Most jobs require 0–2 years of experience

Highest hiring activity: Riyadh, Makkah, Eastern Region

Large companies pay higher salaries

Hiring peaks in November and December

Highest-paying roles are usually Engineering, Technical, or Managerial

⚠️ Challenges

Regional data was imbalanced, causing biased charts

Some regions had very few entries, which created misleading results

Solved by focusing on the main regions only

📈 Streamlit Dashboard

Run the dashboard with:

streamlit run app.py


Dashboard features:

Salary & experience visualizations

Region and job title filters

Monthly hiring trends

Top hiring companies

🛠 Tools Used

Python

Pandas

Seaborn

Matplotlib

Streamlit

✔ Conclusion

This project provides a clear overview of job trends in Saudi Arabia and shows how data cleaning + visualization can help uncover useful insights about the labor market.
