# Project_Analisis_Data
Proyek ini bertujuan untuk menganalisis kualitas udara di Kota Changping berdasarkan data polusi udara seperti PM2.5 dan PM10. Data eksplorasi dilakukan untuk memahami pola fluktuasi polusi berdasarkan waktu, musim, dan faktor lingkungan seperti curah hujan dan kecepatan angin.

# Setup Environment Python
``` bash
brew install python
python3 --version
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
which pip3
```
## Jika Ya, akan muncul (/usr/bin/pip3) Lanjutkan
# Menjalankan Dasboard
Navigasikan Ke Folder Tempat File dasboard.py berada. Contoh:
```bash
cd Downloads/Project_Analisis_Data-main/Dasboard
```
Lalu gunakan perintah untuk menjalankan aplikasi:

```bash
python3 -m streamlit run dasboard.py
```

## (opional) jika ada error (pip not found)
1. jalankan perintah berikut untuk menginstall pip:
```bash
python3 -m ensurepip --default-pip
```
2. atau secara manual:
```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3
```
3. jika pip tidak dikenali, tambahkan pip ke Path dengan:
```bash
export PATH=$HOME/.local/bin:$PATH
```
lalu jalankan kembali dasboard dengan:
```bash
python3 -m streamlit run dasboard.py
```
