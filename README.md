# README - Data Cleaner A1

# Description (English)

## This application is a Data Cleaner tool built using PyQt6 and pandas. It allows users to select an input file (Excel or CSV) and an output folder, process the data to clean up null values, detect outliers, check for data type anomalies, and apply a few other transformations. The cleaned data is saved into an Excel file with multiple sheets, including unfiltered data, hygiene (cleaned data), and findings (anomalies detected).

## Features:
	•	Select File: Load the input Excel or CSV file.
	•	Select Output Folder: Choose the destination folder to save the cleaned file.
	•	Handle Null Values: Option to keep nulls, fill with mean, or custom value.
	•	Outlier Detection: Automatically detects and removes outliers based on the IQR method.
	•	Data Type Anomalies: Identifies columns with invalid data types and flags them.
	•	Uppercase Conversion: Converts all string values to uppercase if needed.
	•	Progress Bar: Shows progress during data processing.

## Requirements:
	•	Python 3.x
	•	PyQt6: For creating the GUI.
	•	pandas: For data manipulation and cleaning.
	•	numpy: For numerical operations.
	•	datetime: For timestamping the output files.

## Installation:
	1.	Install the necessary Python libraries:

## pip install PyQt6 pandas numpy

	2.	Download or clone this repository and run the data_cleaner.py script.

## How to Use:
	1.	Open the application.
	2.	Click “Select File” to choose the input Excel or CSV file.
	3.	Click “Select Output Folder” to choose where to save the cleaned data.
	4.	Click “Start Processing” to begin cleaning the data.
	5.	Once processing is complete, the cleaned file will be saved in the selected folder with timestamped filename.

## Example Use Case:

## You have a CSV or Excel file that contains sales data, with some missing values, outliers, and possibly incorrect data types. You can use this tool to:
	•	Fill or replace missing values.
	•	Remove any outliers in the numerical columns.
	•	Detect and flag any anomalies in data types (e.g., strings in numeric columns).
	•	Convert all text fields to uppercase for consistency.

## License:

This project is licensed under the MIT License.

# Deskripsi (Bahasa Indonesia)

Aplikasi ini adalah alat Data Cleaner yang dibangun menggunakan PyQt6 dan pandas. Aplikasi ini memungkinkan pengguna untuk memilih file input (Excel atau CSV) dan folder output, kemudian memproses data untuk membersihkan nilai null, mendeteksi outlier, memeriksa anomali tipe data, dan menerapkan beberapa transformasi lainnya. Data yang sudah dibersihkan akan disimpan dalam file Excel dengan beberapa sheet, termasuk data yang tidak difilter, data yang sudah dibersihkan, dan temuan (anomali yang terdeteksi).

## Fitur:
	•	Pilih File: Memuat file input Excel atau CSV.
	•	Pilih Folder Output: Pilih folder tujuan untuk menyimpan file yang sudah dibersihkan.
	•	Menangani Nilai Null: Pilihan untuk mempertahankan null, mengisi dengan nilai rata-rata, atau nilai kustom.
	•	Deteksi Outlier: Secara otomatis mendeteksi dan menghapus outlier berdasarkan metode IQR.
	•	Anomali Tipe Data: Mengidentifikasi kolom dengan tipe data yang tidak valid dan memberi tanda.
	•	Konversi ke Uppercase: Mengonversi semua nilai string ke uppercase jika diperlukan.
	•	Progress Bar: Menampilkan progres saat pemrosesan data.

##  Persyaratan:
	•	Python 3.x
	•	PyQt6: Untuk membuat antarmuka pengguna grafis (GUI).
	•	pandas: Untuk manipulasi dan pembersihan data.
	•	numpy: Untuk operasi numerik.
	•	datetime: Untuk menandai waktu pada file output.

## Instalasi:
	1.	Instal pustaka Python yang diperlukan:

## pip install PyQt6 pandas numpy

	2.	Unduh atau clone repositori ini dan jalankan skrip data_cleaner.py.

## Cara Menggunakan:
	1.	Buka aplikasi.
	2.	Klik “Select File” untuk memilih file input Excel atau CSV.
	3.	Klik “Select Output Folder” untuk memilih tempat menyimpan data yang sudah dibersihkan.
	4.	Klik “Start Processing” untuk memulai proses pembersihan data.
	5.	Setelah pemrosesan selesai, file yang sudah dibersihkan akan disimpan di folder yang dipilih dengan nama file yang mengandung timestamp.

## Contoh Kasus Penggunaan:

## Anda memiliki file CSV atau Excel yang berisi data penjualan, dengan beberapa nilai yang hilang, outlier, dan kemungkinan tipe data yang salah. Anda dapat menggunakan alat ini untuk:
	•	Mengisi atau mengganti nilai yang hilang.
	•	Menghapus outlier pada kolom numerik.
	•	Mendeteksi dan memberi tanda pada anomali tipe data (misalnya, string pada kolom numerik).
	•	Mengonversi semua kolom teks ke uppercase untuk konsistensi.

## Lisensi:

## Proyek ini dilisensikan di bawah Lisensi MIT.
