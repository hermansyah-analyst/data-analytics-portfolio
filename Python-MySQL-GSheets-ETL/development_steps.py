# # ============================================================
# # STEP 1 — CEK INSTALASI PYTHON
# # ============================================================
# #
# # Sebelum membuat pipeline, kita perlu memastikan bahwa Python
# # sudah terinstall di komputer.
# #
# # Cara pengecekan:
# # 1. Buka Command Prompt (CMD).
# # 2. Ketik:
# #
# #       python --version
# #
# # 3. Tekan Enter.
# #
# # Jika muncul versi Python, contohnya:
# #
# #       Python 3.13.5
# #
# # berarti Python sudah terinstall dan siap digunakan.
# #
# # Jika muncul pesan seperti:
# #
# #       'python' is not recognized...
# #
# # berarti Python belum terinstall atau belum masuk ke PATH.
# # Python perlu diinstall terlebih dahulu.
# #
# # ============================================================

# # ============================================================
# # STEP 2 — CEK MYSQL CONNECTOR/PYTHON
# # ============================================================
# #
# # Agar Python dapat berkomunikasi dengan database MySQL,
# # kita membutuhkan MySQL Connector/Python.
# #
# # Sebelum melakukan instalasi, kita cek terlebih dahulu
# # apakah MySQL Connector/Python sudah tersedia di komputer.
# #
# # Pengecekan dilakukan melalui Command Prompt (CMD) dengan:
# #
# #     pip show mysql-connector-python
# #
# # Jika informasi package muncul, berarti connector sudah
# # terinstall dan tidak perlu melakukan instalasi ulang.
# #
# # Jika package tidak ditemukan, lakukan instalasi dengan:
# #
# #     pip install mysql-connector-python
# #
# # Setelah itu, package diuji melalui Python.
# #
# # ============================================================


# # ============================================================
# # STEP 3 — MEMBUAT FOLDER PROJECT DI VS CODE
# # ============================================================
# #
# # Setelah memastikan Python dan MySQL Connector/Python tersedia,
# # kita membuat folder khusus untuk project agar seluruh file
# # yang berkaitan dengan pipeline tersimpan secara terorganisir.
# #
# # Folder project yang digunakan:
# #
# #     sql_bi_pipeline
# #
# # Folder ini nantinya akan menjadi tempat untuk menyimpan:
# #
# # - Python script
# # - file konfigurasi yang diperlukan
# # - dokumentasi project
# # - file pendukung lainnya
# #
# # VS Code digunakan sebagai code editor sekaligus tempat
# # untuk menjalankan dan menguji Python script.
# #

# # 1. Buat folder:
# #    sql_bi_pipeline

# # 2. Buka VS Code

# # 3. Pilih:
# #    File → Open Folder

# # 4. Pilih folder:
# #    sql_bi_pipeline

# # 5. Buat file:
# #    test_mysql.py
# # ============================================================


# # ============================================================
# # STEP 4 — TEST MYSQL CONNECTOR
# # ============================================================
# #
# # Setelah memastikan MySQL Connector/Python sudah terinstall,
# # kita perlu melakukan test untuk memastikan Python dapat
# # menemukan dan menggunakan library tersebut.
# #
# # Pada tahap ini kita belum melakukan koneksi ke database MySQL.
# # Kita hanya memastikan bahwa connector berhasil di-import
# # oleh Python.
# #
# # Cara melakukan test:
# # Kita import mysql.connector kemudian menampilkan pesan
# # jika proses import berhasil.
# #
# # ============================================================

# import mysql.connector

# print("MySQL Connector berhasil di-import oleh Python")

# # ============================================================
# # STEP 5 — MEMBUAT KONEKSI KE DATABASE
# # ============================================================
# #
# # Setelah MySQL Connector berhasil di-import, sekarang kita
# # melakukan koneksi langsung dari Python ke database MySQL.
# #
# # Tujuan:
# # Memastikan Python dapat berkomunikasi dengan database MySQL
# # menggunakan konfigurasi koneksi yang benar.
# #
# # Informasi database:
# #
# #     Host     : localhost
# #     Port     : 3306
# #     Database : sql_case_study
# #     User     : root
# #
# # Jika koneksi berhasil, Python akan menampilkan pesan
# # "MySQL berhasil terhubung".
# #
# # ============================================================

# db = mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     database="sql_case_study",
#     user="root",
#     password="root"
# )

# print("MySQL berhasil terhubung")

# # ============================================================
# # STEP 6 — MEMBUAT CURSOR MYSQL
# # ============================================================
# #
# # Setelah Python berhasil terhubung ke database MySQL,
# # kita membutuhkan cursor untuk berkomunikasi dengan database.
# #
# # Analogi sederhananya:
# #
# #     mysql.connector.connect()
# #     = telepon berhasil tersambung 📞
# #
# #     cursor
# #     = alat untuk berbicara dengan database
# #
# # Cursor digunakan untuk mengirimkan perintah SQL kepada
# # database dan mengambil hasil dari perintah tersebut.
# #
# # Pada tahap ini kita baru membuat cursor.
# # Kita belum menjalankan query SQL.
# #
# # ============================================================

# cursor = db.cursor()

# print("Cursor MySQL berhasil dibuat")

# # ============================================================
# # STEP 8 — MENJALANKAN QUERY MYSQL DENGAN EXECUTE()
# # ============================================================
# #
# # Setelah cursor berhasil dibuat, kita dapat mengirimkan
# # perintah SQL kepada database menggunakan:
# #
# #     cursor.execute()
# #
# # Pada tahap ini kita meminta MySQL untuk mengambil seluruh
# # data dari view_summary_master.
# #
# # Analogi:
# #
# #     cursor.execute()
# #     = kita memberikan pesanan kepada dapur 🍜
# #
# # MySQL akan menjalankan query tersebut dan menyiapkan
# # hasilnya untuk kita ambil pada langkah berikutnya.
# # Tapi ingat: execute() belum berarti data sudah masuk ke variabel Python.
# # Saat ini MySQL baru:
# # "Oke, pesanan diterima. Datanya sudah aku siapkan." 😂
# # ============================================================

# cursor.execute("""
#     SELECT *
#     FROM view_summary_master
# """)

# print("Query berhasil dijalankan")


# # ============================================================
# # STEP 9 — MENGAMBIL DATA DENGAN FETCHALL()
# # ============================================================
# #
# # Setelah query dijalankan menggunakan cursor.execute(),
# # MySQL sudah menyiapkan hasil dari query tersebut.
# #
# # Sekarang kita mengambil seluruh hasil query ke dalam Python
# # menggunakan:
# #
# #     cursor.fetchall()
# #
# # Hasilnya disimpan ke dalam variable "rows".
# #
# # Analogi:
# #
# #     execute()
# #     = dapur menerima dan menyiapkan pesanan 🍜
# #
# #     fetchall()
# #     = makanan yang sudah jadi dikirim ke Python 🚚
# #
# # ============================================================

# rows = cursor.fetchall()

# print("Data berhasil diambil dari MySQL")
# print("Jumlah baris:", len(rows))

# # ============================================================
# # STEP 10 — MEMBACA NAMA KOLOM / HEADER
# # ============================================================
# #
# # Setelah data berhasil diambil dari MySQL menggunakan
# # cursor.fetchall(), kita perlu mengetahui struktur kolom
# # dari hasil query.
# #
# # Informasi nama kolom dapat diperoleh dari:
# #
# #     cursor.description
# #
# # Kemudian nama kolom diambil dari setiap informasi kolom
# # dan disimpan ke dalam variable "headers".
# #
# # Variable:
# #
# #     columns → informasi mengenai kolom hasil query
# #     headers → nama kolom/header saja
# #
# # Header ini nantinya akan digunakan sebagai baris pertama
# # ketika data dikirim ke Google Sheets.
# #
# # ============================================================

# columns = cursor.description
# headers = [column[0] for column in columns]

# print("Nama kolom berhasil dibaca:")
# print(headers)

# # ============================================================
# # CONNECT PYTHON DENGAN GSHEET
# # ============================================================

# # ============================================================
# # STEP 11 — PERSIAPAN GOOGLE CLOUD & CREDENTIAL JSON
# # ============================================================
# #
# # Agar Python dapat mengakses Google Sheets secara otomatis,
# # kita membutuhkan autentikasi dari Google Cloud.
# #
# # Pada tahap ini kita melakukan persiapan:
# #
# # 1. Membuat / memilih Google Cloud Project.
# #
# # 2. Mengaktifkan API yang diperlukan untuk komunikasi
# #    dengan Google Sheets dan Google Drive.
# #
# # 3. Membuat Service Account sebagai identitas yang akan
# #    digunakan oleh Python untuk mengakses Google Sheets.
# #
# # 4. Membuat credential berupa file JSON dari Service Account.
# #
# # File JSON ini nantinya akan digunakan oleh Python untuk
# # melakukan authentication.
# #
# # Contoh nama file:
# #
# #     service_account.json
# #
# # File credential ini bersifat RAHASIA.
# # Jangan upload file JSON tersebut ke GitHub karena di dalamnya
# # terdapat credential untuk Service Account.
# #
# # ============================================================

# # ============================================================
# # STEP 12 — PERSIAPAN GOOGLE CLOUD & SERVICE ACCOUNT
# # ============================================================
# #
# # TUJUAN
# # ------------------------------------------------------------
# # Pada tahap ini kita menyiapkan autentikasi Google agar
# # Python nantinya dapat berkomunikasi dengan Google Sheets.
# #
# # Kita akan membuat Service Account dan credential berupa
# # file JSON yang nantinya akan dibaca oleh Python.
# #
# #
# # PROSES
# # ------------------------------------------------------------
# #
# # 1. Buka Google Cloud Console.
# #
# # 2. Login menggunakan akun Google.
# #
# # 3. Buat Google Cloud Project baru.
# #
# #    Contoh nama project:
# #
# #        sql-bi-pipeline
# #
# # 4. Setelah project dibuat, pastikan project tersebut
# #    menjadi project yang sedang aktif.
# #
# #
# # ------------------------------------------------------------
# # AKTIFKAN GOOGLE SHEETS API
# # ------------------------------------------------------------
# #
# # 5. Masuk ke:
# #
# #        APIs & Services → Library
# #
# # 6. Cari:
# #
# #        Google Sheets API
# #
# # 7. Buka Google Sheets API kemudian klik:
# #
# #        Enable
# #
# #
# # ------------------------------------------------------------
# # AKTIFKAN GOOGLE DRIVE API
# # ------------------------------------------------------------
# #
# # 8. Kembali ke API Library.
# #
# # 9. Cari:
# #
# #        Google Drive API
# #
# # 10. Buka Google Drive API kemudian klik:
# #
# #        Enable
# #
# # Google Drive API diperlukan karena library yang digunakan
# # nantinya dapat menggunakan Google Drive untuk mencari dan
# # membuka spreadsheet.
# #
# #
# # ------------------------------------------------------------
# # BUAT SERVICE ACCOUNT
# # ------------------------------------------------------------
# #
# # 11. Masuk ke:
# #
# #        IAM & Admin → Service Accounts
# #
# # 12. Klik:
# #
# #        Create Service Account
# #
# # 13. Berikan nama Service Account.
# #
# #     Contoh:
# #
# #        sql-bi-pipeline
# #
# # 14. Klik Create and Continue.
# #
# # 15. Setelah Service Account berhasil dibuat, akan muncul
# #     email Service Account.
# #
# #     Contoh:
# #
# #        sql-bi-pipeline@sales-bnetfit.iam.gserviceaccount.com
# #
# #
# # ------------------------------------------------------------
# # BUAT JSON KEY
# # ------------------------------------------------------------
# #
# # 16. Klik Service Account yang sudah dibuat.
# #
# # 17. Masuk ke tab:
# #
# #        Keys
# #
# # 18. Klik:
# #
# #        Add Key → Create new key
# #
# # 19. Pilih:
# #
# #        JSON
# #
# # 20. Klik Create.
# #
# # Google akan mendownload file credential JSON.
# #
# #
# # ------------------------------------------------------------
# # SIMPAN FILE JSON KE PROJECT
# # ------------------------------------------------------------
# #
# # 21. Rename file JSON menjadi:
# #
# #        service_account.json
# #
# # 22. Simpan file tersebut di dalam folder project VS Code.
# #
# # Struktur folder menjadi:
# #
# #        sql_bi_pipeline/
# #        │
# #        ├── test_mysql.py
# #        └── service_account.json
# #
# #
# # ------------------------------------------------------------
# # KEAMANAN
# # ------------------------------------------------------------
# #
# # service_account.json merupakan credential rahasia.
# #
# # File tersebut:
# #
# # - Jangan dibagikan kepada orang lain.
# # - Jangan dikirim ke publik.
# # - Jangan di-upload ke GitHub.
# #
# # Pada tahap dokumentasi GitHub nanti, file ini akan
# # dimasukkan ke .gitignore agar tidak ikut ter-upload.
# #
# #
# # ============================================================
# # HASIL STEP 12
# # ============================================================
# #
# # Google Cloud Project       → BERHASIL
# # Google Sheets API          → AKTIF
# # Google Drive API           → AKTIF
# # Service Account            → BERHASIL
# # JSON Key                   → BERHASIL
# # service_account.json       → TERSIMPAN
# #
# # STEP 12 — DONE
# # ============================================================

# # ============================================================
# # STEP 13 — GOOGLE AUTHENTICATION
# # ============================================================
# #
# # Setelah credential JSON berhasil dibuat dan disimpan di
# # dalam folder project, sekarang Python akan membaca file
# # tersebut untuk melakukan authentication ke Google.
# #
# # File yang digunakan:
# #
# #     service_account.json
# #
# # Pada tahap ini kita baru melakukan authentication.
# # Kita belum membuka spreadsheet.
# #
# # ============================================================

# import gspread

# from google.oauth2.service_account import Credentials


# credentials = Credentials.from_service_account_file(
#     "service_account.json",
#     scopes=[
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive"
#     ]
# )

# print("Google authentication berhasil")
# print("SERVICE ACCOUNT:", credentials.service_account_email)

# # ============================================================
# # STEP 14 — AUTHORIZE GOOGLE SHEETS DENGAN GSPREAD
# # ============================================================
# #
# # Pada Step 13, Python berhasil membaca file
# # service_account.json dan membuat credentials.
# #
# # Sekarang credentials tersebut diberikan kepada gspread
# # menggunakan:
# #
# #     gspread.authorize()
# #
# # Tujuannya agar library gspread dapat menggunakan
# # credential tersebut untuk berkomunikasi dengan Google Sheets.
# #
# # Pada tahap ini kita belum membuka spreadsheet tertentu.
# # Kita baru membuat koneksi/authentication antara Python
# # dan layanan Google Sheets melalui gspread.
# #
# # ============================================================

# gc = gspread.authorize(credentials)

# print("gspread berhasil melakukan authorization")


# # ============================================================
# # STEP 15 — MEMBUKA GOOGLE SPREADSHEET
# # ============================================================
# #
# # Setelah gspread berhasil melakukan authorization, sekarang
# # kita mencoba membuka spreadsheet yang akan digunakan sebagai
# # tujuan pengiriman data dari MySQL.
# #
# # Nama spreadsheet:
# #
# #     BNETFIT MASTER DATA
# #
# # Spreadsheet dibuka berdasarkan nama menggunakan:
# #
# #     gc.open()
# #
# # Pada tahap ini kita belum memilih worksheet/tab tertentu.
# # Kita baru memastikan bahwa Python dapat menemukan dan
# # membuka spreadsheet tersebut.
# #
# # ============================================================

# sheet = gc.open("BNETFIT MASTER DATA")

# print("Spreadsheet berhasil dibuka")

# # ============================================================
# # STEP 16 — MEMBUKA WORKSHEET / TAB
# # ============================================================
# #
# # Setelah spreadsheet berhasil dibuka, kita memilih worksheet
# # atau tab tertentu yang akan digunakan sebagai tujuan data.
# #
# # Nama worksheet yang digunakan:
# #
# #     SUMMARY MASTER
# #
# # Worksheet dibuka menggunakan:
# #
# #     sheet.worksheet()
# #
# # Pada tahap ini kita belum menulis data.
# # Kita hanya memastikan bahwa Python dapat menemukan dan
# # membuka worksheet yang sudah dibuat di dalam spreadsheet.
# #
# # ============================================================

# worksheet = sheet.worksheet("SUMMARY MASTER")

# print("Worksheet berhasil dibuka")


# # ============================================================
# # STEP 17 — TEST WRITE KE GOOGLE SHEETS
# # ============================================================
# #
# # TUJUAN
# # ------------------------------------------------------------
# # Setelah Python berhasil:
# #
# # - melakukan authentication ke Google
# # - melakukan authorization dengan gspread
# # - membuka spreadsheet
# # - membuka worksheet
# #
# # sekarang kita perlu memastikan bahwa Python tidak hanya
# # bisa MEMBACA / MEMBUKA Google Sheets, tetapi juga memiliki
# # izin untuk MENULIS data ke dalam worksheet.
# #
# # Sebelum mengirim seluruh data dari MySQL, kita melakukan
# # test terlebih dahulu dengan data sederhana.
# #
# #
# # ============================================================
# # TEST DATA
# # ============================================================
# #
# # Kita akan menulis:
# #
# #     TEST PYTHON
# #
# # ke cell:
# #
# #     A1
# #
# # Jika tulisan tersebut muncul di worksheet, berarti proses
# # Python → Google Sheets untuk WRITE sudah berhasil.
# #
# #
# # ============================================================
# # FORMAT DATA
# # ============================================================
# #
# # gspread mengharapkan data yang dikirim ke Google Sheets
# # dalam bentuk list 2 dimensi.
# #
# # Contoh yang benar:
# #
# #     [["TEST PYTHON"]]
# #
# # Bukan:
# #
# #     "TEST PYTHON"
# #
# # Kesalahan format ini sebelumnya pernah menyebabkan error:
# #
# #     APIError: [400]: Invalid value at 'data.values'
# #
# # Oleh karena itu, kita menggunakan:
# #
# #     values=[["TEST PYTHON"]]
# #
# # ============================================================
# # SCRIPT TEST
# # ============================================================

# worksheet.update(
#     range_name="A1",
#     values=[["TEST PYTHON"]]
# )

# print("Python berhasil menulis ke Google Sheets")


# # ============================================================
# # HASIL YANG HARUS DICEK
# # ============================================================
# #
# # Setelah script berhasil dijalankan:
# #
# # 1. Buka Google Sheets.
# # 2. Buka worksheet:
# #
# #        SUMMARY MASTER
# #
# # 3. Periksa cell A1.
# #
# # Jika muncul:
# #
# #        TEST PYTHON
# #
# # berarti Python sudah berhasil menulis ke Google Sheets.
# #
# #
# # ============================================================
# # CATATAN
# # ============================================================
# #
# # Data "TEST PYTHON" hanya digunakan untuk pengujian.
# #
# # Setelah test berhasil, data test akan dihapus sebelum
# # kita mengirim data sebenarnya dari MySQL.
# #
# # Jangan langsung mengirim seluruh data sebelum test write
# # berhasil, karena test kecil ini membantu memastikan bahwa
# # masalah koneksi dan permission sudah selesai terlebih dahulu.
# #
# # ============================================================
# # HASIL STEP 17
# # ============================================================
# #
# # Python berhasil menulis TEST PYTHON ke cell A1.
# #
# # STEP 17 — DONE
# # ============================================================


# # ============================================================
# # STEP 18 — MEMBERSIHKAN DATA TEST
# # ============================================================
# #
# # TUJUAN
# # ------------------------------------------------------------
# # Pada Step 17 kita berhasil melakukan test write dengan
# # menulis:
# #
# #     TEST PYTHON
# #
# # ke cell A1.
# #
# # Karena tulisan tersebut hanya digunakan untuk pengujian,
# # sekarang kita membersihkannya sebelum memasukkan data
# # sebenarnya dari MySQL.
# #
# # Proses pembersihan dilakukan menggunakan Python agar kita
# # tidak perlu menghapusnya secara manual dari Google Sheets.
# #
# #
# # ============================================================
# # PROSES
# # ============================================================
# #
# # Kita menggunakan:
# #
# #     worksheet.update()
# #
# # untuk mengosongkan cell A1.
# #
# # Cell A1 akan diisi dengan string kosong:
# #
# #     ""
# #
# # ============================================================

# worksheet.update(
#     range_name="A1",
#     values=[[""]]
# )

# print("Data test berhasil dihapus dari Google Sheets")


# # ============================================================
# # HASIL YANG HARUS DICEK
# # ============================================================
# #
# # Setelah script berhasil:
# #
# # 1. Buka Google Sheets.
# # 2. Buka worksheet:
# #
# #        SUMMARY MASTER
# #
# # 3. Periksa cell A1.
# #
# # Cell A1 seharusnya sudah kosong.
# #
# #
# # ============================================================
# # CATATAN
# # ============================================================
# #
# # Kita melakukan test write dan kemudian membersihkan data
# # test sebelum memasukkan data sebenarnya.
# #
# # Ini merupakan bagian dari proses testing agar data
# # pengujian tidak tercampur dengan data production.
# #
# # ============================================================
# # HASIL STEP 18
# # ============================================================
# #
# # TEST PYTHON berhasil dihapus.
# #
# # Worksheet siap digunakan untuk data sebenarnya.
# #
# # STEP 18 — DONE
# # ============================================================

# # ============================================================
# # STEP 19 — MENYIAPKAN DATA UNTUK GOOGLE SHEETS
# # ============================================================
# #
# # TUJUAN
# # ------------------------------------------------------------
# # Data dari MySQL sudah berhasil diambil menggunakan
# # cursor.fetchall() dan disimpan dalam variable "rows".
# #
# # Kita juga sudah mendapatkan nama kolom dalam variable
# # "headers".
# #
# # Sebelum data dikirim ke Google Sheets, kita perlu memastikan
# # bahwa setiap nilai memiliki format yang dapat diterima oleh
# # Google Sheets API.
# #
# # Hal ini penting karena hasil query MySQL dapat memiliki
# # berbagai tipe data, misalnya:
# #
# #     - string
# #     - integer
# #     - float
# #     - date
# #     - datetime
# #     - Decimal
# #
# # Beberapa tipe data seperti date dan Decimal perlu dikonversi
# # terlebih dahulu.
# #
# #
# # ============================================================
# # ERROR YANG PERNAH TERJADI
# # ============================================================
# #
# # Sebelumnya kita mendapatkan error:
# #
# #     TypeError: Object of type date is not JSON serializable
# #
# # Artinya object "date" dari MySQL tidak dapat langsung
# # dikirim melalui request JSON ke Google Sheets.
# #
# # Oleh karena itu kita melakukan transformasi tipe data.
# #
# # ============================================================

# from datetime import date, datetime
# from decimal import Decimal


# data = []


# for row in rows:

#     new_row = []

#     for value in row:

#         # Mengubah date / datetime menjadi teks format ISO
#         if isinstance(value, (date, datetime)):

#             new_row.append(value.isoformat())

#         # Mengubah Decimal menjadi float
#         elif isinstance(value, Decimal):

#             new_row.append(float(value))

#         # Tipe data lainnya dibiarkan seperti semula
#         else:

#             new_row.append(value)

#     data.append(new_row)


# print("Data berhasil disiapkan untuk Google Sheets")
# print("Jumlah baris yang siap dikirim:", len(data))

# # ============================================================
# # STEP 20 — MENGIRIM HEADER + DATA KE GOOGLE SHEETS
# # ============================================================
# #
# # TUJUAN
# # ------------------------------------------------------------
# # Pada Step 19, data dari MySQL sudah berhasil disiapkan
# # dan dikonversi ke format yang dapat dikirim ke Google Sheets.
# #
# # Sekarang kita menggabungkan:
# #
# #     headers
# #     +
# #     data
# #
# # kemudian mengirimkannya ke worksheet SUMMARY MASTER.
# #
# # Header akan menjadi baris pertama, sedangkan data akan
# # ditempatkan mulai dari baris kedua.
# #
# # ============================================================

# all_data = [headers] + data


# # ============================================================
# # MENGIRIM DATA KE GOOGLE SHEETS
# # ============================================================

# worksheet.update(
#     range_name="A1",
#     values=all_data
# )

# print("Data berhasil dikirim ke Google Sheets")


# # ============================================================
# # STEP 21 — MENUTUP CURSOR DAN KONEKSI MYSQL
# # ============================================================
# #
# # TUJUAN
# # ------------------------------------------------------------
# # Setelah seluruh data berhasil diambil dari MySQL,
# # diproses oleh Python, dan dikirim ke Google Sheets,
# # koneksi database sudah tidak diperlukan lagi.
# #
# # Oleh karena itu kita menutup:
# #
# #     1. Cursor
# #     2. Koneksi database
# #
# # Menutup koneksi setelah selesai digunakan merupakan praktik
# # yang baik agar resource database tidak terus terbuka.
# #
# # Analogi:
# #
# #     connect() → telepon tersambung 📞
# #     cursor    → alat untuk berbicara
# #     execute() → memberikan perintah
# #     fetchall() → menerima data
# #     update()  → mengirim data ke Google Sheets
# #     close()   → menutup telepon 📞
# #
# # ============================================================

# cursor.close()

# print("Cursor MySQL ditutup")


# db.close()

# print("Koneksi MySQL ditutup")

