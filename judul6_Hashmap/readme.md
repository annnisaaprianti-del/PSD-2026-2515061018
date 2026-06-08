#SISTEM PERPUSTAKAAN MENGGUNAKAN HASHMAP OPEN ADDRASING#
Program ini merupakan simulasi sederhana sistem perpustakaan yang dibuat menggunakan struktur data HashMap Open Addressing dengan Linear Probing. Sistem ini dapat digunakan untuk menyimpan data buku, mencari buku berdasarkan kode, melihat daftar buku yang tersedia, dan melakukan peminjaman buku. Penggunaan HashMap membuat proses pencarian data menjadi lebih cepat karena sistem tidak perlu memeriksa semua data satu per satu.
<img width="626" height="192" alt="image" src="https://github.com/user-attachments/assets/08fdca1d-8916-4027-a9fb-a1462125573f" />
Pada bagian ini dibuat kelas Buku yang berfungsi untuk menyimpan informasi setiap buku yang ada di perpustakaan. Data yang disimpan meliputi kode buku, judul buku, dan status ketersediaan buku.
Saat sebuah buku pertama kali ditambahkan ke sistem, statusnya otomatis bernilai tersedia. Nantinya status tersebut akan berubah ketika buku dipinjam oleh pengguna. Dengan adanya status ini, sistem dapat mengetahui apakah suatu buku masih bisa dipinjam atau sedang dipinjam oleh orang lain.
<img width="590" height="213" alt="image" src="https://github.com/user-attachments/assets/81d3b3d4-2e03-4fcc-b821-21a10d104169" />
kelas Entry digunakan sebagai tempat penyimpanan data di dalam hash table. Setiap slot pada hash table memiliki tiga komponen utama, yaitu key, value, dan state.
Key digunakan untuk menyimpan kode buku, value digunakan untuk menyimpan objek buku, sedangkan state digunakan untuk menandai apakah slot tersebut masih kosong atau sudah terisi data.Bagian ini penting karena hash table bekerja dengan cara menyimpan data pada slot-slot tertentu yang nantinya akan diakses kembali saat proses pencarian dilakukan.
<img width="914" height="663" alt="image" src="https://github.com/user-attachments/assets/2ae338c8-36e1-48d7-aca0-7a3de57a8fb8" />
Ketika objek perpustakaan dibuat, sistem akan menyiapkan sejumlah slot kosong yang nantinya digunakan untuk menyimpan data buku. Pada program ini ukuran hash table ditentukan sebanyak 10 slot.
Secara sederhana, hash table dapat dibayangkan seperti rak penyimpanan yang memiliki beberapa tempat kosong. Setiap buku yang masuk akan ditempatkan pada posisi tertentu sesuai hasil perhitungan fungsi hash.
Fungsi hash digunakan untuk menentukan lokasi penyimpanan suatu buku berdasarkan kode bukunya.
Misalnya terdapat kode buku 101. Sistem akan menghitung:
Fungsi hash digunakan untuk menentukan lokasi penyimpanan suatu buku berdasarkan kode bukunya.
Misalnya terdapat kode buku 101. Sistem akan menghitung:
101 % 10 = 1
Artinya buku tersebut akan disimpan pada indeks ke-1.
Tujuan dari fungsi hash adalah agar sistem dapat langsung mengetahui lokasi penyimpanan data tanpa harus mencari satu per satu dari awal. Hal ini membuat proses pencarian menjadi jauh lebih cepat, terutama jika jumlah data yang disimpan semakin banyak.

Program ini menunjukkan bagaimana struktur data HashMap dapat diterapkan pada sistem perpustakaan sederhana. Dengan menggunakan fungsi hash, data buku dapat disimpan dan dicari dengan lebih cepat. Selain itu, penggunaan metode Linear Probing memungkinkan sistem tetap dapat menyimpan data meskipun terjadi collision. Oleh karena itu, HashMap menjadi salah satu struktur data yang efektif untuk mengelola data yang membutuhkan proses pencarian secara cepat, seperti data buku pada perpustakaan.

Link yt: https://youtu.be/TOmRI9ZBj6M 
