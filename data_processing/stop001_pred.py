import csv
from matplotlib import pyplot as plt

data = []
info = []
with open('../predictions/lstm_pred_500101216.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i != 0:
            data.append(row)
        else:
            info.append(row)
        i += 1
print(data)    
data = list(filter(lambda x: x[0].split('_')[1] == "500101216", data[0]))
print(len(data))
data12 = list(filter(lambda x: x[0].split('_')[0][5] == "2", data))
print(len(data12))
ratio = []
for i in range(len(data12)):
    ratio.append(float(data12[i][1]))
print(ratio)
plt.plot(ratio, color='blue')
x = range(len(data12))
label = [data12[i][0].split('_')[0][4:] if i % 72 == 0 else '' for i in range(len(data12))]
# label = ['1204', '1205', '1206', '1207', '1208', '1209', '1210']
print(label)
plt.xticks(ticks=x, labels=label)
plt.savefig('../predictions/stop1216_pred.png')
data = info + data
with open('../predictions/stop1216_pred_lstm.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)