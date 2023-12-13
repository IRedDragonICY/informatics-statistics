import scipy.stats as stats
import collections
import numpy as np

data = [16, 32, 34, 28, 30, 35, 29, 50, 33, 63, 37, 27, 23, 42, 47, 42, 35, 20, 23, 69, 40, 25, 56, 19, 22, 38, 30, 33, 30, 40, 33, 24, 26, 41, 59, 35, 25, 21, 45, 42, 30, 25, 31, 36, 33, 35, 18, 29, 45, 30]

# total data
print ("Total data: ", len(data))

# mengurutkan data
data.sort()

# data setelah diurutkan
print ("Data setelah diurutkan: ", data)

# Menghitung rata-rata
mean = stats.tmean(data)
print("Mean = Σ(xi)/N")
print ("Mean = ",sum(data),"/",len(data),"=",mean)
print ("Mean: ", mean)

# Menghitung Variansi dengan metode sampel (N-1)
variance_sample = stats.tvar(data)
print("Sample Variance = Σ((xi - mean)²)/(N - 1)")
print("Sample Variance = ",sum([(x - mean) ** 2 for x in data]),"/",len(data)-1,"=",variance_sample)
print("Sample Variance: ", variance_sample)

# Menghitung Standar Deviasi dengan metode sampel (N-1)
std_dev_sample = stats.tstd(data)
print("Sample Standard Deviation = √(Σ((xi - mean)²)/(N - 1))")
print("Sample Standard Deviation: ", std_dev_sample)


# menghitung quartile 1 2 3 dan 4
print("Quartile 1: ", np.percentile(data, 25))
print("Quartile 2: ", np.percentile(data, 50))
print("Quartile 3: ", np.percentile(data, 75))

# modus
print("Modus: ", stats.mode(data))

# Menghitung frekuensi dari setiap nilai dalam data
freq_data = collections.Counter(data)



# Membuat Tabel dengan Frekuensi
diff_list=[]
diff_square_list=[]
fx_diff_list=[]
fx_diff_square_list=[]
print("\033[1m{:<10}|{:<10}|{:<10}|{:<15}|{:<10}|{:<15}\033[0m".format("Value","Freq","(xi-mean)","f*(xi-mean)","(xi-mean)²","f*(xi-mean)²"))
print('-' * 86)  # print line of dashes
for x in freq_data:
    diff = round(x - mean, 3)
    diff_square=round(diff ** 2,3 )
    fx_diff = round(freq_data[x] * diff, 3)
    fx_diff_square = round(freq_data[x] * diff_square, 3)
    print("{:<10}|{:<10}|{:<10}|{:<15}|{:<10}|{:<15}".format(x, freq_data[x], diff, fx_diff, diff_square, fx_diff_square))
    diff_list.append(abs(diff)*freq_data[x])
    diff_square_list.append(diff_square*freq_data[x])
    fx_diff_list.append(fx_diff)
    fx_diff_square_list.append(fx_diff_square)

print('-' * 86)  # print line of dashes
# total sum
print("{:<10}|{:<10}|{:<10}|{:<15.3f}|{:<10}|{:<15.3f}".format("Σ","","",sum(diff_list),"",sum(fx_diff_square_list)))

