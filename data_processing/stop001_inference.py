import csv

data = []
info = []
with open('../inference_csv/inf_1211_to_1217.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i != 0:
            data.append(row)
        else:
            info.append(row)
        i += 1
# print(data)    
data = list(filter(lambda x: x[5] == "25.02605", data))
# print(data)
data = info + data
with open('../inference_o_csv/stop001_inf_1211_to_1217.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)