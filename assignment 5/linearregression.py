import csv
import matplotlib.pyplot as plt

areaList= list()
priceList= list()

with open('train.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        areaList.append(int(row["LotArea"]))
        priceList.append(int(row["SalePrice"]))

print(max(areaList))
print(max(priceList))

plt.plot(areaList, priceList, 'ro')
plt.show()