import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'main_data.csv')

day_df = pd.read_csv(file_path)
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

st.title("🚲 Bike Sharing Dashboard")

# ======================
# FILTER
# ======================
season_options = ['All'] + sorted(day_df['season'].unique())
selected_season = st.selectbox("Pilih Musim", season_options)

if selected_season == 'All':
    filtered_df = day_df
else:
    filtered_df = day_df[day_df['season'] == selected_season]

# ======================
# VISUALISASI 1 (TREND)
# ======================
st.subheader("📈 Tren Penyewaan Sepeda")

st.line_chart(filtered_df.set_index('dteday')['cnt'])

# ======================
# VISUALISASI 2 (MUSIM)
# ======================
st.subheader("📊 Penyewaan Berdasarkan Musim")

fig1, ax1 = plt.subplots()
sns.barplot(data=filtered_df, x='season', y='cnt', ax=ax1)
ax1.set_title("Rata-rata Penyewaan per Musim")
st.pyplot(fig1)

# ======================
# VISUALISASI 3 (CUACA)
# ======================
st.subheader("🌤️ Penyewaan Berdasarkan Cuaca")

fig2, ax2 = plt.subplots()
sns.barplot(data=filtered_df, x='weathersit', y='cnt', ax=ax2)
ax2.set_title("Rata-rata Penyewaan berdasarkan Cuaca")
st.pyplot(fig2)
