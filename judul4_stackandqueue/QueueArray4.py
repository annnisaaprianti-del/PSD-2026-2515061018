class QueueArray:
    def __init__(self, max_size=10):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Daftar musik anda penuh")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = x
        print(f"lagu {x} berhasil ditambahkan dalam playlist")

    def dequeue(self):
        if self.is_empty():
            print("Playlist anda kosong")
            return
        print(f"lagu {self.q[self.front_idx]} berhasil diputar")
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Playlist kosong")
            return
        print(f"lagu pertama dalam playlist: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("playlist kosong")
            return
        
        print("daftar musik dalam playlist: ", end="")
        i = self.front_idx
        while True:
            # Cetak nama lagu
            print(self.q[i], end="")
            
            # Jika lagu ini bukan lagu terakhir (rear_idx), cetak koma dan spasi
            if i == self.rear_idx:
                break
            print(", ", end="")
            
            i = (i + 1) % self.MAXN
        print()

def main():
    queue = QueueArray()
    pilih = 0
    while pilih != 5:
        print("\n=== Playlist Favorit icaa ===")
        print(" halo icaa! apa yang ingin kamu lakukan ?")
        print("1. tambah lagu")
        print("2. putar lagu")
        print("3. lagu pertama")
        print("4. Tampilkan playlist")
        print("5. Keluar dari playlist")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
            
        if pilih == 1:
            val = input("lagu apa yang ingin anda tambahkan?: ")
            queue.enqueue(val)
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()