# Project Analisis Data
Dashboard interaktif dibuat menggunakan Streamlit, memungkinkan pengguna untuk mengeksplorasi data berdasarkan rentang waktu, musim, kondisi cuaca, serta memahami hubungan dengan faktor lingkungan seperti curah hujan dan kecepatan angin.

# #Penginstalan Pada macOS
## 1. Setup Environment Python
```
brew install python
python3 --version
```

## 2. Setup Environment Streamlit
Navigasikan Ke Folder Tempat Dashboard
```
cd Downloads/Project_Analisis_Data-main/Dasboard
pip3 install -r requirements.txt
pip3 install streamlit
pip3 show streamlit
```

## 3. Periksa Apakah Python dan Pip Berjalan Dengan Benar
```
which Python3
which pip3
```
> jika Ya, akan muncul (/opt/homebrew/bin/pip3) Lanjutkan

## 4. Menjalankan Dasboard
Gunakan perintah untuk menjalankan aplikasi:
```bash
python3 -m streamlit run dashboard.py
```


> [!TIP]
> Jika terdapat error **_"No module named streamlit"_**, ini terjadi karena sistem macOS tidak mengizinkan pemasangan paket python secara langsung menggunakan pip3 install streamlit seperti di atas.
> 1. jalankan perintah berikut jika streamlit tersedia di Homebrew:
>```
>brew install streamlit
>```
>2. jika tidak tersedia, gunakan virtual environtment:
>```
>python3 -m venv myenv
>sourch myenv/bin/active
>python3 -m pip install streamlit
>```
>3. periksa apakah streamlit sudah terinstal:
>```
>pip3 show streamlit
>```
>4. lalu jalankan kembali dashboard dengan:
>```
>python3 -m streamlit run dashboard.py
>```
>
> Jika terdapat error **_"pip not found"_**, 
>1. jalankan perintah berikut untuk menginstall pip:
>```
>python3 -m ensurepip --default-pip
>```
>2. atau secara manual:
>```
>curl -sS https://bootstrap.pypa.io/get-pip.py | python3
>```
>3. jika pip tidak dikenali, tambahkan pip ke Path dengan:
>```
>export PATH=$HOME/.local/bin:$PATH
>```
>4. lalu jalankan kembali dasboard dengan:
>```
>python3 -m streamlit run dashboard.py
>```

# #Penginstalan Pada Windows
## 1. Pastikan python telah terinstall
- unduh dan installl Python dari [python.org](https://www.python.org/downloads/)
- saat instalasi, pastikan opsi **Add Python to PATH** dicentang
- cek apakah python dan pip sudah tersedia dengan:
  ```
  python --version
  pip --vesion
  ```
  
## 2. Pastikan depensasi terinstall
```
pip install -r requirements.txt
```

## 3. Install streamlit
```
python -m ensurepip --default-pip
pip install streamlit
```
> jika streamlit tidak ditemukan, coba
> ```
> python -m ensurepip --defaultl-pip
> pip install streamlit
> ```

## 4. Jalankan dashboard
- navigasikan ke folder tempat **dashboar.py** dengan ```cd C:\Users\NamaPengguna\Downloads\Project_Analisis_Data-main\Dashboard```
- jalankan streamlit dengan ```streamlit run dashboard.py```
