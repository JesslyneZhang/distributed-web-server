# Distributed Web Server Menggunakan Docker dan Nginx Load Balancer

## 1. Deskripsi Project

Project ini merupakan implementasi **Distributed Web Server** menggunakan Docker dan Nginx Load Balancer pada Ubuntu Server Virtual Machine.

Sistem dirancang dengan menggunakan dua backend server berbasis Python Flask yang berjalan dalam container Docker. Kedua backend tersebut dihubungkan dengan Nginx sebagai load balancer untuk mendistribusikan request dari pengguna.

Selain itu, kedua backend menggunakan satu MySQL database yang sama sehingga data yang disimpan melalui salah satu backend dapat diakses melalui backend lainnya.

Project ini dibuat untuk mempelajari konsep distribusi beban server, containerization, database sharing, serta high availability melalui mekanisme failover sederhana.

## 2. Tujuan Project

1. Mengimplementasikan web server terdistribusi menggunakan Docker.
2. Menerapkan Nginx sebagai load balancer untuk mendistribusikan request ke beberapa backend.
3. Mengimplementasikan dua backend server menggunakan Python Flask.
4. Menghubungkan beberapa backend ke satu database MySQL.
5. Menguji mekanisme failover ketika salah satu backend mengalami kegagalan.
6. Memahami proses deployment dan pengelolaan layanan menggunakan Docker Compose.

## 3. Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Ubuntu Server 24.04 LTS | Sistem operasi server |
| VirtualBox | Virtualisasi server |
| Docker Engine | Menjalankan aplikasi dalam container |
| Docker Compose | Mengelola beberapa container |
| Python Flask | Framework backend web |
| Gunicorn | WSGI HTTP server untuk Flask |
| Nginx | Reverse proxy dan load balancer |
| MySQL | Database bersama |
| HTML & CSS | Tampilan antarmuka aplikasi |
| GitHub | Kolaborasi dan pengelolaan source code |

## 4. Arsitektur Sistem

Sistem terdiri dari empat layanan utama:

1. **Nginx Load Balancer**
   - Menerima request dari pengguna.
   - Mendistribusikan request ke backend server.
   - Meneruskan request ke backend yang tersedia.

2. **Backend Server 1**
   - Menjalankan aplikasi Flask.
   - Menangani request dari pengguna.
   - Terhubung ke MySQL database.

3. **Backend Server 2**
   - Menjalankan aplikasi Flask yang sama dengan Backend 1.
   - Menangani request dari pengguna.
   - Terhubung ke MySQL database yang sama.

4. **MySQL Database**
   - Menyimpan data aplikasi.
   - Digunakan bersama oleh Backend 1 dan Backend 2.

### Alur Sistem

Browser Pengguna → Nginx Load Balancer → Backend Server 1 / Backend Server 2 → MySQL Database.

## 5. Fitur Aplikasi

Aplikasi yang dikembangkan adalah **Distributed Server Monitor**, dengan fitur:

- Menampilkan identitas backend server yang menangani request.
- Menampilkan status backend server.
- Menampilkan status koneksi database.
- Menambahkan pesan ke database.
- Menampilkan daftar pesan yang tersimpan.
- Memperlihatkan penggunaan backend secara bergantian melalui load balancing.

## 6. Struktur Folder Project

```text
distributed-web-server/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   └── templates/
│       └── index.html
│
├── database/
│   └── init.sql
│
├── nginx/
│   └── nginx.conf
│
├── docker-compose.yml
│
├── README.md
│
└── docs/
    ├── architecture.png
    └── screenshots/
```

## 7. Pembagian Tugas Anggota

| Anggota | Tanggung Jawab |
|---|---|
| Anggota 1 [Erin] | Persiapan Ubuntu Server VM, instalasi Docker dan Docker Compose, integrasi sistem, serta pengujian akhir |
| Anggota 2 [Jesslyne] | Pengembangan aplikasi Flask, tampilan web, fitur tambah dan tampil data, serta backend Dockerfile |
| Anggota 3 [Sheira] | Perancangan MySQL database, pembuatan init.sql, konfigurasi Nginx, Docker Compose, dan pengujian load balancing serta failover |

## 8. Persyaratan Sistem

Sebelum menjalankan project, pastikan perangkat telah memiliki:

- VirtualBox (untuk menjalankan Ubuntu Server VM).
- Ubuntu Server 24.04 LTS.
- Docker Engine.
- Docker Compose Plugin.
- Git.

Untuk pengembangan lokal, Docker Desktop dapat digunakan pada macOS atau Windows.

## Git Workflow & Collaboration

Untuk menjaga agar pengerjaan project tetap terorganisir dan menghindari konflik kode, setiap anggota kelompok wajib mengerjakan tugas pada branch masing-masing.

**Jangan melakukan perubahan atau push langsung ke branch `main`.**

### 1. Clone Repository

Setiap anggota harus melakukan clone repository terlebih dahulu:

```bash
git clone https://github.com/username/distributed-web-server.git
```

Masuk ke folder project:

```bash
cd distributed-web-server
```

### 2. Pastikan Branch Main Terbaru

Sebelum mulai mengerjakan tugas, pastikan repository lokal sudah mendapatkan perubahan terbaru:

```bash
git switch main
git pull origin main
```

### 3. Buat Branch Masing-Masing

Setiap anggota membuat branch sesuai dengan tanggung jawabnya.

**Anggota 1 — VM dan Integrasi Docker**

```bash
git switch -c feature/vm-integration
```

**Anggota 2 — Flask Backend dan Web Application**

```bash
git switch -c feature/backend-app
```

**Anggota 3 — Database, Nginx, dan Docker Compose**

```bash
git switch -c feature/database-nginx
```

Setelah branch berhasil dibuat, seluruh perubahan yang dilakukan akan tersimpan pada branch tersebut.

### 4. Simpan dan Upload Perubahan

Setelah selesai mengerjakan fitur, jalankan:

```bash
git status
```

Tambahkan perubahan:

```bash
git add .
```

Buat commit:

```bash
git commit -m "Describe your changes"
```

Upload branch ke GitHub:

```bash
git push -u origin NAMA_BRANCH
```

Contoh untuk Anggota 2:

```bash
git push -u origin feature/backend-app
```

### 5. Menggabungkan Branch ke Main

Setelah perubahan selesai di-upload:

1. Buka repository GitHub.
2. Pilih menu **Pull requests**.
3. Klik **New pull request**.
4. Atur base branch menjadi `main`.
5. Pilih compare branch sesuai branch anggota.
6. Periksa perubahan kode.
7. Klik **Create pull request**.
8. Anggota lain melakukan review.
9. Jika sudah disetujui, klik **Merge pull request**.

Setelah berhasil di-merge, perubahan akan masuk ke branch `main`.

### 6. Memperbarui Project Setelah Merge

Sebelum mulai mengerjakan tugas berikutnya, setiap anggota harus memperbarui branch main lokal:

```bash
git switch main
git pull origin main
```

Jika ingin mengerjakan tugas baru, buat branch baru dari `main` terbaru.

### 7. Aturan Kolaborasi

- Setiap anggota wajib bekerja pada branch masing-masing.
- Jangan melakukan push langsung ke `main`.
- Gunakan commit message yang jelas dan sesuai perubahan.
- Lakukan pull sebelum memulai pekerjaan baru.
- Gunakan Pull Request untuk menggabungkan pekerjaan.
- Jangan mengunggah file rahasia seperti `.env`, password, atau credential.
- Jika terjadi konflik Git, selesaikan konflik terlebih dahulu sebelum melakukan merge.

**Tujuan workflow ini:** memastikan setiap fitur dapat dikembangkan secara terpisah, diperiksa bersama, dan digabungkan dengan aman ke dalam project utama.

## 10. Skenario Pengujian

### A. Pengujian Load Balancing

- Jalankan seluruh container.
- Akses aplikasi melalui Nginx.
- Kirim beberapa request secara berulang.
- Amati identitas backend yang menangani setiap request.
- Pastikan request dapat didistribusikan ke kedua backend.

### B. Pengujian Database Sharing

- Tambahkan pesan melalui aplikasi.
- Periksa apakah pesan tersimpan di MySQL.
- Akses aplikasi melalui backend lainnya.
- Pastikan pesan yang sama tetap dapat ditampilkan.

### C. Pengujian Failover

- Jalankan seluruh container.
- Hentikan salah satu backend.
- Kirim request melalui Nginx.
- Pastikan aplikasi tetap dapat diakses melalui backend yang masih berjalan.
- Jalankan kembali backend yang dihentikan.

## 11. Hasil yang Diharapkan

Melalui implementasi ini, diharapkan:

1. Nginx mampu mendistribusikan request ke dua backend server.
2. Kedua backend dapat berkomunikasi dengan satu MySQL database.
3. Data tetap konsisten dan dapat diakses dari kedua backend.
4. Aplikasi tetap dapat diakses ketika salah satu backend dihentikan.
5. Seluruh layanan dapat dijalankan dan dikelola menggunakan Docker Compose.

## 12. Status Pengembangan

Project dikembangkan secara kolaboratif oleh tiga anggota kelompok.

Fitur dan konfigurasi yang telah selesai akan terus diintegrasikan dan diuji hingga seluruh komponen dapat berjalan sebagai satu sistem terdistribusi.

## 13. Kontributor

- Anggota 1 — Infrastruktur dan integrasi server.
- Anggota 2 — Backend Flask dan antarmuka aplikasi.
- Anggota 3 — Database MySQL dan konfigurasi Nginx.

---

**Project:** Distributed Web Server Using Docker and Nginx Load Balancer  
**Mata Kuliah:** Manajemen Jaringan dan Server
