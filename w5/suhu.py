# Program Konversi Suhu

print("=== Program Konversi Suhu ===")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")
print("3. Celsius ke Kelvin")
print("4. Kelvin ke Celsius")

pilihan = input("Pilih menu (1/2/3/4): ")

if pilihan == "1":
    c = float(input("Masukkan suhu Celsius: "))
    f = (c * 9/5) + 32
    print(f"Hasil: {c}°C = {f}°F")

elif pilihan == "2":
    f = float(input("Masukkan suhu Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"Hasil: {f}°F = {c}°C")

elif pilihan == "3":
    c = float(input("Masukkan suhu Celsius: "))
    k = c + 273.15
    print(f"Hasil: {c}°C = {k} K")

elif pilihan == "4":
    k = float(input("Masukkan suhu Kelvin: "))
    c = k - 273.15
    print(f"Hasil: {k} K = {c}°C")

else:
    print("Pilihan tidak valid!")