import csv
import time
import datetime

def preprocess_date(dateandtime):
    print(dateandtime)
    dateandtime = dateandtime.split('_')
    return dateandtime[0][:4] + '/' + dateandtime[0][4:6] + '/' + dateandtime[0][6:8] + ' ' + dateandtime[2]

# Read in the data from the CSV file
data = []
info = []
with open('dataset_o_csv/500101001.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i != 0:
            data.append(row)
        else:
            info.append(row)
        i += 1
# Sort the data by date
# str = "20231005_500101001_23:00"
# dateandtime = str.split('_')
# dateandtime = dateandtime[0][:4] + '/' + dateandtime[0][4:6] + '/' + dateandtime[0][6:8] + ' ' + dateandtime[2]
# print(dateandtime)
# t = time.strptime(dateandtime, "%Y/%m/%d %H:%M")
data.sort(key=lambda x: datetime.datetime.strptime(preprocess_date(x[11]), "%Y/%m/%d %H:%M"))
data = info + data

# Write the data to a new CSV file
with open('sorted.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
