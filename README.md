# Project_Analisis_Data
Proyek ini bertujuan untuk menganalisis kualitas udara di Kota Changping berdasarkan data polusi udara seperti PM2.5 dan PM10. Data eksplorasi dilakukan untuk memahami pola fluktuasi polusi berdasarkan waktu, musim, dan faktor lingkungan seperti curah hujan dan kecepatan angin.

# Setup Environment Python
``` bash
brew install python
python3 --version
```

# Setup Environment Streamlit
Navigasikan Ke Folder Tempat Dashboard
```bash
cd Downloads/Project_Analisis_Data-main/Dasboard
pip3 install -r requirements.txt
pip3 install streamlit
pip3 show streamlit
```

# Periksa Apakah Python dan Pip Berjalan Dengan Benar
```bash
which Python3
which pip3
```
## Jika Ya, akan muncul (/opt/homebrew/bin/pip3) Lanjutkan
# Menjalankan Dasboard
Lalu gunakan perintah untuk menjalankan aplikasi:

```bash
python3 -m streamlit run dashboard.py
```

## (opional) jika ada error (No module named streamlit)
Ini terjadi karena sistem macOS tidak mengizinkan pemasangan paket python secara langsung menggunakan pip3 install streamlit seperti di atas.
1. jalankan perintah berikut jika streamlit tersedia di Homebrew:
```bash
brew install streamlit
```
2. jika tidak tersedia, gunakan virtual environtment:
```bash
python3 -m venv myenv
sourch myenv/bin/active
python3 -m pip install streamlit
```
3. periksa apakah streamlit sudah terinstall:
```bash
pip3 show streamlit
```
4. lalu jalankan kembali dashboard dengan:
```bash
python3 -m streamlit run dashboard.py
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
python3 -m streamlit run dashboard.py
```
