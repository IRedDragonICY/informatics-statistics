import numpy as np
from scipy.stats import poisson
import math

# Misalkan waktu adalah 6 jam dan diperoleh hasil 3 kali pengujian.
# Jadi, lambda (rata-rata peristiwa dalam interval waktu tertentu) adalah 3 kali per 6 jam.
lambda_ = 3/6 

# Kita akan menghitung probabilitas untuk 2 dan 3 pengujian akurasinya tinggi.
x = np.arange(2,4)
# print nilai e
print(f'Nilai e: {math.e}')
# Menggunakan fungsi massa probabilitas (pmf) dari scipy untuk menghitung probabilitas.
prob = poisson.pmf(x, lambda_)

for i in range(len(x)):
    print(f'-------Step by Step Calculation for x={x[i]}-------')
    print(f'1. Using the Poisson PMF, we get the following equation:')
    print(f'P(X={x[i]}) = (e^(-lambda) * lambda^x) / x!')
    print(f'2. Substituting the values of lambda and x, we get:')
    print(f'P(X={x[i]}) = (e^(-{lambda_}) * {lambda_}^{x[i]}) / {x[i]}!')
    print(f'3. Simplifying the above expression, we get:')
    print(f'P(X={x[i]}) = ({math.exp(-lambda_)} * {lambda_**x[i]}) / {math.factorial(x[i])}')
    print(f'4. Calculating the above expression, we get:')
    print(f'P(X={x[i]}) = {prob[i]}')
    print('')

print(f'-------Final Results-------')
print(f'Peluang pengujian ke-2 akurasinya tinggi: {prob[0]}')
print(f'Peluang pengujian ke-2 dan ke-3 akurasinya tinggi: {prob[0]*prob[1]}')
