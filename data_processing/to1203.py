import csv

data = []
info = []
with open('../LSTM_dataset/filled_csv_full.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i != 0:
            data.append(row)
        else:
            info.append(row)
        i += 1
 
data = list(filter(lambda x: x[0] != "12" or (x[0] == "12" and int(x[1]) <= 3), data))
# data.sort(key=lambda x: int(x[-2].split('_')[1]))

data = info + data
with open('../LSTM_dataset/filled_csv_to1203.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)