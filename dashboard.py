import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Styling
sns.set_style("whitegrid")

# =========================
# LOAD DATA
# =========================
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "main_data.csv")

day_df = pd.read_csv(file_path)
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['year'] = day_df['dteday'].dt.year

# =========================
# TITLE
# =========================
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Analisis penyewaan sepeda berdasarkan musim, cuaca, dan tren waktu")

# =========================
# FILTER
# =========================
st.sidebar.header("🔍 Filter Data")

# FILTER MUSIM
season_option = st.sidebar.selectbox(
    "Pilih Musim",
    ["All"] + sorted(day_df['season'].dropna().unique())
)

# FILTER TAHUN (INI PENGGANTI DATE)
year_option = st.sidebar.selectbox(
    "Pilih Tahun",
    ["All"] + sorted(day_df['year'].unique())
)

# =========================
# APPLY FILTER
# =========================
filtered_df = day_df.copy()

if season_option != "All":
    filtered_df = filtered_df[filtered_df['season'] == season_option]

if year_option != "All":
    filtered_df = filtered_df[filtered_df['year'] == year_option]

# =========================
# VISUALISASI 1: MUSIM
# =========================
st.subheader("📊 Rata-rata Penyewaan Berdasarkan Musim")

fig1, ax1 = plt.subplots()
sns.barplot(data=filtered_df, x='season', y='cnt', ax=ax1)

ax1.set_title("Rata-rata Penyewaan Sepeda per Musim")
ax1.set_xlabel("Musim")
ax1.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig1)

# =========================
# VISUALISASI 2: CUACA
# =========================
st.subheader("🌦️ Rata-rata Penyewaan Berdasarkan Cuaca")

fig2, ax2 = plt.subplots()
sns.barplot(data=filtered_df, x='weathersit', y='cnt', ax=ax2)

ax2.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
ax2.set_xlabel("Kondisi Cuaca")
ax2.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig2)

# =========================
# VISUALISASI 3: TREND BULAN PER TAHUN
# =========================
st.subheader("📈 Tren Penyewaan Sepeda per Bulan")

monthly_trend = filtered_df.groupby(['year', 'mnth'])['cnt'].mean().reset_index()

fig3, ax3 = plt.subplots()

for year in sorted(monthly_trend['year'].unique()):
    data = monthly_trend[monthly_trend['year'] == year]
    ax3.plot(data['mnth'], data['cnt'], marker='o', label=f"Tahun {year}")

ax3.set_title("Tren Penyewaan Sepeda per Bulan")
ax3.set_xlabel("Bulan")
ax3.set_ylabel("Jumlah Penyewaan")
ax3.legend(title="Tahun")

st.pyplot(fig3)

# =========================
# INSIGHT
# =========================
st.subheader("📌 Insight Utama")

st.markdown("""
- Musim Fall dan Summer menunjukkan penyewaan tertinggi.
- Cuaca cerah (Clear) menghasilkan jumlah penyewaan paling tinggi.
- Cuaca buruk seperti Light Snow menurunkan jumlah penyewaan secara signifikan.
- Tren bulanan menunjukkan pola musiman:
  - Pertengahan tahun (Juni–September) = peak season
  - Awal tahun (Januari–Februari) = low season
- Perbandingan antar tahun membantu menentukan strategi operasional yang lebih tepat.
""")
