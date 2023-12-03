import csv
import os
import datetime

def preprocess_date(dateandtime):
    print(dateandtime)
    dateandtime = dateandtime.split('_')
    return dateandtime[0][:4] + '/' + dateandtime[0][4:6] + '/' + dateandtime[0][6:8] + ' ' + dateandtime[2]

def next_time(hr, min):
    if min == 40:
        min = 0
        if hr == 23:
            hr = 0
        else:
            hr += 1
    else:
        min += 20
    return [hr, min]

def filldata(data):
    # print(data)
    for i in range(len(data)):
        # print(len(data))
        row = data[i]
        nextrow = data[i + 1]
        hr = int(row[3])
        min = int(row[4])
        while nextrow[2] != row[2] and [nextrow[3], nextrow[4]] != next_time(hr, min) and [hr, min] != [23, 40]:
            # find last day data
            month = int(row[0])
            date = int(row[1])
            hr = next_time(hr, min)[0]
            min = next_time(hr, min)[1]
            # print(month, date, hr, min)
            flag = True
            while(flag):
                lastday = list(filter(lambda x:  x[0] == month and x[1] == date - 1 and x[3] == hr and x[4] == min, data))
                flag = lastday == [] or lastday == None
                date -= 1
            
            # print(lastday[0])
            filldate = [row[0], row[1], row[2], hr, min, row[5], row[6], row[7], lastday[0][8], lastday[0][9], row[10], row[11], lastday[0][11]]
            # print(filldate)
            data.insert(i + 1, filldate)
            i+=1
            nextrow = data[i + 1]
            # print(nextrow)
            # print([nextrow[3], nextrow[4]], next_time(hr, min) , hr , min)
    for j in range(3820, 3863):
        row = data[j]
        data.append([row[0], row[1]+1, row[2]+1, row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]])
        
def sortbydate(data):      
    data.sort(key=lambda x: datetime.datetime.strptime(preprocess_date(x[11]), "%Y/%m/%d %H:%M"))
        
data = []
info = []

directory = 'dataset_o_csv'
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(file):
        print('filename: ')
        print(file)
        with open(file, 'r') as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                if i != 0:
                    data.append([int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), float(row[5]), float(row[6]), int(row[7]), float(row[8]), int(row[9]), int(row[10]), row[11], row[12]])
                else:
                    info.append(row)
                i += 1
        
        sortbydate(data)
        filldata(data)
        
        data = info + data
        file = file.split('/')
        # os.mkdir('dataset_filled')
        with open('dataset_filled/' + file[1], 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            
        data = []
        info = []