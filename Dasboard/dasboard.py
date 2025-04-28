import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dasboard/Cleaned_PRSA_Data_Changping.csv")

# Konversi datetime
df["datetime"] = pd.to_datetime(df["year"].astype(str) + "-" + 
                                df["month"].astype(str) + "-" + 
                                df["day"].astype(str) + " " + 
                                df["hour"].astype(str) + ":00:00")

# Header dashboard
st.title("Dashboard Kualitas Udara Kota Changping 🌫️🌍")
st.write("Analisis tren PM2.5 dan PM10 berdasarkan waktu dan faktor lingkungan.")

# Visualisasi Tren PM2.5 dan PM10
st.subheader("Tren PM2.5 dan PM10")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=df["datetime"], y=df["PM2.5"], label="PM2.5", ax=ax)
sns.lineplot(x=df["datetime"], y=df["PM10"], label="PM10", ax=ax)
plt.xticks(rotation=45)
plt.title("Tren PM2.5 dan PM10 dari Waktu ke Waktu")
st.pyplot(fig)

# Boxplot berdasarkan musim
df["season"] = df["month"].apply(lambda x: "Winter" if x in [12,1,2] else 
                                           "Spring" if x in [3,4,5] else 
                                           "Summer" if x in [6,7,8] else "Fall")
st.subheader("Distribusi PM2.5 Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x=df["season"], y=df["PM2.5"], ax=ax)
plt.title("PM2.5 Berdasarkan Musim")
st.pyplot(fig)

# Boxplot PM2.5 hari kerja vs akhir pekan
df["weekend"] = df["datetime"].dt.dayofweek >= 5
st.subheader("Polusi PM2.5 pada Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x=df["weekend"], y=df["PM2.5"], ax=ax)
plt.title("PM2.5 Hari Kerja vs Akhir Pekan")
st.pyplot(fig)

# Scatterplot hubungan CO dan PM2.5
st.subheader("Hubungan CO dan PM2.5")
fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(x=df["CO"], y=df["PM2.5"], ax=ax)
plt.title("Hubungan Antara CO dan PM2.5")
st.pyplot(fig)

st.write("Dashboard ini membantu memahami pola polusi udara dan faktor yang memengaruhinya")

