import math
import pandas as pd

data = "20 35 37 40 40 38 33 25 35 32 15 25 25 24 30 19 35 27 29 32 34 50 23 20 56 33 26 20 16 29 40 36 47 40 30 20 23 42 33 28 35 63 47 69 22 40 59 42 35 32"

if " " in data:
    data = data.split(" ")
elif "," in data:
    data = data.split(",")
elif " " in data:
    data = data.split(" ")

data = [int(i) for i in data]
data.sort()
max = max(data)
min = min(data)
R= max - min
k = math.ceil(1+3.332*math.log10(len(data)))
# memaksakan pembulatan ke atas
C = math.ceil(R/k)

# print ("mean = ",sum(data),"/",len(data)," = ",sum(data)/len(data))

# mencari median
if len(data)%2 == 0:
    median = (data[int(len(data)/2)]+data[int(len(data)/2)-1])/2
else:
    median = data[int(len(data)/2)] 



# membuat kelas
classInterval = []
for i in range(k):
    if i == 0:
        classInterval.append([min,min+C])
    else:
        classInterval.append([classInterval[i-1][1],classInterval[i-1][1]+C])

# mencari frekuensi
frequency = []
for i in range(k):
    frequency.append(0)
for i in data:
    for j in range(k):
        if i >= classInterval[j][0] and i <= classInterval[j][1]:
            frequency[j] += 1
            break

# mencari frekuensi kumulatif
cumulativeFrequency = []
for i in range(k):
    if i == 0:
        cumulativeFrequency.append(frequency[i])
    else:
        cumulativeFrequency.append(frequency[i]+cumulativeFrequency[i-1])
# mencari  Xi
Xi = []
for i in range(k):
    Xi.append((classInterval[i][0]+classInterval[i][1])/2)

FiXi = []
for i in range(k):
    FiXi.append(frequency[i]*Xi[i])




# Fr
Fr = []
for i in range(k):
    Fr.append(frequency[i]/len(data))

mean = sum(FiXi)/len(data)

# data yang sudah diurutkan
print ("Data yang sudah diurutkan:")
print (data)
print ("R = ",max," - ",min," = ",R)
print ("k = math.ceil(",1,"+3.332*math.log10(",len(data),")) = ",k)
print ("C = math.ceil(",R,"/",k,") = ",C)
print ("Mean = ",sum(FiXi),"/",len(data)," = ",mean)
print ("Mean = ",sum(data),"/",len(data)," = ",sum(data)/len(data))
if len(data)%2 == 0:
    print ("Median = (",data[int(len(data)/2)]," + ",data[int(len(data)/2)-1],")/ 2 = ",median)
else:
    print ("Median = ",data[int(len(data)/2)])

# Membuat DataFrame
df = pd.DataFrame({
    'Class Interval': [f'{c[0]} - {c[1]}' for c in classInterval],
    'Frequency': frequency,
    'Cumulative Frequency': cumulativeFrequency,
    'Xi': Xi,
    'FiXi': FiXi,
    'Fr': [f'{round(f*100,2)}%' for f in Fr],
})
# sigma
df.loc['sigma'] = ['', sum(frequency), '','',sum(FiXi), '']
print(df)