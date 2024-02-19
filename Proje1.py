

class Library:
    def __init__(self, file_path="books.txt"):
        self.file_path = file_path
        self.check_file_existence()
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def check_file_existence(self):
        try:
            open(self.file_path, "r").close()
        except FileNotFoundError:
            open(self.file_path, "w").close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        if not book_lines:
            print("Kütüphane boş.")
        else:
            for line in book_lines:
                book_info = line.split(',')
                print(f"Kitap Adı: {book_info[0]}, Yazar: {book_info[1]}")

    def add_book(self):
        kitapAdi = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        yayinYili = input("İlk Yayın Yılı: ")
        sayfaSayisi = input("Sayfa Sayısı: ")

        book_info = f"{kitapAdi},{yazar},{yayinYili},{sayfaSayisi}\n"
        self.file.write(book_info)
        print("Kitap eklendi.")

    def remove_book(self):
        silinenKitap = input("Silinecek Kitap Adı: ")
        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        book_to_remove_index = -1
        for i, line in enumerate(book_lines):
            if silinenKitap in line:
                book_to_remove_index = i
                break

        if book_to_remove_index != -1:
            del book_lines[book_to_remove_index]
            self.file.seek(0)
            self.file.truncate()

            for updated_book in book_lines:
                self.file.write(updated_book + '\n')

            print(f"{silinenKitap} adlı kitap silindi.")
        else:
            print(f"{silinenKitap} adlı kitap bulunamadı.")

#lib adında nesne oluşturarak Library classını kullandım
lib = Library()


while True:
    print("*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")
    print("4) Çıkış")

    choice = input("Lütfen bir seçenek girin (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
        
    elif choice == "4":
        break
    else:
        print("Geçersiz seçenek. Lütfen 1 ile 4 arasında bir sayı girin.")


# In[ ]:




