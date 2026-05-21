===SISTEM SORTIR KANTOR POS (BST)===
sistem ini tentang pendataan surat yang masuk dan akan dikirim, dalam sistem ini user dapat menginputkan data surat, mulai dari kode pos, penerima, dan alamat yang nanti nya akan di bentuk logikan seperti pohon.
<img width="1154" height="697" alt="image" src="https://github.com/user-attachments/assets/ed92961f-445e-403f-a325-96b9efa02fc1" />
baris kode ini menjelaskan tentang awal mula/ definisi awal yang ada dalam koding, serta pada beris ini terdapat fungsi insert yang berguna untuk menambahkan dan mengatur registrasi dari surat masuk.
<img width="844" height="363" alt="image" src="https://github.com/user-attachments/assets/1cbdf9df-ada3-4d0d-93f7-0b576c7e5499" />
fungsi search ini berguna untuk mencari surat dengan kata kunci dari kode pos, fungsi ini menggunakan rekursi dalam proses pencariannya yaitu dia bekerja dengan memanggil dirinya sendiri, dalam fungsi ini terdapat 4 kondisi yaitu, kondisi pertama ketika root tersebut dalam keadaan kosong, maka program tidak akan berjalan,karena berarti belum ada data yang masuk,yang ke-2 yaitu ketika surat dengan kode pos yang dicari == kode pos surat yang menjadi root, maka search akan langsung mecetak informasi yang dimiliki root. kondisi yang ke-3 yaitu ketika yaitu ketika kode pos yang dicari lebih kecil dari root maka pencarian akan dilanjutkan ke cabang kiri sampai ujung. dan yang terakhir kondisi ke 4 ketika lebih besar dari root maka akan langsung diarahkan pencarian di cabang sebelah kanan sampai ujung.
<img width="1192" height="592" alt="image" src="https://github.com/user-attachments/assets/3682fc2c-4632-47e9-ba5c-8394dba42922" />
ketiga fungsi ini adalah pencetakan yang dilakukan tree, inorder akan melakukan pencetakan dengan mencetak data registrasi yang ada di sebelah kiri, setelah itu akan mencetak root nya dan beralih ke sebelah kanan, untuk preorder pencetakan mendahulukan root setelah itu kedata sebelah kiri lalu kanan, dan sedangkan untuk post order pencetakan dilakukan dengan mencetak data sebelah kiri, lalu kanan dan terakhir akan mencetak rootnya.
<img width="556" height="462" alt="image" src="https://github.com/user-attachments/assets/6f741a26-10f1-4df2-a90c-849ed29207b6" />
mencari nilai min dan max seperti halnya dalam search
<img width="1002" height="285" alt="image" src="https://github.com/user-attachments/assets/0c58f539-6c8e-418c-a5b6-f9d7c0fe315d" />
dan ini untuk menampilkan jumlah surat yang masuk dan jumlah kode pos nya

link yt: https://youtu.be/JyzcGiIYmrY?si=fix6G3oQunN3MBF8
