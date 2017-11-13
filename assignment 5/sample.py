import csv
import matplotlib.pyplot as plt
import pylab as pl

areaList= list()
priceList= list()

with open('sample.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        areaList.append(int(row["area"]))
        priceList.append(int(row["price"]))

print(max(areaList))
print(max(priceList))

pl.plot(areaList, priceList)
pl.show()