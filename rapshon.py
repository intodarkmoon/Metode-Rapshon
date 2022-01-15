nilx = float(input("Masukkan nilai x = "))
nilxr = float(input("Masukkan nilai xr = "))

# Menuju rumus
hasil = nilxr - (nilxr ** 3 + 2 * nilxr ** 2 + 10 * nilxr - 20) / (3 * nilxr ** 2 + 4 * nilxr + 10)
print(f"Hasil dari X ke {nilx} = ", hasil)
print("=========================================")
hasil2 = abs(hasil - nilxr)
e = 0.00001
print("Hasil dari xr + 1 - xr = ", hasil2)
print("==================================")
if hasil2 < e:
    print("Sudah lebih keci dari epsilon")
else:
    print("Belum lebih kecil dari epsilon")
