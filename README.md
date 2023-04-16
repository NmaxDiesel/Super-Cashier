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
