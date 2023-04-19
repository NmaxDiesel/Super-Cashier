# Super-Cashier-Python



## Background Project 
Terdapat bisnis coffeeshop besar di daerah Jabodetabek, sang owner ingin melakukan ekspansi ke wilayah lain. Owner berniat melakukan inovasi pada bisnisnya dengan membuat sebuah sistem kasir yang bisa beroperasi secara self-service dengan harapan agar customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli serta customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut.

## Tujuan Project
Program ini dibuat dengan tujuan agar konsumen coffeeshop bisa berbelanja secara self service dengan tindakan seperti:

- Costumer dapat membuat ID transaksi mereka masing-masing
- Costumer dapat menginputkan nama item, jumlah item, dan harga barang yang ingin dibeli
- Costumer dapat mengupdate nama item, jumlah item, dan harga barang apabila ada yang ingin mereka ubah
- Costumer dapat memeriksa kembali barang yang ingin mereka checkout
- Program dapat menghitung diskon untuk costumer sesuai ketentuan yang sudah ditetapkan


## Flowchart Project
Berikut meruapkan diagram alir dari program Super Cashier yang dibuat:

![Flowchart Supercashier drawio](https://user-images.githubusercontent.com/123163060/232277631-d960f04f-3b93-4f68-99d2-8e6d7ab7f9e7.png)

## Requirement Project

- add_item(self, name, quantity, price): Metode ini digunakan untuk menambahkan item ke dalam order_list. Jika item dengan name tertentu belum ada dalam order_list, maka item tersebut akan ditambahkan sebagai kunci dalam kamus order_list dengan nilai sebagai sebuah daftar yang berisi quantity dan price sebagai elemen pertama dan kedua. Jika item dengan name tertentu sudah ada dalam order_list, maka quantity dari item tersebut akan diupdate dengan menambahkannya dengan quantity yang baru.

- delete_item(self, name): Metode ini digunakan untuk menghapus item dari order_list berdasarkan name item yang diberikan.

- update_item_name(self, name, update_name): Metode ini digunakan untuk mengganti nama item dalam order_list dari name lama menjadi update_name baru.

- update_item_qty(self, name, update_quantity): Metode ini digunakan untuk mengupdate quantity suatu item dalam order_list berdasarkan name item yang diberikan dengan update_quantity yang baru.

- update_item_price(self, name, update_price): Metode ini digunakan untuk mengupdate price suatu item dalam order_list berdasarkan name item yang diberikan dengan update_price yang baru.

- check_order(self): Metode ini digunakan untuk memeriksa daftar item yang ada dalam order_list. Jika order_list kosong, maka akan dicetak pesan bahwa belum ada item yang dibeli. Jika order_list tidak kosong, maka akan dicetak daftar item yang telah dibeli beserta jumlah, harga per item, dan total harga untuk setiap item, serta mengembalikan total harga dari seluruh item yang ada dalam order_list.

- total_price(self): Metode ini digunakan untuk menghitung total harga dari seluruh item yang ada dalam order_list dengan memanggil metode check_order(). Setelah itu, akan diberikan diskon berdasarkan total harga yang telah dihitung, dan dicetak total belanja yang harus dibayarkan setelah diskon.

- reset_transaction(self): Metode ini digunakan untuk menghapus semua item dalam order_list dan mengembalikan order_list menjadi sebuah kamus kosong.

- main(): Merupakan metode utama yang berfungsi sebagai tampilan antarmuka pengguna dalam bentuk teks untuk berinteraksi dengan objek Transaction. Pengguna dapat memilih berbagai opsi seperti menambahkan, menghapus, mengupdate, atau memeriksa item dalam order_list serta menghitung total harga. Program akan terus berjalan hingga pengguna memilih untuk keluar (memilih opsi 9) dan memunculkan pesan terima kasih.

## Dokumentasi Code

1. Definisikan beberapa metode (fungsi) yang dibutuhkan dalam program transaksi kita.
<img width="1217" alt="Screenshot 2023-04-16 at 18 12 00" src="https://user-images.githubusercontent.com/123163060/232305516-1ccd5555-94fd-4d86-b275-6d40f8485c20.png">

2. Definisikan semua fungsi yang dibutuhkan, mulai dari fungsi add_item hingga yang terakhir.
<img width="1245" alt="Screenshot 2023-04-16 at 18 17 23" src="https://user-images.githubusercontent.com/123163060/232305819-57e1a3ca-082b-47de-87e1-c6e1d5549cb7.png">

3. Masukkan perhitungan diskon terhadap barang yang sudah ditetapkan.
<img width="1672" alt="Screenshot 2023-04-16 at 18 21 32" src="https://user-images.githubusercontent.com/123163060/232306800-443af1df-bd82-4825-86b2-e1ea871a1ae9.png">

4. Fungsi loop dimulai.
<img width="1670" alt="Screenshot 2023-04-16 at 18 23 04" src="https://user-images.githubusercontent.com/123163060/232306796-0b5fd664-73fe-48c1-a74e-ec6a19501af1.png">

5. Program selesai ketika fungsi loop sudah dihentikan oleh konsumen. Terlihat juga apa yang bisa program lakukan apabila ada kesalahan dalam penginputan data oleh konsumen.
<img width="1578" alt="Screenshot 2023-04-16 at 18 25 43" src="https://user-images.githubusercontent.com/123163060/232306760-449a7478-5e53-4558-ba28-376c045a6666.png">

## Hasil Test Case

Berikut merupakan hasil test case program.
1. Contoh kasusnya ialah pembeli ingin membeli Kopi Americano seharga Rp 20.000 sebanyak 2 item

<img width="951" alt="Screenshot 2023-04-16 at 18 51 43" src="https://user-images.githubusercontent.com/123163060/232308099-357d7aac-47ce-47fc-87e8-c7350613a5a2.png">

2. Konsumen ingin menampilkan total harga yang harus ia bayar. Program kemudian menampilkan nilainya.
<img width="1676" alt="Screenshot 2023-04-16 at 18 56 48" src="https://user-images.githubusercontent.com/123163060/232308290-66b791cd-158d-48be-b827-96da3cfcefba.png">

## Conclusion
Program berhasil berfungsi dengan baik. Diketahui berdasarkan kemampuan program dalam memenuhi kebutuhan kebutuhan bisnis sang owner yaitu program sudah dapat membuatkan ID transaksi konsumen, dapat menginputkan nama item, jumlah item, harga barang yang ingin dibeli, dan juga dapat mengupdate elemen dalam pemesanan item konsumen. Program bisa melakukan pemeriksaan kembali dan menghitung diskon untuk costumer sesuai ketentuan yang sudah ditetapkan.

## Future Work
- Integrasi dengan Teknologi Canggih: Mengintegrasikan program kasir dengan teknologi canggih seperti Internet of Things (IoT), kecerdasan buatan (Artificial Intelligence/AI), dan pembelajaran mesin (Machine Learning/ML) untuk meningkatkan efisiensi dan akurasi transaksi. Contohnya, penggunaan sensor RFID untuk mengenali barang secara otomatis, penggunaan chatbot untuk melayani pelanggan, dan analisis data untuk mengidentifikasi tren dan pola pembelian pelanggan.
- Analisis Data dan Pelaporan: Menyediakan fitur analisis data dan pelaporan yang canggih untuk membantu pemilik bisnis dalam mengambil keputusan berdasarkan data. Fitur ini dapat memberikan wawasan tentang performa penjualan, tren pembelian, stok barang, dan kebiasaan pelanggan, sehingga pemilik bisnis dapat membuat strategi yang lebih efektif untuk mengoptimalkan operasional dan meningkatkan keuntungan.Ini dapat dilakukan dengan dukungan tools BI.
- Meningkatkan keamanan data dalam program kasir dengan mengimplementasikan langkah-langkah keamanan yang kuat, seperti enkripsi data, autentikasi pengguna, dan proteksi terhadap ancaman keamanan siber. Selain itu, penting untuk mematuhi peraturan perlindungan data yang berlaku, seperti General Data Protection Regulation (GDPR) untuk menjaga kerahasiaan dan privasi data pelanggan.
- Integrasi dengan platform e-commerce. Jika bisnis juga memiliki toko online, integrasi program kasir dengan platform e-commerce seperti Shopee, Tokopedia, dan lainnya dapat mempermudah manajemen pesanan secara otomatis. Hal ini dapat menghemat waktu dan tenaga pemilik bisnis dalam memproses pesanan dan pengiriman barang.
