# **Inventory Management System (IMS)**

## **Deskripsi Program**

Inventory Management System (IMS) adalah sebuah aplikasi berbasis Python yang dirancang untuk membantu pengguna dalam mengelola inventaris barang secara efisien. Aplikasi ini menyediakan fitur lengkap seperti menambahkan, menghapus, memperbarui, dan menampilkan data stok barang. Dengan antarmuka berbasis teks yang intuitif, IMS sangat cocok digunakan oleh individu atau bisnis kecil yang ingin menjaga kontrol atas inventaris mereka.

---

## **Fitur Utama**

1. **Menampilkan Stok Barang**
   - **Tampilkan Semua Stok**: Lihat seluruh daftar stok barang yang tersedia di database.
   - **Tampilkan Bahan Tertentu**: Cari dan tampilkan detail spesifik dari suatu barang berdasarkan ID-nya.
   - **Tampilkan Berdasarkan Kategori**: Filter dan tampilkan barang-barang berdasarkan kategori tertentu (misalnya: Ayam, Minuman, dll.).
   - **Pengurutan Data**: Urutkan stok barang berdasarkan kolom tertentu (No, Nama, Stok, Harga, dll.) dalam urutan Ascending (ASC) atau Descending (DESC).

2. **Menambahkan Stok Barang**
   - Tambahkan barang baru ke dalam database dengan informasi seperti nama, jumlah stok, kategori, dan harga per unit.
   - Validasi input dilakukan untuk memastikan bahwa data yang dimasukkan benar dan tidak ada duplikasi.

3. **Menghapus Stok Barang**
   - Hapus barang dari database berdasarkan ID unik.
   - Konfirmasi sebelum penghapusan untuk mencegah kesalahan.

4. **Memperbarui Data Stok**
   - Ubah informasi barang yang sudah ada seperti nama, jumlah stok, kategori, atau harga.
   - Validasi input dilakukan untuk memastikan integritas data.

5. **Keluar dari Program**
   - Keluar dari aplikasi dengan aman setelah selesai melakukan operasi.

---

## **Cara Menggunakan Program**

### **Prasyarat**
- Pastikan Anda memiliki Python versi 3.x terinstal di sistem Anda.
- Instal modul `tabulate` dengan menjalankan perintah berikut:
  ```bash
  pip install tabulate
  ```

### **Langkah-langkah Penggunaan**

1. **Jalankan Program**  
   Jalankan file Python menggunakan terminal atau command prompt:
   ```bash
   python nama_file.py
   ```

2. **Menu Utama**  
   Setelah program dijalankan, Anda akan disambut dengan menu utama yang menawarkan pilihan berikut:
   ```
   =============================
   Selamat Datang di Inventory Management System
   =============================
   List Aksi:
   1. Menampilkan Stok
   2. Menambah Daftar Stok
   3. Menghapus Stok
   4. Mengubah Data Stok
   5. Exit Program
   Masukkan angka yang ingin dijalankan :
   ```

3. **Navigasi Menu**
   - Pilih nomor yang sesuai dengan aksi yang ingin Anda lakukan.
   - Ikuti instruksi yang diberikan di layar untuk menyelesaikan tugas.

---

## **Contoh Penggunaan**

### **1. Menampilkan Stok**
Setelah memilih opsi "1. Menampilkan Stok", Anda dapat melihat semua barang yang tersedia dalam format tabel yang rapi:
```
+----+-------+---------------+------+---------+------------------+-------------+
| No |  Id   |      Nama     | Stok | Kategori| Harga Per Stok   | Harga Total |
+----+-------+---------------+------+---------+------------------+-------------+
| 1  | ID001 | Ayam Boiler   | 20   | Ayam    | 10000            | 200000      |
| 2  | ID002 | Tahu Bacem    | 15   | Tahu    | 15000            | 225000      |
| 3  | ID003 | Kelapa Muda   | 25   | Minuman | 20000            | 500000      |
| 4  | ID004 | Ayam Kampung  | 20   | Ayam    | 10000            | 200000      |
+----+-------+---------------+------+---------+------------------+-------------+
```

Anda juga dapat mengurutkan data berdasarkan kolom tertentu (misalnya: Stok, Harga, dll.).

---

### **2. Menambahkan Stok**
Untuk menambahkan barang baru, pilih opsi "2. Menambah Daftar Stok". Masukkan informasi yang diperlukan seperti nama, jumlah stok, kategori, dan harga. Contoh:
```
Masukkan Nama Barang: Kentang Goreng
Masukkan Jumlah Stok: 50
Masukkan Kategori: Makanan
Masukkan Harga Per Stok: 8000
```

Barang baru akan ditambahkan ke database.

---

### **3. Menghapus Stok**
Untuk menghapus barang, pilih opsi "3. Menghapus Stok". Masukkan ID barang yang ingin dihapus. Contoh:
```
Masukkan ID Stok yang ingin dihapus: ID002
```

Barang dengan ID tersebut akan dihapus dari database setelah konfirmasi.

---

### **4. Memperbarui Data Stok**
Untuk memperbarui informasi barang, pilih opsi "4. Mengubah Data Stok". Masukkan ID barang yang ingin diperbarui dan kolom yang ingin diubah. Contoh:
```
Masukkan ID Stok yang ingin diubah: ID001
Kolom apa yang ingin diubah (Nama, Stok, Kategori, Harga Per Stok): Stok
Nilai 20 ingin diubah jadi apa: 25
```

Data akan diperbarui setelah konfirmasi.

---

## **Keunggulan Program**

- **Antarmuka Sederhana**: Mudah digunakan bahkan untuk pemula.
- **Validasi Input**: Mencegah kesalahan input dengan validasi yang ketat.
- **Tampilan Tabel Rapi**: Menggunakan library `tabulate` untuk menampilkan data dalam format tabel yang mudah dibaca.
- **Fleksibilitas**: Mendukung berbagai operasi CRUD (Create, Read, Update, Delete) untuk manajemen inventaris.

---

## **Kontak Pengembang**

Jika Anda memiliki pertanyaan, saran, atau masalah terkait program ini, silakan hubungi kami di:
- Email: [email@example.com](mailto:email@example.com)
- GitHub: [github.com/username](https://github.com/username)

---

## **Lisensi**

Program ini dilisensikan di bawah lisensi MIT. Anda bebas menggunakan, memodifikasi, dan mendistribusikan program ini sesuai dengan ketentuan lisensi.

---

Terima kasih telah menggunakan **Inventory Management System**! Kami harap program ini dapat membantu Anda mengelola inventaris dengan lebih baik. 😊
