from tabulate import tabulate
import sys

def cekKategori(aksi):
    setKategori = set()  # Biar ngak ada duplikat
    for i in range(len(listStok)): # Mencari Kategori yang ada
        setKategori.add(listStok[i][4])
    
    # Ubah set menjadi list of lists
    listKategori = [[kategori] for kategori in setKategori]
    
    
    # Menggunakan tabulate untuk mencetak tabel
    tableKategori = tabulate(
        listKategori,
        headers  = ["Kategori"],
        tablefmt="fancy_grid",
        colalign=("center",)
    )

    print(f'''
=========================     
Berikut Kategori yang ada 
    Didalam Database
=========================
{tableKategori}
    ''')
    listKategoriValidasi = list(setKategori) #untuk mengecek kategori 
    while True:
        inputKategori = input(f"Masukkan Kategori apa yang ingin anda {aksi} (Tahu/Minuman/..) : ").title().strip()
        if inputKategori in listKategoriValidasi: #tidak bisa pakai list kategori karena bentuknya list dalam list
            return inputKategori
        
        else :
            print('''
=========================================
Maaf INPUT yang anda masukkan masih salah
        Silahkan Coba Lagi
=========================================                 
                  ''')
        
def beneranMauUpdate(index, indexKolom,inputUpdate):
    while True:
        inputUpdateValidasi = input(f"Apakah anda benar ingin mengupdate data tersebut (Y/N) ? ").upper().strip()
        if inputUpdateValidasi == "Y" or inputUpdateValidasi =="YES":
            print(f'''
===============================================================================
Selamat anda berhasil mengupdate {headers[indexKolom]} dari stok {listStok[index][2]}
===============================================================================
''')        
            if indexKolom ==3 or indexKolom == 5: #ini buat yang masuknya integer
                listStok[index][indexKolom] = int(inputUpdate)
                listStok[index][-1] = listStok[index][3] * listStok[index][5]
            
            elif indexKolom == 2 or indexKolom == 4 :
                listStok[index][indexKolom] = inputUpdate
            menuUpdateStok()
            
        elif inputUpdateValidasi == "N" or inputUpdateValidasi =="NO":
            menuUpdateStok()
        else :
            print(f'''
================================================
Input yang anda masukkan salah (bukan angka Y/N)
        Silahkan Coba lagi 
================================================
''')
            beneranMauUpdate(index, indexKolom,inputUpdate)
            
def validasiUpdateKolom(index, kolomApa): #index angak sedangkan kolomapa string kolom nya
    #print index specificnya
    listDicari = [listStok[index]]
    indexKolom = headers.index(kolomApa)
    tampilkanTableStok(listDicari)

    while True:  
            inputUpdate = input(f"Nilai {listDicari[0][indexKolom]} ingin diubah jadi apa : ").strip().title()
        # headers=["No","Id", "Nama", "Stok", "Kategori", "Harga Per Stok"]
            if len(inputUpdate) == 0 :
                print(''''
================================================
         Input yang anda masukkan salah 
                tidak boleh kosong
                Silahkan Coba lagi 
================================================                    
''') #handle ketika input yang dimasukkan user kosong
                validasiUpdateKolom(index, kolomApa)
                
            if kolomApa == "Stok" or kolomApa =="Harga Per Stok" : #handle untuk update "Stok" dan "Harga Per Stok"
                if inputUpdate.isdigit() == False :
                    print('''
================================================
        Input yang anda masukkan salah 
    STOK dan Harga Per Stok tidak boleh Alphabet
     atau kosong atau tidak boleh kurang dari 0
                Silahkan Coba lagi 
================================================                    
    ''') #handle ketika input nama dan kategorinya ada angka gakboleh
                    validasiUpdateKolom(index, kolomApa)
                
                #ketika udh bener ganti fungsi
                beneranMauUpdate(index, indexKolom,inputUpdate)
                menuUpdateStok()
                
            if kolomApa == "Nama" or kolomApa =="Kategori":
                if all(i.isalpha() for i in inputUpdate.split()) == False :
                    print('''
=====================================================
        Input yang anda masukkan salah 
    NAMA dan KATAGORI tidak boleh ada nilai numerikal
            atau character (@#$%^&*)
                Silahkan Coba lagi 
=====================================================                    
''') #handle ketika input ada nilai numerikal example(zidan1 ada123) ini ngak boleh
                    validasiUpdateKolom(index, kolomApa)
                if  kolomApa =="Kategori" :
                    #ketika udh bener ganti fungsi
                    beneranMauUpdate(index, indexKolom,inputUpdate)
                    menuUpdateStok()

                if kolomApa == "Nama":
                    listSementara = listStok[index].copy()
                    listSementara[2] = inputUpdate
                    if validasiDuplikat(listSementara) == True : #hasilin true ketika sama
                        print(f'''
==============================================================
Input yang anda masukkan salah NAMA Dari Stok tidak boleh sama
                Silahkan Coba lagi 
==============================================================
''')                    
                        menuUpdateStok()
                    elif validasiDuplikat(listSementara) == False :
                        beneranMauUpdate(index, indexKolom,inputUpdate)
                        menuUpdateStok()
       
def validasiUpdateIndex(indexDiubah):
    while True:
        try:
            # tampilkanTableStok(listStok[indexDiubah])
            inputUpdateKolom = input("Masukkan Kolom apa yang ingin anda ubah (Nama, Stok, Kategori, Harga Per Stok)  selain No, Harga Total dan Id: ").title().strip()
            if inputUpdateKolom == "No" or inputUpdateKolom == "Id" or inputUpdateKolom == "Harga Total": #Nomor sama id sama harga total tidak boleh diubah
                print(f'''
============================================================
Input yang anda masukkan salah No atau Id tidak boleh diubah
                Silahkan Coba lagi 
============================================================
''')
            elif inputUpdateKolom in headers:
                validasiUpdateKolom(indexDiubah-1,inputUpdateKolom) #kurangin satu karena index 
            else:
                print(f'''
=======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
                Silahkan Coba lagi 
=======================================================
''')
        except ValueError:
            print(f'''
=======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
                Silahkan Coba lagi 
=======================================================
''')
    
def updateStok():
    tampilkanTableStok(listStok)
    
    listbaru = [[item[0], item[1]] for item in listStok] #mendapatkan id dan nomor dari list utama
    # Print using tabulate
    print('''
=====================
Berikut Merupakan Id
Yang anda dapat Update
=====================  
          ''')
    tableId = tabulate(
                listbaru, 
                headers=["No", "ID"], 
                tablefmt="fancy_grid",
                colalign=("center", "center")
            )
    print(tableId)
    while True :
        try :
            inputUpdateIndex = int(input("Masukkan ID Stok yang ingin diubah nilainya (1,2,3,4,...): "))
            print(inputUpdateIndex)
            if inputUpdateIndex <= 0:
                print(f'''
=======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
                Silahkan Coba lagi 
=======================================================
''')            
                updateStok()
            if inputUpdateIndex <= len(listStok):
                validasiUpdateIndex(inputUpdateIndex)   
            else:
                print(f'''
=======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
                Silahkan Coba lagi 
=======================================================
''')
        except ValueError:
            print(f'''
=======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
                Silahkan Coba lagi 
=======================================================
''')
     
def menuUpdateStok() :
    while True :
        try:
            inputMenuUpdate = int(input('''
=====================
Menu Mengubah Stok
=====================
1. Mengubah Stok 
2. Kembali Ke Menu Utama 
Masukkan angka yang diinginkan : '''))
            
            if inputMenuUpdate == 1:
                if len(listStok) == 0: # Handle Database Kosong
                    print('''
==========================================
Dalam Database Belum Terdaftar Stok Apapun
Silahkan Masukkan Stok pada Database
==========================================
''')            
                    menuUpdateStok()
                else :
                    updateStok()
                
            elif inputMenuUpdate == 2:
                main_menu()
                
                
            else :
                print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 2)
                Silahkan Coba lagi 
=======================================================
''')
        except ValueError:
            print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 2)
                Silahkan Coba lagi 
=======================================================
''')

def hapusKategori():
    kategoriDicari = cekKategori("Hapus")
    while True :
        inputValidasiHapus = input(f"Apakah anda benar ingin menghapus Kategori {kategoriDicari} dari Database (Y/N) ? ").upper().strip()
        if inputValidasiHapus == "Y" or inputValidasiHapus =="YES":
            print(f'''
========================================
Selamat anda berhasil menghapus {kategoriDicari} dari database
========================================
                  ''')
            for item in listStok[:]:  #harus pakai [:] untuk iterasi semua yang ada di list
                if item[4] == kategoriDicari:
                    listStok.remove(item)
                    
            for i in range(len(listStok)):#buat ubah kolom nomor biar ngak aneh urutannya
                listStok[i][0] = i + 1
            
            menuHapusStok()
        elif inputValidasiHapus == "N" or inputValidasiHapus =="NO":
            menuHapusStok()
        else : # Handle input salah
            print(f'''
================================================
Input yang anda masukkan salah (bukan angka Y/N)
        Silahkan Coba lagi 
================================================
''')     
            
def validasiHapusSpesifik(inputIndexHAPUS):
    while True:
        inputValidasiHapus = input(f"Apakah anda benar ingin menghapus {listStok[inputIndexHAPUS-1][1]} dari Database (Y/N) ? ").upper().strip()
        if inputValidasiHapus == "Y" or inputValidasiHapus =="YES":
            print(f'''
======================================================
Selamat anda berhasil menghapus {listStok[inputIndexHAPUS-1][1]} dari database
======================================================
''')
            del listStok[inputIndexHAPUS-1] #Hapus stoknya
            
            for i in range(inputIndexHAPUS - 1, len(listStok)): #ngubah nomor jadi turun
                listStok[i][0] = i + 1 #Misal hapus index 2, index 3 dan 4 jadi turun 1
            menuHapusStok()
        
        elif inputValidasiHapus == "N" or inputValidasiHapus =="NO":
            menuHapusStok()
        else : # Handle input salah
            print(f'''
================================================
Input yang anda masukkan salah (bukan angka Y/N)
        Silahkan Coba lagi 
================================================
''')     
          
def hapusSpesifik():
    listbaru = [[item[0], item[1]] for item in listStok]#mendapatkan id dan nomor dari list utama
    # Print using tabulate
    print('''
=====================
Berikut Merupakan Id
Yand anda dapat hapus
=====================  
          ''')
    tableId = tabulate(
                listbaru, 
                headers=["No", "ID"], 
                tablefmt="fancy_grid",
                colalign=("center", "center")
            )
    print(tableId)
    
    while True:
            try:
                
                inputIndexHAPUS = int(input("Masukkan ID Stok yang ingin dihapus (1,2,3,4,5,...): "))
                if inputIndexHAPUS <= len(listStok):
                    validasiHapusSpesifik(inputIndexHAPUS)
                else :
                    print(f'''
=======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
        Silahkan Coba lagi 
=======================================================
''')
            except ValueError:
                print(f'''
=======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
                Silahkan Coba lagi 
=======================================================
''')
                
def menuHapusStok() :
    while True:
        try:
            inputMenuHapus = int(input('''
=====================
Menu Menghapus Stok
=====================
1. Menghapus Stok
2. Menghapus SELURUH Database Stok
3. Menghapus Stok Sesusai KATEGORI
4. Kembali Ke Menu Utama  
Masukkan angka yang ingin dijalankan : '''))
            if inputMenuHapus ==1:
                if len(listStok) == 0: # Handle Database Kosong
                    print('''
==========================================
Dalam Database Belum Terdaftar Stok Apapun
Silahkan Masukkan Stok pada Database
==========================================
''')                
                    menuHapusStok()
                    
                else :
                    tampilkanTableStok(listStok)
                    hapusSpesifik()
            elif inputMenuHapus == 2:
                if len(listStok) == 0: # Handle Database Kosong
                    print('''
==========================================
Dalam Database Belum Terdaftar Stok Apapun
Silahkan Masukkan Stok pada Database
==========================================
''')            
                    menuHapusStok()
                while True:
                    inputValidasiHapusSeluruh = input(f"Apakah anda benar ingin menghapus SELURUH DATA dari Database (Y/N) ? ").upper().strip()
                    if inputValidasiHapusSeluruh == "Y" or inputValidasiHapusSeluruh =="YES":
                        listStok.clear()
                        print(f'''
================================================
Selamat anda berhasil menghapus Seluruh Database
================================================
''')
                        menuHapusStok()
                    elif inputValidasiHapusSeluruh == "N" or inputValidasiHapusSeluruh =="NO":
                        menuHapusStok()
                    else : # Handle input salah
                        print(f'''
================================================
Input yang anda masukkan salah (bukan angka Y/N)
        Silahkan Coba lagi 
================================================
''')                
                        menuHapusStok()
            elif inputMenuHapus == 3:
                if len(listStok) == 0: # Handle Database Kosong
                    print('''
==========================================
Dalam Database Belum Terdaftar Stok Apapun
Silahkan Masukkan Stok pada Database
==========================================
''') 
                    menuHapusStok()
                else :
                    hapusKategori()
            elif inputMenuHapus == 4:
                main_menu()
            else: # Handle index out of bounds
                print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 2)
                Silahkan Coba lagi 
=======================================================
''')
        except ValueError: #Haddle input string
            print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 2)
                Silahkan Coba lagi 
=======================================================
''')

def validasiDuplikat(listYangAda):
    for item in listStok:
        if item[2].upper() == listYangAda[2].upper() :  # cek nama doang ngak boleh sama sisanya boleh
            return True
        
    return False

def validasiTambahStok(listTambah):
    while True:
        try :
            inputValidasiTambah = input(f"Apakah anda benar ingin menambah {listTambah[2]} kedalam Database (Y/N) ? ").upper().strip()
            if inputValidasiTambah == "Y" or inputValidasiTambah =="YES":
                print(f'''
================================================================
Selamat Anda Berhasi menambahkan {listTambah[1]} ke dalam Database
================================================================
''')
                listStok.append(listTambah)
                menuMenambahStok()
            elif inputValidasiTambah == "N" or inputValidasiTambah =="NO":
                menuMenambahStok()
            else :
                print(f'''
================================================
    Input yang anda masukkan salah (bukan Y/N)
                Silahkan Coba lagi 
================================================
''')
        except ValueError:
            print(f'''
================================================
    Input yang anda masukkan salah (bukan Y/N)
                Silahkan Coba lagi 
================================================
''')

def nambahStok():
    global idTerkahir
    while True:
        try:
            # Input Nama
            while True:
                inputTambahNama = input("Masukkan Nama bahan yang ingin ditambah : ")
                if not all(i.isalpha() for i in inputTambahNama.split()):
                    print('''
=====================================================
        Input yang anda masukkan salah 
    NAMA tidak boleh ada nilai numerikal
            atau karakter (@#$%^&*)
                Silahkan Coba lagi 
=====================================================                    
''')
                else:
                    break  # Exit loop if input is valid
            
            # Input Stock
            while True:
                try:
                    inputTambahStock = int(input("Masukkan Jumlah dari bahan tersebut : ")) 
                    if inputTambahStock < 0:
                        print('''
================================================
        Input yang anda masukkan salah 
  input stok tidak boleh kurang dari 0
                Silahkan Coba lagi 
================================================                    
''')
                    else:
                        break  # Exit loop if input is valid
                except ValueError:
                    print(f'''
======================================================
            Input yang anda masukkan salah
                Silahkan Coba lagi 
======================================================
''')
            
            # Input Kategori
            while True:
                inputTambahKategori = input("Masukkan Kategori dari bahan Tersebut   : ").title()
                if not all(i.isalpha() for i in inputTambahKategori.split()):
                    print('''
=====================================================
        Input yang anda masukkan salah 
    KATEGORI tidak boleh ada nilai numerikal
            atau karakter (@#$%^&*)
                Silahkan Coba lagi 
=====================================================                    
''')
                else:
                    break  # Exit loop if input is valid
            
            # Input Harga
            while True:
                try:
                    inputTambahHarga = int(input("Masukkan Harga dari bahan tersebut  : "))
                    if inputTambahHarga < 0:
                        print('''
================================================
        Input yang anda masukkan salah 
  input harga tidak boleh kurang dari 0
                Silahkan Coba lagi 
================================================                    
''')
                    else:
                        break  # Exit loop if input is valid
                except ValueError:
                    print(f'''
======================================================
            Input yang anda masukkan salah
                Silahkan Coba lagi 
======================================================
''')
            
            # Generate new ID and No
            inputTambahNo = len(listStok) + 1  # Get the next number
            inputTambahID = int(idTerkahir[-3:])  # Get the last three characters as int (IDxxx)
            inputTambahID += 1  # Increment by one
            inputTambahID = idTerkahir[:-3] + str(inputTambahID).zfill(3)  # Combine with "ID" and zero-fill
            idTerkahir = inputTambahID
            
            #Generate total harga
            inputTotalHarga = inputTambahStock* inputTambahHarga
            # Check for empty fields
            if any(len(field.strip()) == 0 for field in [inputTambahNama, inputTambahKategori]): 
                print('''
================================================
         Input yang anda masukkan salah 
                tidak boleh kosong
                Silahkan Coba lagi 
================================================                    
''')
                continue  # Retry input
            
            # Create new stock entry
            listbaru = [inputTambahNo, inputTambahID, inputTambahNama, inputTambahStock, inputTambahKategori, inputTambahHarga,inputTotalHarga]
            
            # Check for duplicate names
            if validasiDuplikat(listbaru):  # Check for duplicate names
                print(f'''
==============================================================
Input yang anda masukkan salah NAMA Dari Stok tidak boleh sama
                Silahkan Coba lagi 
==============================================================
''')
                continue  # Retry input
            else:
                validasiTambahStok(listbaru)
                break  # Exit the loop after successful addition
            
        except ValueError:
            print(f'''
======================================================
            Input yang anda masukkan salah
                Silahkan Coba lagi 
======================================================
''')
            continue  # Retry input


def menuMenambahStok():
    while True:
        try :
            inputMenuTambah = int(input('''
=====================
Menu Menambah Stok
=====================
1. Menambah Bahan
2. Kembali Ke Menu Utama 
Masukkan angka yang diinginkan : '''))
            if inputMenuTambah == 1:
                nambahStok()
            elif inputMenuTambah == 2:
                main_menu()
            else : #handle index out of bounds
                print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 2)
                Silahkan Coba lagi 
=======================================================
''')
        except ValueError: #Handle Input Salah
            print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 2)
                Silahkan Coba lagi 
=======================================================
''')
   
def tampilkanKategori():
    
    kategoriDicari= cekKategori("Lihat") 
    
    # List comprehension untuk mendapatkan sub-list yang memiliki "kategori yang sesuai" di indeks Ke Empat
    listHasilFilter = [item for item in listStok if item[4] == kategoriDicari]
    print(f'''
======================================================
Berikut Merupakan Tabel yang memiliki Kategori {kategoriDicari}          
======================================================
''')
    tampilkanTableStok(listHasilFilter)
    menuMenampilkanStok()
   
def sortDataBeneran(indexkolom, urutanSort):
    listSorted = listStok.copy() #biar list awal tetep sama dan ngak berubah
    if urutanSort == "ASC" :
        for i in range(len(listSorted)) : 
            for j in range(0, len(listSorted)-i-1): 
                if listSorted[j][indexkolom] > listSorted[j + 1][indexkolom]: # Mencari paling kanan Taro Kanan
                    listSorted[j], listSorted[j + 1] = listSorted[j + 1], listSorted[j]
        
    elif urutanSort == "DESC" :
        for i in range(len(listSorted)) :
            for j in range(0, len(listSorted)-i-1): 
                if listSorted[j][indexkolom] < listSorted[j + 1][indexkolom]: # ini kurang dari buat reversenya
                    listSorted[j], listSorted[j + 1] = listSorted[j + 1], listSorted[j]
        
    print(f'''
===========================================
    Berikut Merupakan Isi dari Database 
    Setelah Di urutkan berdasrkan {headers[indexkolom]}
===========================================''')
    tampilkanTableStok(listSorted)
    menuMenampilkanStok() 

def sortData(kolomSort):
    while True:
        try:
            inputorder = input("Ingin di urutkan secara Apa (ASC/DESC)? ").upper().strip()
            indexKolom= headers.index(kolomSort)
            if inputorder == "ASC" or inputorder == "DESC":
                sortDataBeneran(indexKolom, inputorder)
            else :
                print(f'''
===============================================
Input yang anda masukkan salah (bukan ASC/DESC)
                Silahkan Coba lagi 
===============================================
''')
        except ValueError:
            print(f'''
===============================================
Input yang anda masukkan salah (bukan ASC/DESC)
                Silahkan Coba lagi 
===============================================
''')
            
def menuSortingData():
    while True: # Handle Validasi Y/N
        inputValidasiSort = input("Apakah anda ingin mengurutkan data berdasarkan kolom tertentu (Y/N) ? ").upper().strip()
        
        if inputValidasiSort == "Y" or inputValidasiSort =="YES":
            while True: #Kalo Kolom masuk salah balik lagi
                try:
                    inputKolomSort = input("Kolom Apa yang ingin anda sort(No, Id, Nama, Stok, Kategori, Harga Per Stok, Harga Total) ? ").title().strip()#handle gede kecil input pake title
                    if inputKolomSort in headers:
                        sortData(inputKolomSort)
                    else : # Handle input salah
                        print(f'''
===================================================
Input yang anda masukkan salah (tidak ada dalam DB)
                Silahkan Coba lagi 
===================================================
''')
                        
                except ValueError: #Handle input salah
                    print(f'''
================================================
Input yang anda masukkan salah (bukan angka Y/N)
                Silahkan Coba lagi 
================================================
''')
                    
        elif inputValidasiSort == "N" or inputValidasiSort =="NO":
            menuMenampilkanStok()
            
        else : #Handle input salah
            print(f'''
================================================
Input yang anda masukkan salah (bukan angka Y/N)
                Silahkan Coba lagi 
================================================
''')

def tampilkanDataSpesifik():
    if len(listStok) == 0 :
        print('''
==========================================
Dalam Database Belum Terdaftar Stok Apapun
Silahkan Masukkan Stok pada Database
==========================================
''')  #handle database kosong
        menuMenampilkanStok()
        
    
    listbaru = [[item[0], item[1]] for item in listStok] #mendapatkan id dan nomor dari list utama
    # Print using tabulate
    print('''
=====================
Berikut Merupakan Id
Yand anda dapat Lihat
=====================  
          ''')
    tableId = tabulate(
                listbaru, 
                headers=["No", "ID"], 
                tablefmt="fancy_grid",
                colalign=("center", "center")
            )
    print(tableId)
    
    while True:
        try:
            inputIndexDataSpesifik = int(input("Masukkan Id yang ingin dilihat detailnya (1,2,3,4,....): "))-1 
            if inputIndexDataSpesifik < 0 :
                print(f'''
======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
                Silahkan Coba lagi 
======================================================
''')            
                tampilkanDataSpesifik()
            if inputIndexDataSpesifik < len(listStok) :
                listDataSpesifik = [listStok[inputIndexDataSpesifik]]#harus list dalam list untuk tabulate
                tampilkanTableStok(listDataSpesifik)
                menuMenampilkanStok()
            else :
                print(f'''
======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
                Silahkan Coba lagi 
======================================================
''')
        except :
            print(f'''
======================================================
Input yang anda masukkan salah (diluar INDEX yang ada)
                Silahkan Coba lagi 
======================================================
''')
    
def menuMenampilkanStok():
    while True :
        try :
            inputValidasi = int(input('''
=====================
Menu Menampilkan Stok
=====================
1. Tampilkan Semua Stok
2. Tampilkan Bahan Tertentu
3. Tampilkan Bahan Per Kategori
4. Kembali Ke Menu Utama 
Masukkan angka yang ingin dijalankan : '''))
            
            if inputValidasi == 1:
                
                if len(listStok) == 0: # Handle Database Kosong
                    print('''
==========================================
Dalam Database Belum Terdaftar Stok Apapun
Silahkan Masukkan Stok pada Database
==========================================
''') 
                else: 
                    print('''
===========================================
Berikut Merupakan Seluruh Isi dari Database
===========================================
                          ''')
                    tampilkanTableStok(listStok)
                    menuSortingData()
                    
                    
            elif inputValidasi == 2: # Data Spesifik
                tampilkanDataSpesifik()
                
            elif inputValidasi == 3 : 
                if len(listStok) == 0: # Handle Database Kosong
                    print('''
==========================================
Dalam Database Belum Terdaftar Stok Apapun
Silahkan Masukkan Stok pada Database
==========================================
''') 
                else :
                    tampilkanKategori()    
                
            elif inputValidasi == 4: #Balik Ke Menu Utama
                main_menu()
                
            else : #Handle Index Out of Bounds
                print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 3)
                Silahkan Coba lagi 
=======================================================
''')
    
            
        except ValueError: #handle input error
            print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 3)
                Silahkan Coba lagi 
=======================================================
''')        

def tampilkanTableStok(tableTampilkan):
    tableStok = tabulate(
                tableTampilkan, 
                headers=headers, 
                tablefmt="fancy_grid",
                colalign=("center", "center", "center", "center", "center","center","center")
            )
    print(tableStok)
    
def main_menu():
    while True:
        try :
            inputAksi = int(input('''

=============================================
Selamat Datang di Inventory Management System
=============================================
List Aksi:
1. Menampilkan Stok
2. Menambah Daftar Stok
3. Menghapus Stok
4. Mengubah Data Stok
5. Exit Program

Masukkan angka yang ingin dijalankan : '''
            ))
            
            if inputAksi == 1: # Read function
                menuMenampilkanStok()
            
            if inputAksi == 2: # Create Function
                menuMenambahStok()
                
            elif inputAksi == 3: # Delete Function
                menuHapusStok()
            
            elif inputAksi == 4: #Update Function
                menuUpdateStok()
            
            elif inputAksi == 5: # Keluar Program
                print('''
=========================================================
Terimakasih sudah menggunakan Sistem Sampai Jumpa Kembali
=========================================================
''')            
                sys.exit() #ngak pake break gara gara readability
                
            else : #Handle Index Out of Bounds
                print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 5)
                Silahkan Coba lagi 
=======================================================
''')
                
        except ValueError: #handle input error
            print(f'''
=======================================================
Input yang anda masukkan salah (bukan angka 1 sampai 5)
                Silahkan Coba lagi 
=======================================================
''')
            
listStok= [[1,"ID001", "Ayam Boiler", 20, "Ayam", 10000, 200000], 
           [2,"ID002", "Tahu Bacem", 15, "Tahu", 15000,225000], 
           [3,"ID003", "Kelapa Muda", 25, "Minuman", 20000, 500000],
           [4,"ID004", "Ayam Kampung", 20, "Ayam", 10000, 200000]]

idTerkahir = listStok[-1][1]

headers=["No","Id", "Nama", "Stok", "Kategori", "Harga Per Stok", "Harga Total"]

main_menu()
