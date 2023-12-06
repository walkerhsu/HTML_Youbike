import csv
import os
from datetime import datetime

def preprocess_date(dateandtime):
    dateandtime = dateandtime.split('_')
    return dateandtime[0][:4] + '/' + dateandtime[0][4:6] + '/' + dateandtime[0][6:8] + ' ' + dateandtime[2]

def next_time(hr_min):
    hr_min = hr_min.split(':')
    hr = int(hr_min[0])
    min = int(hr_min[1])
    if min == 40:
        min = 0
        if hr == 23:
            hr = 0
        else:
            hr += 1
    else:
        min += 20
    if hr < 10:
        hr = '0' + str(hr)
    if min < 10:
        min = '0' + str(min)
    next_hr_min = str(hr) + ':' + str(min)
    return next_hr_min

def concat_data(directory):
    data = []
    info = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            with open(directory + '/' + filename, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                i = 0
                for row in reader:
                    if i != 0:
                        data.append(row)
                    else:
                        info.append(row)
                    i += 1
                    
    return data, info

data, info = concat_data('../output/lstm+mse_v2')
# print(data[0])
print(info[0])

complete_data = []
hr_min = '00:00'

flag = True

data.sort(key=lambda x: datetime.strptime(preprocess_date(x[0]), "%Y/%m/%d %H:%M"))
data.sort(key=lambda x: x[0].split('_')[1])
data.insert(0, info[0])

with open('../predictions/prediction_rnn.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in data:
        writer.writerow(row)



