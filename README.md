# Laporan Tugas Program Komputasi Numerik - A04

</div>

### Anggota Kelompok

- Raynald Ramadhani Fachriansyah (5025241020)

- Ferdian Ardra Hafizhan (5025241033)

- Reza Afzaal Faizullah Taqy (5025241051)

- Muhammad Hilbran Akmal Abrar (5025241052)

- Ary Pasya Fernanda (5025241053)

## Soal

<img width="550" alt="soal" src="https://github.com/user-attachments/assets/1bce36c5-203b-4819-af0b-2ff2dc8324ff" />


### Code

```py
def f(x):
    return x**3 + 10*x**2 - 7*x - 196

def posisi_salah(a, b, xr_true, min_error = 0, max_error = 1, max_iter=100):
    if f(a) * f(b) >= 0:
        return None

    for i in range(max_iter):
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        fxr = f(xr)

        if i == 0:
            error_true = None
        else:
            error_true = abs((xr - xr_true) / xr)

        if error_true is not None:
            print(f"Iterasi {i}: a={a:.2f}, b={b:.2f}, xr={xr:.2f}, f(xr)={fxr:.2f}, error_true={error_true:.2f}")
        else:
            print(f"Iterasi {i}: a={a:.2f}, b={b:.2f}, xr={xr:.2f}, f(xr)={fxr:.2f}, error_true= N/A")

        if error_true is not None and min_error <= error_true < max_error:
            return xr

        if f(a) * fxr < 0:
            b = xr
        else:
            a = xr

    return xr

a = -5
b = 8
xr_true = 4
result = posisi_salah(a, b, xr_true)
if result is not None:
    print(f"Akar yang ditemukan: {result:.2f}")
```

### Penjelasan

# Metode Posisi Salah

Program ini menggunakan **metode posisi salah** untuk mencari akar dari fungsi non-linear. Metode ini merupakan metode numerik berbasis **interpolasi linear**.

---

## Fungsi Utama

```python
def f(x):
    return x**3 + 10*x**2 - 7*x - 196
```

### Penjelasan:

Fungsi `f(x)` yang ingin dicari akarnya:
\[
f(x) = x^3 + 10x^2 - 7x - 196
\]

---

## Fungsi Metode Posisi Salah

```python
def posisi_salah(a, b, xr_true, min_error = 0, max_error = 1, max_iter=100):
```

### Parameter:

- `a`, `b`: Tebakan awal (interval `[a, b]`)
- `xr_true`: Akar sebenarnya (untuk menghitung error relatif)
- `min_error`: Batas bawah error
- `max_error`: Batas atas error (default `1`)
- `max_iter`: Iterasi maksimum (default `100`)

---

### Proses Utama:

```python
if f(a) * f(b) >= 0:
    return None
```

Cek apakah `f(a)` dan `f(b)` memiliki tanda berbeda. Kalau tidak, akar belum tentu ada di interval tersebut.

---

```python
xr = b - (f(b) * (a - b)) / (f(a) - f(b))
```

Menghitung pendekatan akar menggunakan rumus posisi salah.

---

```python
error_true = abs((xr - xr_true) / xr)
```

Menghitung error relatif terhadap akar sebenarnya.

---

```python
if f(a) * fxr < 0:
    b = xr
else:
    a = xr
```

Update interval berdasarkan tanda dari `f(xr)`.

---

## Menjalankan Program

```python
a = -5
b = 8
xr_true = 4
result = posisi_salah(a, b, xr_true)
```

Menjalankan fungsi dengan interval awal `[-5, 8]` dan akar sebenarnya `4`.

---

## Output

<img width="506" alt="output" src="https://github.com/user-attachments/assets/01c1bb65-376a-4841-9b1f-71483d9e3926" />

---
