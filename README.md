# Project_Analisis_Data
Proyek ini bertujuan untuk menganalisis kualitas udara di Kota Changping berdasarkan data polusi udara seperti PM2.5 dan PM10. Data eksplorasi dilakukan untuk memahami pola fluktuasi polusi berdasarkan waktu, musim, dan faktor lingkungan seperti curah hujan dan kecepatan angin.

# Setup Environment Python
``` bash
brew install python
python3 --version`
pip3 install -r requirements.txt
```

# Setup Environment Streamlit
```bash
pip3 install streamlit
pip3 show streamlit
pip3 install -r requirements.txt
```

# Periksa Apakah Python dan Pip Berjalan Dengan Benar
```bash
which Python3
which pip
```

# Menjalankan Dasboard
Masuk Ke Folder Tempat File Dasboard.py Berada

```bash
cd "Project_Analisis_Data/Dasboard"
python3 -m streamlit run Dasboard.py
```
## (opional) jika ada error, coba tutup terminal dan buka kembali, atau pastikan Streamlit ada di PATH dengan:
```bash
export PATH=$HOME/.local/bin:$PATH
```

lalu jalankan kembali dasboard dengan:
```bash
python3 -m streamlit run Dasboard.py
```
