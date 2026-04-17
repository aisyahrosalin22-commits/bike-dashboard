import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data hasil cleaning (FIX PATH)
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'main_data.csv')

day_df = pd.read_csv(file_path)
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

st.title("🚲 Bike Sharing Dashboard")

# Filter
season = st.selectbox("Pilih Musim", day_df['season'].unique())
filtered_df = day_df[day_df['season'] == season]

# Line chart
st.subheader("Tren Penyewaan")
st.line_chart(filtered_df.set_index('dteday')['cnt'])

# Bar chart
st.subheader("Rata-rata Penyewaan per Musim")
fig, ax = plt.subplots()
sns.barplot(data=day_df, x='season', y='cnt', ax=ax)
st.pyplot(fig)