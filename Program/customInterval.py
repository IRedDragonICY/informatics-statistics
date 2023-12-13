import math

intervalClass =["5-10","11-16","17-22","23-28","29-34","35-40","41-46"]
freq = [10,8,7,15,5,5,5]

intervals = [[int(j) for j in i.split('-')] for i in intervalClass]
 
midpoints = [(i[0] + i[1]) / 2 for i in intervals]
print("Midpoints: ", midpoints)

cumulative_freq = [sum(freq[:i+1]) for i in range(len(freq))]
print("Cumulative Frequency: ", cumulative_freq)

N = sum(freq)
print("Total Frequency (N): ", N)


quartiles = []
print ("Qn = L + (((n/4) - F)/f)*c")
for q in [1/4 , 2/4 , 3/4]: 
    pos_q= q*N 
    
    idx_q=[i for i,freq_cum in enumerate(cumulative_freq) if freq_cum>=pos_q][0]
    
    L=intervals[idx_q][0] 
    f=freq[idx_q] 
    
    if idx_q==0:
        F=0
    else:
        F=cumulative_freq[idx_q - 1] 
    
    c=intervals[idx_q][1]-L 
    print (f"Q{len(quartiles)+1} = {L} + ((({pos_q}) - {F})/{f})*{c}")
    q_val=L+(((pos_q-F)/f)*c)
    
    print(f"Quartile {len(quartiles)+1} Value: ", q_val)
    
# Menggunakan fungsi max() untuk menemukan frekuensi tertinggi
max_freq = max(freq)

# Mencari indeks dari frekuensi tertinggi
mode_index = freq.index(max_freq)

# Mendapatkan interval kelas dari modus
mode_class = intervals[mode_index]

L1 = mode_class[0]  # batas bawah kelas modus
fm = max_freq  # frekuensi kelas modus

# Mencari frekuensi sebelum dan sesudah kelas modus
if mode_index != 0:
    f1 = freq[mode_index - 1]
else:
    f1 = 0

if mode_index != len(freq) - 1:
    f2 = freq[mode_index + 1]
else:
    f2 = 0

c = mode_class[1] - L1 # lebar interval kelas

# Menggunakan rumus estimasi untuk menghitung modus dalam data kelompok
modus_estimate= L1 + ((fm - f1) / ((fm - f1) + (fm - f2))) * c 

print(f"Modus: {modus_estimate}")
