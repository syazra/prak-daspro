import random

game_title = "🎁 CHOOSE THE BOX 🎁"
welcome_message = "WELCOME!"

right_answer = random.randint(1, 5)

print("--------------------------------")
print(f"----- {game_title} -----")
print(f"----------- {welcome_message} -----------")
print("--------------------------------\n")

nama_user = input("Masukkan nama anda: ")
print(f"Halo {nama_user}!")

print('''
Silakan pilih salah satu kotak di bawah ini.
Jika beruntung, kamu akan mendapatkan hadiah besar!
[1]  [2]  [3]  [4]  [5]
''')

try:
    pilihan_user = int(input("Masukkan pilihan anda (1/2/3/4/5): "))
    if pilihan_user < 1 or pilihan_user > 5:
        print("Pilihan harus antara 1 sampai 5.")
        exit()
except ValueError:
    print("Input harus berupa angka.")
    exit()

print(f"Apakah kamu yakin hadiah ada di kotak nomor {pilihan_user}?")
jawaban_user = input("y/n: ").lower()

if jawaban_user == "y": 
    if pilihan_user == right_answer:
        print("\n🎉 SELAMAT! Anda mendapatkan 1 mobil Porsche! 🎉")
    else:
        print(f"\n😢 Maaf, Anda belum beruntung. Hadiah ada di kotak nomor {right_answer}.")
elif jawaban_user == "n":
    print("Program dihentikan. Silakan coba lagi kapan-kapan.")
else:
    print("Input tidak valid. Silakan ulangi game ini.")