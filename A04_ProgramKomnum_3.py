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
