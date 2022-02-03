# NOTE Umum
# di python penulisan variabel sangat mudah tanpa harus
# mendeklarasikan tipe data terlebih dahulu kek C
# C-ways            --> int x = 10;
# Python-ways       --> x = 10

# ====================================================== #
# TODO ini tipe-data integer dan float (Numbers)
a = 10
x = 5.0
panjang = 100

print('Contoh print Numbers:')
print(panjang)
print(panjang + a)
# Kalo integer + float --> hasilnya float
print(a + x) 
# ====================================================== #



# ====================================================== #
# TODO ini tipe-data boolean (Bool)
benar = True
salah = False

print('\nContoh print Boolean:')
print(benar)
print(salah)
# ====================================================== #



# NOTE Strings
# di python deklarasi strings sangat mudah tanpa harus
# set size dari isi strings kek C yang tidak mengenal strings
# di C mengenal huruf (char) bukan kata/kalimat (strings)
# C-ways            --> char string[20] = "Hello World";
#                   --> char string[] = "Hello World";
#                   --> char string* = "Hello World";
# Python-ways       --> string = "Halo nama saya Anton"

# ====================================================== #
# TODO ini tipe-data string dan char (Strings)
nama = "Anton"
huruf = 'c'

print('\nContoh print Strings:')
print(nama)
print('Nama saya adalah ' + nama)
print(nama + ' + ' + huruf)
# ====================================================== #



# NOTE List
# karena di python gaada Array (harus import lib Array)
# Jadi ada namanya tipe-data List yang mirip array tapi bisa diisi
# berbagai tipe-data didalamnya
# C-ways            --> int x = [1,2,3];            (gaboleh diisi selain int)
# Python-ways       --> x = [1,2.0,"mantap",True]   (boleh dicampur)

# ====================================================== #
# TODO ini tipe-data list (List)
ini_list=[1,2.0,"mantap",True]

print('\nContoh print List')
print(ini_list)
# Kebetulan index ke-2 adalah string, jadi bisa langsung digabung
print('print index ke-3: ' + ini_list[2])
# ====================================================== #


# NOTE Tuple
# Nah bedanya dengan tipe-data List, Tuple ini bersifat Immutable
# dengan kata lain Tuple ini gabisa diubah valuenya (ditambah, dikurangi, dll)
# Tuple ->  static | List -> dynamic
# ====================================================== #
# TODO ini tipe-data tuple (Tuple)
ini_tuple=(1,2,'nais','tuple')

print('\nContoh print Tuple')
print(ini_tuple)
# Kebetulan index ke-2 adalah string, jadi bisa langsung digabung
print('print index ke-3: ' + ini_tuple[2])
# ====================================================== #