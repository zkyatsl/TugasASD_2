
import os
os.system('cls')
from prettytable import PrettyTable

class Game:
    def __init__(self, id, judul, genre, harga, jumlah):
        self.id = id
        self.judul = judul
        self.genre = genre
        self.harga = harga
        self.jumlah = jumlah

class Node:
    def __init__(self, game):
        self.game = game
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_game(self, game, pos="akhir", id_sebelum=None):
        new_node = Node(game)

        if pos == "awal":
            new_node.next = self.head
            self.head = new_node
            self.update_node_ids()
        elif pos == "akhir":
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
                new_node.game.id = current.game.id + 1
        elif pos == "antara":
            if not self.head or not self.head.next:
                print("Minimal dua node untuk menambah di antara.")
                return

            current = self.head
            while current.next and current.next.game.id != id_sebelum:
                current = current.next

            if current.next:
                new_node.next = current.next
                current.next = new_node
                self.update_node_ids()
            else:
                print(f"Game dengan ID {id_sebelum} tidak ditemukan.")
        else:
            print("Posisi tidak valid.")

    def update_node_ids(self):
        current = self.head
        id_counter = 1
        while current:
            current.game.id = id_counter
            id_counter += 1
            current = current.next

    def remove_game(self, pos=None, id_sebelum=None):
        if not self.head:
            print("Linked list kosong. Tidak ada yang dapat dihapus.")
            return False

        if pos == "awal":
            self.head = self.head.next
            self.update_node_ids()
            return True
        elif pos == "akhir":
            current = self.head
            if not current.next:
                self.head = None
                return True
            while current.next.next:
                current = current.next
            current.next = None
            return True
        elif pos == "antara":
            if not self.head or not self.head.next:
                print("Minimal dua node untuk menghapus di antara.")
                return False

            if not id_sebelum:
                print("ID game tidak boleh kosong.")
                return False

            current = self.head

    # Menangani kasus penghapusan di awal
            if current.game.id == id_sebelum:
                self.head = self.head.next
                self.update_node_ids()
                return True

            while current.next and current.next.game.id != id_sebelum:
                current = current.next

            if current.next:
                current.next = current.next.next
                self.update_node_ids()
                return True
            else:
                print(f"Game dengan ID {id_sebelum} tidak ditemukan.")
                return False    


    def update_stok(self, game_id, new_stock):
        current = self.head
        while current:
            if current.game.id == game_id:
                current.game.jumlah = new_stock
                return True
            current = current.next
        return False

    def display_games(self):
        current = self.head
        table = PrettyTable()
        table.field_names = ["NO", "Judul", "Genre", "Harga", "Jumlah"]
        while current:
            game = current.game
            table.add_row([game.id, game.judul, game.genre, game.harga, game.jumlah])
            current = current.next
        print(table)

# Menu Utama sekaligus sama CRUD nya
def main():
    game_store = LinkedList()
    game1 = Game(1, "The Last of Us Part II", "Action-Adventure", 630000, 10)
    game2 = Game(2, "God of War", "Action-Adventure", 729000, 5)
    game3 = Game(3, "Uncharted 4: A Thief's End", "Action-Adventure", 250000, 3)
    game4 = Game(4, "Sekiro™: Shadows Die Twice - GOTY Edition", "Action-Adventure", 891000, 7)
    game_store.tambah_game(game1)
    game_store.tambah_game(game2)
    game_store.tambah_game(game3)
    game_store.tambah_game(game4)
    print("="*71)
    print ("|                  SELAMAT DATANG DI MAMANK GAMESHOP                   |")
    print("="*71)
    game_store.display_games()

    while True:
        print("="*71)
        print("|                         WELCOME, ADMIN Mamanks                      |")
        print("="*71)
        print("Menu:")
        print("1. Tambah Game")
        print("2. Hapus Game")
        print("3. Update Stok Game")
        print("4. Tampilkan Semua Game")
        print("5. Keluar")

        choice = input("Pilih opsi: ")

        if choice == "1":
            id = int(input("Masukkan ID Game: "))
            judul = input("Masukkan Judul Game: ")
            genre = input("Masukkan Genre Game: ")
            harga = float(input("Masukkan Harga Game: "))
            jumlah = int(input("Masukkan Stok Game: "))
            print("Pilih posisi tambahan:")
            print("1. Di Awal")
            print("2. Di Akhir")
            print("3. Di Antara")
            posisi_pilihan = input("Pilih posisi (1-3): ")
            if posisi_pilihan == '1':
                game_store.tambah_game(Game(id, judul, genre, harga, jumlah), pos="awal")
            elif posisi_pilihan == '2':
                game_store.tambah_game(Game(id, judul, genre, harga, jumlah), pos="akhir")
            elif posisi_pilihan == '3':
                id_sebelum = int(input("Masukkan ID game sebelum posisi baru: "))
                game_store.tambah_game(Game(id, judul, genre, harga, jumlah), pos="antara", id_sebelum=id_sebelum)
            else:
                print("Pilihan posisi tidak valid.")
            print("Game berhasil ditambahkan!.")

        elif choice == "2":
            print("Pilih posisi penghapusan:")
            print("1. Di Awal")
            print("2. Di Akhir")
            print("3. Di Antara")
            posisi_pilihan_hapus = input("Pilih posisi (1-3): ")
            if posisi_pilihan_hapus == '1':
                if game_store.remove_game(pos="awal"):
                    print("Game di awal berhasil dihapus.")
                else:
                    print("Game di awal tidak ditemukan atau tidak dapat dihapus.")
            elif posisi_pilihan_hapus == '2':
                if game_store.remove_game(pos="akhir"):
                    print("Game di akhir berhasil dihapus.")
                else:
                    print("Game di akhir tidak ditemukan atau tidak dapat dihapus.")
            elif posisi_pilihan_hapus == '3':
                id_sebelum = int(input("Masukkan ID game sebelum posisi yang ingin dihapus: "))
                if game_store.remove_game(pos="antara", id_sebelum=id_sebelum):
                    print(f"Game di antara berhasil dihapus.")
                else:
                    print(f"Game di antara tidak ditemukan atau tidak dapat dihapus.")
            else:
                print("Pilihan posisi tidak valid.")

        elif choice == "3":
            game_id = int(input("Masukkan ID Game yang ingin diupdate stoknya: "))
            new_stock = int(input("Masukkan Stok Baru: "))
            if game_store.update_stok(game_id, new_stock):
                print("Stok game berhasil diupdate!.")
            else:
                print("Game yang kamu cari ga ada!.")

        elif choice == "4":
            game_store.display_games()

        elif choice == "5":
            print("Terima kasih! Balik ya!")
            break

        else:
            print("Opsi tidak valid. Silakan pilih opsi yang benar.")

if __name__ == "__main__":
    main()
