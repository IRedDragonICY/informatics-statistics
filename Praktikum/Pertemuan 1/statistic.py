# import math
import math
datas ="79 49 48 74 81 98 87 80 80 84 90 70 91 93 82 78 70 71 92 38 56 81 74 73 68 72 85 51 65 93 83 86 90 35 83 73 74 43 86 88 92 93 76 71 90 72 67 75 80 91 61 72 97 91 88 81 70 74 99 95 80 59 71 77 63 60 83 82 60 67 89 63 76 63 88 70 66 88 79 75"

data = datas.split(" ")
for i in range(len(data)):
    data[i] = int(data[i])
R = max(data) - min(data)
k = math.ceil(1 + 3.3 * math.log10(len(data)))
C = math.ceil(R / k)
print("R = ", R)
print("k = ", k)
print("C = ", C)

interval = []

for i in range(k):
    interval.append([min(data) + i * C, min(data) + (i + 1) * C])
frequency = [0] * k
for i in range(len(data)):
    for j in range(k):
        if interval[j][0] <= data[i] < interval[j][1]:
            frequency[j] += 1
            break
# mencari median dari kelas interval
median = 0
for i in range(k):
    median += frequency[i]
    if median > len(data) / 2:
        median = interval[i][0] + C * (len(data) / 2 - (median - frequency[i])) / frequency[i]
        break
# mencari frequency cummulative
frequencyCummulative = [0] * k
frequencyCummulative[0] = frequency[0]
for i in range(1, k):
    frequencyCummulative[i] = frequencyCummulative[i - 1] + frequency[i]
# mencari frequency relatif (Fr = Fi/n x 100%)
frequencyRelatif = [0] * k
for i in range(k):
    frequencyRelatif[i] = frequency[i] / len(data) * 100
#cetak tabel
print("Interval\t\tFrekuensi\t\tFr\t\tFc")
for i in range(k):
    print(interval[i][0], "-", interval[i][1], "\t\t", frequency[i], "\t\t", frequencyRelatif[i], "\t\t", frequencyCummulative[i], "%")


