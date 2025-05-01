import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Cleaned_PRSA_Data_Changping.csv")

# Konversi datetime
df["datetime"] = pd.to_datetime(df["year"].astype(str) + "-" + 
                                df["month"].astype(str) + "-" + 
                                df["day"].astype(str) + " " + 
                                df["hour"].astype(str) + ":00:00")

# Identifikasi musim
df["season"] = df["month"].apply(lambda x: "Winter" if x in [12,1,2] else 
                                           "Spring" if x in [3,4,5] else 
                                           "Summer" if x in [6,7,8] else "Fall")

# Header dashboard
st.title("Dashboard Kualitas Udara Kota Changping 🌫️🌍")

# **Penjelasan PM2.5 dan PM10**
st.markdown("""
### 🔎 Apa Itu PM2.5 dan PM10?
PM2.5 dan PM10 adalah partikel udara yang berukuran kecil dan dapat mempengaruhi kesehatan manusia:
- **PM2.5** memiliki ukuran ≤ 2.5 mikrometer, sangat kecil dan bisa masuk ke paru-paru bahkan aliran darah.
- **PM10** lebih besar (≤ 10 mikrometer), berasal dari debu jalanan atau aktivitas industri.

Keduanya berkontribusi terhadap polusi udara dan bisa memengaruhi kesehatan pernapasan, terutama bagi penderita asma atau penyakit paru-paru. Dashboard ini bertujuan untuk menganalisis pola polusi berdasarkan **waktu, musim, dan faktor lingkungan** seperti cuaca dan tingkat CO.
""")

# **Sidebar untuk Filter Interaktif**
st.sidebar.header("Filter Data")

# Filter berdasarkan rentang tanggal
start_date = st.sidebar.date_input("Pilih tanggal mulai", df["datetime"].min().date())
end_date = st.sidebar.date_input("Pilih tanggal akhir", df["datetime"].max().date())
df_filtered = df[(df["datetime"].dt.date >= start_date) & (df["datetime"].dt.date <= end_date)]

# Filter berdasarkan musim
season_selected = st.sidebar.multiselect("Pilih musim", df["season"].unique(), default=df["season"].unique())
df_filtered = df_filtered[df_filtered["season"].isin(season_selected)]

# Filter berdasarkan cuaca (pastikan kolom 'weather' ada di dataset)
if "weather" in df.columns:
    weather_selected = st.sidebar.multiselect("Pilih cuaca", df["weather"].unique(), default=df["weather"].unique())
    df_filtered = df_filtered[df_filtered["weather"].isin(weather_selected)]

# **Visualisasi Tren PM2.5 dan PM10**
st.subheader("Tren PM2.5 dan PM10")
if not df_filtered.empty:
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=df_filtered["datetime"], y=df_filtered["PM2.5"], label="PM2.5", ax=ax)
    sns.lineplot(x=df_filtered["datetime"], y=df_filtered["PM10"], label="PM10", ax=ax)
    plt.xticks(rotation=45)
    plt.title("Tren PM2.5 dan PM10 dari Waktu ke Waktu")
    st.pyplot(fig)
else:
    st.warning("Data tidak tersedia untuk filter yang dipilih.")

# **Distribusi PM2.5 Berdasarkan Musim**
st.subheader("Distribusi PM2.5 Berdasarkan Musim")
if not df_filtered.empty:
    fig, ax = plt.subplots(figsize=(8,6))
    sns.boxplot(x=df_filtered["season"], y=df_filtered["PM2.5"], ax=ax)
    plt.title("PM2.5 Berdasarkan Musim")
    st.pyplot(fig)
else:
    st.warning("Data tidak tersedia untuk filter yang dipilih.")

# **Polusi PM2.5 pada Hari Kerja vs Akhir Pekan**
df_filtered["weekend"] = df_filtered["datetime"].dt.dayofweek >= 5
st.subheader("Polusi PM2.5 pada Hari Kerja vs Akhir Pekan")
if not df_filtered.empty:
    fig, ax = plt.subplots(figsize=(8,6))
    sns.boxplot(x=df_filtered["weekend"], y=df_filtered["PM2.5"], ax=ax)
    plt.title("PM2.5 Hari Kerja vs Akhir Pekan")
    st.pyplot(fig)
else:
    st.warning("Data tidak tersedia untuk filter yang dipilih.")

# **Scatterplot Hubungan CO dan PM2.5**
st.subheader("Hubungan CO dan PM2.5")
if "CO" in df_filtered.columns and not df_filtered.empty:
    fig, ax = plt.subplots(figsize=(8,6))
    sns.scatterplot(x=df_filtered["CO"], y=df_filtered["PM2.5"], ax=ax)
    plt.title("Hubungan Antara CO dan PM2.5")
    st.pyplot(fig)
else:
    st.warning("Data tidak tersedia untuk filter yang dipilih.")

st.write("Gunakan sidebar untuk menyaring data sesuai kebutuhan.")
