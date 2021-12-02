import csv
from datetime import datetime



filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #getting highs and lows from file
    highs,lows,dates = [], [], []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        dates.append(current_date)

    print(highs)
    print(lows)

from matplotlib import pyplot as plt

#plot data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates,highs, c = 'red')
plt.plot(dates,lows,c = 'blue')
plt.fill_between(dates,highs,lows,facecolor='purple',alpha=0.1)

#format plot
plt.title("Sitka Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis='both',which='major',labelsize=8)

plt.show()

