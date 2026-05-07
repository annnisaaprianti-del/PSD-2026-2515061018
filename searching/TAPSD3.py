
import time
def main():
    print("=" * 45)
    print("      SISTEM CEK ELIGIBLE      ")
    print("=" * 45)
    
    data = [{"nama":"ica","nilai": 90}, {"nama" : "dania", "nilai" :97}, {"nama":"ulfa", "nilai" : 87},
         {"nama" : "citra", "nilai" : 86}, {"nama": "dendi","nilai": 70},
         {"nama": "aldi", "nilai" :80}, {"nama":"jovin","nilai": 98 },
         {"nama":"devi","nilai": 97}, {"nama":"aldi", "nilai":88}, 
         {"nama":"sifa", "nilai":85}]
    n = len(data)
    data.sort(key=lambda x: x["nilai"], reverse=True) #data.sort = untuk mengurutkan pada variabel data
                                                    #(key=lambda x: x["nilai"]) =untuk menyoro pada bagian nilai, jadi nilai lah yang akan di urutkan
                                                    #reverse=true ini berfungsi pengurutan berdasarkan dari yabg terbesar ke yang terkecil
    while True:
        try:
            target = str(input("atas nama siapa? :") ).lower()
            time.sleep(2)
            break
        except ValueError:
            print("Input Tidak Valid!")
    for i, siswa in enumerate(data): #enumerate(data) = agar bisa mngambil nilai dan datanya secara langsung    
        if target == siswa["nama"]:
            if siswa["nilai"] >= 85:
             print(f"Selamat atas nama {siswa['nama']} mendapat nilai akhir {siswa['nilai']} dan menjadi siswa eligible ke-{i + 1}")
            else:
                print(f"Nilai anda {siswa["nilai"]} Mohon maaf nama anda tidak terdaftar sebagai siswa Eligible")
                
if __name__ == "__main__":
    main()
        


