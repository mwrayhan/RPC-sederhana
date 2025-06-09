# RPC Sederhana: Sistem Inventori (Tambah Item) dengan XML-RPC Python

Proyek ini mendemonstrasikan konsep dasar Remote Procedure Call (RPC) menggunakan implementasi XML-RPC standar di Python. Fokus utamanya adalah pengelolaan inventori, di mana sebuah **server** bertindak sebagai "Gudang Inventori" dan sebuah **klien** dapat memanggil fungsi untuk menambahkan item dari jarak jauh.

Tujuan dari proyek ini adalah untuk menunjukkan bagaimana dua program Python yang terpisah dapat berkomunikasi melalui jaringan lokal, memungkinkan klien untuk memanggil fungsi yang didefinisikan di server seolah-olah fungsi tersebut adalah bagian dari kode lokal klien.

---

## Daftar Isi

* [Tentang Proyek](#tentang-proyek)
* [Fitur Utama](#fitur-utama)
* [Teknologi yang Digunakan](#teknologi-yang-digunakan)
* [Struktur Proyek](#struktur-proyek)
* [Cara Menjalankan](#cara-menjalankan)
* [Lisensi](#lisensi)
* [Kontributor](#kontributor)

---

## Tentang Proyek

Sistem ini mensimulasikan skenario di mana sebuah aplikasi klien (misalnya, terminal penerimaan barang) perlu memperbarui inventori pusat yang dikelola oleh aplikasi server.

**Fungsi yang disediakan oleh Layanan (Server):**
* `add_item(name, quantity)`: Fungsi ini menerima nama item (`name`) dan jumlahnya (`quantity`). Jika `quantity` positif, item akan ditambahkan ke inventori dan total stok diperbarui. Jika `quantity` negatif, server akan mengembalikan pesan error. Server akan mengkonfirmasi apakah penambahan berhasil dan berapa total stok item tersebut.

Melalui proyek ini, Anda akan belajar tentang:
* Inisiasi server XML-RPC dan klien.
* Pendaftaran metode di server agar dapat diakses dari jarak jauh.
* Membangun koneksi jaringan antara klien dan server.
* Melakukan panggilan fungsi jarak jauh (RPC call) dari klien.
* Menerima respons (termasuk *error handling* sederhana) dari server.

---

## Fitur Utama

* **Panggilan Fungsi Jarak Jauh (RPC):** Klien dapat memanggil metode `add_item` yang berjalan di server.
* **Manajemen Inventori Dasar:** Server dapat menambah dan melacak jumlah stok item yang berbeda.
* **Validasi Input:** Server memiliki logika dasar untuk menangani input jumlah negatif.
* **Komunikasi Jaringan:** Menggunakan protokol XML-RPC melalui TCP/IP.
* **Sederhana & Mudah Dipahami:** Implementasi minimalis untuk memahami konsep RPC.

---

## Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.x
* **Mekanisme Komunikasi:** Python `xmlrpc.server` (untuk server) dan `xmlrpc.client` (untuk klien)
* **Penyimpanan Inventori (Sisi Server):** Python Dictionary (disimpan dalam memori)

---

## Struktur Proyek

Tentu, dengan kode Python XML-RPC yang Anda berikan, saya akan membuatkan isi file README.md yang lengkap dan sesuai. Ini akan menjelaskan proyek Anda dengan baik kepada siapa pun yang melihat repositori.

Markdown

# RPC Sederhana: Sistem Inventori (Tambah Item) dengan XML-RPC Python

Proyek ini mendemonstrasikan konsep dasar Remote Procedure Call (RPC) menggunakan implementasi XML-RPC standar di Python. Fokus utamanya adalah pengelolaan inventori, di mana sebuah **server** bertindak sebagai "Gudang Inventori" dan sebuah **klien** dapat memanggil fungsi untuk menambahkan item dari jarak jauh.

Tujuan dari proyek ini adalah untuk menunjukkan bagaimana dua program Python yang terpisah dapat berkomunikasi melalui jaringan lokal, memungkinkan klien untuk memanggil fungsi yang didefinisikan di server seolah-olah fungsi tersebut adalah bagian dari kode lokal klien.

---

## Daftar Isi

* [Tentang Proyek](#tentang-proyek)
* [Fitur Utama](#fitur-utama)
* [Teknologi yang Digunakan](#teknologi-yang-digunakan)
* [Struktur Proyek](#struktur-proyek)
* [Cara Menjalankan](#cara-menjalankan)
* [Lisensi](#lisensi)
* [Kontributor](#kontributor)

---

## Tentang Proyek

Sistem ini mensimulasikan skenario di mana sebuah aplikasi klien (misalnya, terminal penerimaan barang) perlu memperbarui inventori pusat yang dikelola oleh aplikasi server.

**Fungsi yang disediakan oleh Layanan (Server):**
* `add_item(name, quantity)`: Fungsi ini menerima nama item (`name`) dan jumlahnya (`quantity`). Jika `quantity` positif, item akan ditambahkan ke inventori dan total stok diperbarui. Jika `quantity` negatif, server akan mengembalikan pesan error. Server akan mengkonfirmasi apakah penambahan berhasil dan berapa total stok item tersebut.

Melalui proyek ini, Anda akan belajar tentang:
* Inisiasi server XML-RPC dan klien.
* Pendaftaran metode di server agar dapat diakses dari jarak jauh.
* Membangun koneksi jaringan antara klien dan server.
* Melakukan panggilan fungsi jarak jauh (RPC call) dari klien.
* Menerima respons (termasuk *error handling* sederhana) dari server.

---

## Fitur Utama

* **Panggilan Fungsi Jarak Jauh (RPC):** Klien dapat memanggil metode `add_item` yang berjalan di server.
* **Manajemen Inventori Dasar:** Server dapat menambah dan melacak jumlah stok item yang berbeda.
* **Validasi Input:** Server memiliki logika dasar untuk menangani input jumlah negatif.
* **Komunikasi Jaringan:** Menggunakan protokol XML-RPC melalui TCP/IP.
* **Sederhana & Mudah Dipahami:** Implementasi minimalis untuk memahami konsep RPC.

---

## Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.x
* **Mekanisme Komunikasi:** Python `xmlrpc.server` (untuk server) dan `xmlrpc.client` (untuk klien)
* **Penyimpanan Inventori (Sisi Server):** Python Dictionary (disimpan dalam memori)

---

## Struktur Proyek

rpc-inventori-sederhana/
├── rpc_add_item_server.py    # Kode utama server
├── rpc_add_item_client.py    # Kode utama klien
└── README.md

## Cara Menjalankan

Ikuti langkah-langkah di bawah ini untuk menjalankan sistem RPC inventori sederhana ini di lingkungan lokal Anda.

**Prasyarat:**

* Python 3.x terinstal di sistem Anda.

**Langkah-langkah:**

1.  **Clone Repositori (jika Anda mendapatkan ini dari Git):**
    ```bash
    git clone [https://github.com/your-username/rpc-inventori-sederhana.git](https://github.com/your-username/rpc-inventori-sederhana.git)
    cd rpc-inventori-sederhana
    ```
    *(Ganti `your-username` dengan username GitHub Anda)*

2.  **Jalankan Server:**
    * Buka Terminal/Command Prompt **pertama**.
    * Navigasi ke direktori proyek `rpc-inventori-sederhana/`.
    * Jalankan server:
        ```bash
        python rpc_add_item_server.py
        ```
    * Anda akan melihat pesan "Server berjalan di port 8000...". **Biarkan terminal ini tetap terbuka dan berjalan.**

3.  **Jalankan Klien:**
    * Buka Terminal/Command Prompt **kedua** (baru).
    * Navigasi ke direktori proyek `rpc-inventori-sederhana/`.
    * Jalankan klien:
        ```bash
        python rpc_add_item_client.py
        ```
    * Klien akan mencoba terhubung ke server, memanggil fungsi `add_item` beberapa kali dengan data contoh, dan menampilkan respons yang diterima dari server di konsol. Anda juga akan melihat output di konsol server setiap kali item ditambahkan.

---

## Lisensi

Proyek ini dilisensikan di bawah [Lisensi MIT](https://opensource.org/licenses/MIT). Anda bebas menggunakan, memodifikasi, dan mendistribusikan kode ini.

---

## Kontributor

* [Raihanul Mawa] - [[Opsional: Profil GitHub Anda atau Link Lain](https://github.com/mwrayhan)]

---
