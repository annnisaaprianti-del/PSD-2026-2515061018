class Node:
    def __init__(self, kode_pos, nama_penerima, alamat):
        self.key = kode_pos  
        self.nama_penerima = nama_penerima
        self.alamat = alamat
        self.left = None
        self.right = None

class SistemSortirKantorPos:
    def __init__(self):
        self.root = None
        
    def insert_node(self, root, kode_pos, nama_penerima, alamat):
        if root is None:
            return Node(kode_pos, nama_penerima, alamat)
        if kode_pos < root.key:
            root.left = self.insert_node(root.left, kode_pos, nama_penerima, alamat)
        elif kode_pos > root.key:
            root.right = self.insert_node(root.right, kode_pos, nama_penerima, alamat)
        return root

    def insert(self, kode_pos, nama_penerima, alamat):
        self.root = self.insert_node(self.root, kode_pos, nama_penerima, alamat)

    def search_node(self, root, kode_pos):
        if root is None:
            return None
        if root.key == kode_pos:
            return root
        if kode_pos < root.key:
            return self.search_node(root.left, kode_pos)
        else:
            return self.search_node(root.right, kode_pos)
        
    def search(self, kode_pos):
        return self.search_node(self.root, kode_pos)
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(f"[{root.key}] Penerima: {root.nama_penerima} | Alamat: {root.alamat}")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(f"[{root.key}]", end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(f"[{root.key}]", end=" ")

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)


def main():
    pos = SistemSortirKantorPos()
    pilih = 0
    while pilih != 10:
        print("\n=== SISTEM SORTIR KANTOR POS (BST) ===")
        print("1. Registrasi Surat Masuk (Insert)")
        print("2. Lacak Surat berdasarkan Kode Pos (Search)")
        print("3. Cetak Rute Distribusi Kurir (Inorder - Terurut)")
        print("4. Cetak Struktur Pohon Distribusi (Preorder)")
        print("5. Cetak Riwayat Evaluasi Pengiriman (Postorder)")
        print("6. Cek Jangkauan Kode Pos Terkecil (Min)")
        print("7. Cek Jangkauan Kode Pos Terbesar (Max)")
        print("8. Hitung Total Surat di Gudang (Count Nodes)")
        print("9. Hitung Total Nilai Kode Pos Terdaftar (Sum Nodes)")
        print("10. Keluar")
        try:
            pilih = int(input("Pilih Menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue
            
        if pilih == 1:
            try:
                kd = int(input("Masukkan Kode Pos (Angka): "))
                nama = input("Masukkan Nama Penerima: ")
                alm = input("Masukkan Alamat Tujuan: ")
                pos.insert(kd, nama, alm)
                print(f"Surat dengan Kode Pos {kd} berhasil disortir ke dalam sistem.")
            except ValueError:
                print("Input Kode Pos harus berupa angka!")
        elif pilih == 2:
            try:
                kd = int(input("Cari Kode Pos: "))
                hasil = pos.search(kd)
                if hasil:
                    print(f"--> Surat Ditemukan! \nPenerima: {hasil.nama_penerima} \nAlamat: {hasil.alamat}")
                else:
                    print("--> Surat untuk Kode Pos tersebut tidak ditemukan.")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            print("\n--- Rute Distribusi Kurir (Terurut Kode Pos) ---")
            pos.inorder(pos.root)
        elif pilih == 4:
            print("Struktur Preorder: ", end="")
            pos.preorder(pos.root)
            print()
        elif pilih == 5:
            print("Struktur Postorder: ", end="")
            pos.postorder(pos.root)
            print()
        elif pilih == 6:
            print(f"Kode Pos Terkecil: {pos.find_min(pos.root)}")
        elif pilih == 7:
            print(f"Kode Pos Terbesar: {pos.find_max(pos.root)}")
        elif pilih == 8:
            print(f"Total Surat di Gudang Saat Ini: {pos.count_nodes(pos.root)} surat")
        elif pilih == 9:
            print(f"Jumlah Total Nilai Kode Pos: {pos.sum_nodes(pos.root)}")
        elif pilih == 10:
            print("Sistem dimatikan. Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()