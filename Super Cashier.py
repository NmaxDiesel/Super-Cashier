class Transaction:
    def __init__(self):
        self.order_list = {}

    def add_item(self, name, quantity, price):

        #Fungsi ini digunakan untuk menambahkan item yang konsumen pilih ke dalam list barang yang dibeli.
        #Parameternya adalah list, string, int, dan float.
        #Di sini tidak menghasilkan output.

        if name not in self.order_list:
            self.order_list[name] = [quantity, price]
        else:
            self.order_list[name][0] += quantity

    def delete_item(self, name):
      
        #Fungsi ini digunakan untuk menghapus item yang konsumen pilih.
        #Parameter di sini ialah nama item yang konsumen pilih.
        #Di sini tidak menghasilkan output.
        
        del self.order_list[name]

    def update_item_name(self, name, update_name):
     
        #Fungsi ini digunakan untuk mengupdate nama item yang konsumen pilih.
        #Parameter di sini ialah nama item yang ingin konsumen ubah.
        #Di sini tidak menghasilkan output.
     
        self.order_list[update_name] = self.order_list.pop(name)

    def update_item_qty(self, name, update_quantity):
     
        #Fungsi ini digunakan untuk mengupdate jumlah item yang konsumen inginkan.
        #Parameter di sini ialah nama item yang ingin konsumen ubah.
        #Di sini tidak menghasilkan output.
        
        self.order_list[name][0] = update_quantity

    def update_item_price(self, name, update_price):
      
        #Fungsi ini digunakan untuk mengubah harga item yang konsumen inginkan.
        #Parameter di sini ialah harga item yang ingin konsumen diubah.
        #Di sini tidak menghasilkan output.
        
        self.order_list[name][1] = update_price

    def check_order(self):
      
        #Fungsi ini digunakan untuk mengecek daftar item yang konsumen inginkan beserta total harganya.
        #Parameter di sini ialah instance dari kelas Transaction.
        #Di sini outputnya ialah harga total.
       
        if not self.order_list:
            print("Belum ada item yang dibeli")
        else:
            print("Item yang dibeli adalah:")
            print("| No | Nama item | Jumlah item | Harga/item | Total harga |")
            print("-" * 65)
            total_price = 0
            for index, (name, item_info) in enumerate(self.order_list.items(), start=1):
                quantity, price = item_info
                total = quantity * price
                print(f"| {index:<2} | {name:<9} | {quantity:<11} | {price:>10,.0f} | {total:>11,.0f} |")
                total_price += total
            print("-" * 65)
            return total_price

    def total_price(self):
      
        #Fungsi ini digunakan untuk menghitung total harga yang harus konsumen bayar serta diskon yang didapatkan.
        #Parameternya di sini ialah instance dari kelas Transaction.
        #Di sini tidak menghasilkan output.
        
        total_price = self.check_order()
        if total_price:
            discount = 0
            if total_price > 500000:
                discount = 0.07
            elif total_price > 300000:
                discount = 0.06
            elif total_price > 200000:
                discount = 0.05

            discounted_price = total_price - (total_price * discount)
            print(f"Total belanja yang harus dibayarkan adalah {discounted_price:,.0f}")

    def reset_transaction(self):
      
        #Fungsi ini digunakan untuk menghapus semua item pada riwayat belanja konsumen.
        #Parameternya di sini ialah hasil instance dari kelas Transaction.
        #Di sini tidak menghasilkan output.
       
        self.order_list = {}
        print("Semua item berhasil dihapus!")


def main():

    #Fungsi utama yang akan dieksekusi saat program dijalankan. 
    #Fungsi ini mengatur alur program utama dan berisi perintah-perintah yang akan dijalankan oleh pengguna.

    print("Luthfi Coffeeshop Jl. Sumatera Raya no.420 Depok")
    print("Selamat datang, selamat berbelanja")
    print("Silakan inputkan menu yang ingin anda beli")
    transaksi = Transaction()

    #Mendeklarasikan objek transaksi yang mungkin merupakan suatu objek kelas Transaction.
    #Ini digunakan untuk merekam dan mengatur transaksi belanja pengguna.

    while True:
    
    #Memulai loop tak terbatas yang akan terus berjalan sampai program dihentikan.

        print("==========================================")
        print("1. Tambah item belanjaan")
        print("2. Hapus item belanjaan")
        print("3. Reset transaksi")
        print("4. Cek pesanan")
        print("5. Hitung total harga")
        print("6. Update item name")
        print("7. Update item qty")
        print("8. Update item price")
        print("9. Keluar")
        print("==========================================")
        print("Jangan lupa berikan tips yaa :<")
        try:
            pilihan = int(input("Masukkan pilihan anda: "))
            if pilihan == 1:
                nama_item = input("Masukkan nama item: ")
                quantity = int(input("Masukkan jumlah item: "))
                harga = int(input("Masukkan harga per item: "))
                transaksi.add_item(nama_item, quantity, harga)
            elif pilihan == 2:
                nama_item = input("Masukkan nama item yang ingin dihapus: ")
                transaksi.delete_item(nama_item)
            elif pilihan == 3:
                transaksi.reset_transaction()
                print("Semua item berhasil dihapus!")
            elif pilihan == 4:
                transaksi.check_order()
            elif pilihan == 5:
                transaksi.total_price()
            elif pilihan == 6:
                nama_item_lama = input("Masukkan nama item yang ingin diupdate: ")
                nama_item_baru = input("Masukkan nama item yang baru: ")
                transaksi.update_item_name(nama_item_lama, nama_item_baru)
            elif pilihan == 7:
                nama_item = input("Masukkan nama item yang ingin diupdate: ")
                qty_baru = int(input("Masukkan jumlah item yang baru: "))
                transaksi.update_item_quantity(nama_item, quantity_baru)
            elif pilihan == 8:
                nama_item = input("Masukkan nama item yang ingin diupdate: ")
                harga_baru = int(input("Masukkan harga per item yang baru: "))
                transaksi.update_item_price(nama_item, harga_baru)
            elif pilihan == 9:
                print("Terima kasih telah mengunjungi Luthfi Coffeeshop, terima kasih sudah berbelanjadan jangan lupa kunjungi lagi yaa !")
                break

            #ika nilai "pilihan" adalah 9, maka akan dicetak pesan "Terima kasih telah mengunjungi Luthfi Coffeeshop, terima kasih sudah berbelanja dan jangan lupa kunjungi lagi yaa !".
            #Program akan keluar dari loop menggunakan perintah "break".

            else:
                print("Maaf, Terdapat kesalahan input data!")
        except ValueError:

           #Jika nilai "pilihan" tidak ada yang sesuai#, maka akan dicetak pesan "Maaf, Terdapat kesalahan input data!".

            print("Maaf, Terdapat kesalahan input data. Silakan dicoba kembali dengan benar!")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

