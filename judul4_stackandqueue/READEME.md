#PLAYLIST FAVORITE ICA#
  kode ini mengimplementasikan daftar lagu kesukaan ica yang di tambahkan setiap hatinya, lagu pertama yang ditambahkan ke daftar adalah lagu pertama yang akan diputar
    <img width="583" height="192" alt="Screenshot 2026-05-11 235202" src="https://github.com/user-attachments/assets/c63b40fd-42f4-436e-b204-257600bd690d" />
pertama saya membuat kelas bagi queue nya terlebih dahulu 
     def __init__(self, max_size=10):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
          kode ini mendeskripsikan ruang jumlah bagi lagu yang masuk, disini saya memasukan hanya akan ada 10 lagu dengan index dari 0-9
self.front_idx = -1
self.rear_idx = -1  kode ini menjelaskan bahwa saat ini array benar-benar dalam keadaan kosong, dan menunjukan bahwa array pada index 0 pun belum terisi.

  <img width="448" height="67" alt="image" src="https://github.com/user-attachments/assets/b5033322-0db6-48c7-9b7e-38540d57cf51" />

  pada fungsi ini memiliki fungsi untuk mengecek apakah queue dalam keadaan kosong, jika benar maka artinya tidak perlu memutar atau membuang sebuah lagu.
  dan jika hasilnya false maka kode akan mereturn "return self.front_idx == -1".

    <img width="815" height="90" alt="image" src="https://github.com/user-attachments/assets/eab7937e-e988-44b4-a373-a6a1967d9f2c" />

    fungsi ini digunakan untuk mengecek, apakah queue dalam keadaan full(penuh)atau masih ada tempat tersisa untuk tambahan lagu berikutnya.
     return (self.rear_idx + 1) % self.MAXN == self.front_idx pada bagian kode ini menunjukan bahwa queue yang di pakai untuk playlist ini yaitu queue cirkular, yang dimana ini 
    untuk mencegah terjadinya index tidak di temukan, ketika melakukan pengecekan, jadi setelah mencapai index 9 pengecekan dilanjutkan bukan ke index 10 melainkan kembali ke index 
    0 sehingg dianalogikan bentuknya melingkar.

      <img width="780" height="346" alt="image" src="https://github.com/user-attachments/assets/d9a49ce5-d7b9-4347-b068-b4a7639d5ba4" />

    fungsi enqueue digunakan untuk menambahkan lagu baru kedalam playlist, pada kode ini sebelum ica dapat menambahkan lagu, kode akan mengecek terlebih dahulu apakah 
    daftar lagu masih bisa menerima lagu baru atau tidak, hal ini dilakukan untuk mencegah terjadinya error overflow.

      <img width="872" height="309" alt="image" src="https://github.com/user-attachments/assets/c3f3d971-ba62-4768-a675-a80014c49666" />

    fungsi dequeue digunakan untuk memutar atau mengurangi lagu yang ada di playlist, setiap lagu yang di denqueue lagu tersebut akan terputar.

      <img width="937" height="193" alt="image" src="https://github.com/user-attachments/assets/7194b9f6-b747-4e5d-b2ac-0d11eccb837e" />

      fungsi peek ini digunakan untuk mengecek lagu yang berada diurutan paling depan tanapa menghapusnya.
      <img width="1045" height="545" alt="image" src="https://github.com/user-attachments/assets/c52901cd-2296-4fcf-b4f7-723f55104b06" />

      pada bagaian ini fungsinya menampilkan daftar lagu yang ada di dalam playlist, dan setiap judul akan dibatasi dengan tana koma

        <img width="881" height="838" alt="image" src="https://github.com/user-attachments/assets/5fd28c9c-bad4-464b-a92a-2890b3d284a2" />

        ini adalah main progaram yaitu kodingan yang akan dijalankan pertama kali, pada bagian ini meminta untuk user menginputkan program mana yang ingin dijalankan

          link youtube: https://youtu.be/FBRRMWmFqc0?si=syTyBwEND3TSawo6








