
data = "80 85 78 90 88 80 85 80 85 9085 90 85 80 80 87 85 80 90 90 90 87 80 75 80"

data_splitted = [data[i:i+2] for i in range(0, len(data), 2)]
print("Total data: ", len(data_splitted))
for i in range(len(data_splitted)):
    print(data_splitted[i], end=" ")
