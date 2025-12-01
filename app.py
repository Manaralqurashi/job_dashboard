import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Saudi Job Market Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_dataset.csv")
    return df

df = load_data()

# Fix missing date columns
df['job_date'] = pd.to_datetime(df['job_date'], errors='coerce')
df['post_month'] = df['job_date'].dt.month
df['post_year'] = df['job_date'].dt.year

# Title
st.title("📊 Saudi Job Market")
st.markdown("This dashboard provides an interactive analysis of salaries, experience, companies, and job market trends across Saudi Arabia.")

# =====================================
#               KPI SECTION
# =====================================
st.subheader("📌 Key Market Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Job Postings", df.shape[0])

with col2:
    st.metric("Average Salary (SAR)", f"{df['salary'].mean():.0f}")

with col3:
    st.metric("Most Common Experience", f"{df['experience_years'].mode()[0]} years")

with col4:
    st.metric("Number of Regions", df['region'].nunique())

st.markdown("---")

# =====================================
#            SIDEBAR FILTERS
# =====================================
st.sidebar.title("Filters & Dataset Info")

st.sidebar.markdown("""
### 📘 Dataset Description  
This dataset is collected from **Jadarat**, the official Saudi employment platform.  
It includes job postings from governmental, private, and semi-government organizations.
""")

st.sidebar.markdown("---")

salary_min, salary_max = st.sidebar.slider(
    "Select Salary Range (SAR):",
    int(df["salary"].min()),
    int(df["salary"].max()),
    (4000, 15000)
)

exp_min, exp_max = st.sidebar.slider(
    "Select Experience Years:",
    int(df["experience_years"].min()),
    int(df["experience_years"].max()),
    (0, 5)
)

selected_regions = st.sidebar.multiselect(
    "Select Region(s):",
    df["region"].unique(),
    default=list(df["region"].unique())
)

selected_titles = st.sidebar.multiselect(
    "Select Job Title(s):",
    df["job_title"].unique(),
    default=df["job_title"].unique()
)

selected_industries = st.sidebar.multiselect(
    "Select Industry:",
    df["economic_activity"].unique(),
    default=df["economic_activity"].unique()
)



st.sidebar.markdown("---")
st.sidebar.markdown("Filters applied to all visualizations.")

# =====================================
#                APPLY FILTERS
# =====================================
df_filtered = df[
    (df["salary"] >= salary_min) &
    (df["salary"] <= salary_max) &
    (df["experience_years"] >= exp_min) &
    (df["experience_years"] <= exp_max) &
    (df["region"].isin(selected_regions)) &
    (df["job_title"].isin(selected_titles)) &
    (df["economic_activity"].isin(selected_industries))
]


# =====================================
#                DATA PREVIEW
# =====================================
st.subheader("📁 Filtered Dataset Preview")
st.dataframe(df_filtered.head())

st.markdown("---")

# =====================================
#            SALARY SECTION
# =====================================
st.subheader("💰 Salary Analysis")

c1, c2 = st.columns(2)

with c1:
    st.markdown("### Salary Distribution (Boxplot)")
    fig1, ax1 = plt.subplots(figsize=(6,4))
    sns.boxplot(x=df_filtered["salary"], ax=ax1, color="#4C9AFF")
    st.pyplot(fig1)

with c2:
    st.markdown("### Salary Distribution (Histogram)")
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.histplot(df_filtered["salary"], kde=True, ax=ax2, color="#6A5ACD")
    st.pyplot(fig2)

st.markdown("**Insight:** Salaries mostly fall between 4K–9K SAR, with clear outliers indicating high-paying specialized roles.")
st.markdown("---")

# =====================================
#         EXPERIENCE ANALYSIS
# =====================================
st.subheader("🎓 Experience Analysis")

fig3, ax3 = plt.subplots(figsize=(10,4))
sns.histplot(df_filtered["experience_years"], kde=True, ax=ax3, color="#FF6B6B")
st.pyplot(fig3)

st.markdown("**Insight:** Most job postings require 0–2 years of experience, showing a strong focus on junior-level roles.")
st.markdown("---")

# =====================================
#      COMPANY SIZE & SALARY
# =====================================
st.subheader("🏢 Company Size vs Salary")

fig4, ax4 = plt.subplots(figsize=(10,4))
sns.barplot(data=df_filtered, x="company_size", y="salary", estimator="mean", ax=ax4, palette="Blues")
plt.xticks(rotation=30)
st.pyplot(fig4)

st.markdown("""
**Insight:** Larger companies tend to offer higher salaries compared to small and medium-sized companies.

### 📌 Company Size Categories
- **SA** – Small Company (11–50 employees)  
- **MB** – Medium Business (51–249 employees)  
- **MA** – Medium Company (250–999 employees)  
- **L** – Large Company (1000–4999 employees)  
- **G** – Giant / Enterprise (5000+ employees)
""")

st.markdown("---")

# =====================================
#          MONTHLY TREND
# =====================================
st.subheader("📅 Monthly Job Posting Trend")

fig6, ax6 = plt.subplots(figsize=(10,4))
sns.countplot(x=df_filtered["post_month"], ax=ax6, palette="viridis")
st.pyplot(fig6)

st.markdown("**Insight:** Job postings peak in November and December, while October is the lowest month.")
st.markdown("---")

# =====================================
#          TOP COMPANIES
# =====================================
st.subheader("🏅 Top Hiring Companies")

top_companies = df_filtered["company_name"].value_counts().head(10)
st.bar_chart(top_companies)

st.markdown("**Insight:** These companies represent the top employers based on posting frequency.")
st.markdown("---")

st.success("Dashboard Loaded Successfully!")
