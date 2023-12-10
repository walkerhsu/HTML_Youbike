import csv
import numpy as np

data = []
info = []
stop = []
def standardize(data):
    print("in")
    print(np.mean(data))
    print(np.std(data))
    standard = []
    for d in data:
        # print((d - np.mean(data))/np.std(data))
        standard.append((d - np.mean(data))/np.std(data))
    return standard

with open('../inference_o_csv/allstops_inf_1021_to_1024.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i != 0:
            stop.append(row)
        else:
            info.append(row)
        i += 1
        
with open('../LSTM_dataset/filled_csv_to1203.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i != 0:
            data.append(row)
        i += 1
lat = []
lng = []
for i in range(112):
    lat.append(float(stop[i][5]))
    lng.append(float(stop[i][6]))
  
print(lat)
lat = standardize(np.array(lat))
lng = standardize(np.array(lng))

print(lat)

for i in range(0,len(data),55*72):
    data[i][5] = lat[i]
    data[i][6] = lng[i]

# data = list(filter(lambda x: x[0] != "12" or (x[0] == "12" and int(x[1]) <= 3), data))

data = info + data
with open('../LSTM_dataset/standard_to1203.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)