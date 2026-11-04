import sys
# 15 data inti dari soal Kelompok F + tepat 5 data tambahan.
data_nilai = [
    42, 55, 61, 68, 73, 79, 82, 87, 91, 64,
    58, 76, 84, 49, 95,
    59, 60, 78, 80, 100,
]


def kategori(nilai):
    """Mengembalikan kategori untuk satu nilai pada rentang 0 sampai 100."""
    if nilai < 60:
        return "RENDAH"
    elif nilai < 80:
        return "SEDANG"
    else:
        return "TINGGI"


def hitung_kategori(data):
    """Menghitung jumlah data di setiap kategori dan mengembalikan dictionary."""
    jumlah = {"RENDAH": 0, "SEDANG": 0, "TINGGI": 0}

    for nilai in data:
        status = kategori(nilai)
        jumlah[status] += 1

    return jumlah


def rata_rata(data):
    """Menghitung dan mengembalikan rata-rata dari sebuah list angka."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def tampilkan_hasil(data):
   
    print("\nHASIL KLASIFIKASI")

    for nomor, nilai in enumerate(data, start=1):
        status = kategori(nilai)
        print(f"{nomor:02d}. Nilai = {nilai:3d} -> {status}")

    jumlah = hitung_kategori(data)
    print("\nRINGKASAN")
    print(f"Total data       : {len(data)}")
    print(f"Jumlah RENDAH    : {jumlah['RENDAH']}")
    print(f"Jumlah SEDANG    : {jumlah['SEDANG']}")
    print(f"Jumlah TINGGI    : {jumlah['TINGGI']}")
    print(f"Rata-rata        : {rata_rata(data):.2f}")
    print(f"Nilai maksimum   : {max(data)}")
    print(f"Nilai minimum    : {min(data)}")


def jalankan_testing():
    """Membandingkan hasil function kategori dengan 8 hasil yang diharapkan."""
    test_cases = [
        ("Sedikit di bawah batas 60", 59, "RENDAH"),
        ("Tepat pada batas 60", 60, "SEDANG"),
        ("Sedikit di atas batas 60", 61, "SEDANG"),
        ("Sedikit di bawah batas 80", 79, "SEDANG"),
        ("Tepat pada batas 80", 80, "TINGGI"),
        ("Sedikit di atas batas 80", 81, "TINGGI"),
        ("Nilai rendah realistis", 42, "RENDAH"),
        ("Nilai tinggi realistis", 95, "TINGGI"),
    ]

    print("=" * 64)
    print("PENGUJIAN PROGRAM - KELOMPOK F")
    print("=" * 64)
    lulus = 0

    for nomor, (keterangan, nilai, expected) in enumerate(test_cases, start=1):
        actual = kategori(nilai)
        hasil = "PASS" if actual == expected else "FAIL"
        if hasil == "PASS":
            lulus += 1
        print(
            f"Test {nomor}: {keterangan} | input={nilai} | "
            f"expected={expected} | actual={actual} | {hasil}"
        )

    print("-" * 64)
    print(f"Hasil pengujian: {lulus}/{len(test_cases)} PASS")
    return lulus == len(test_cases)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sys.exit(0 if jalankan_testing() else 1)
    else:
        tampilkan_hasil(data_nilai)
