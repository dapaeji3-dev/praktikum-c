# Program Menghitung Rata-rata

print("=== Program Hitung Rata-rata ===")

jumlah_data = int(input("Masukkan jumlah data: "))

total = 0

for i in range(jumlah_data):
    angka = float(input(f"Masukkan data ke-{i+1}: "))
    total += angka

rata_rata = total / jumlah_data

print(f"Total nilai = {total}")
print(f"Rata-rata = {rata_rata}")