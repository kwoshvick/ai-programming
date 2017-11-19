import csv
import matplotlib.pyplot as plt
import numpy as np



def readCSV(name):
    areaList = list()
    priceList = list()
    with open(name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            areaList.append(float(row["LotArea"])/100000)
            priceList.append(float(row["SalePrice"])/100000)
    return areaList,priceList



def linearRegression(areaList,priceList):
    fit_points = np.polyfit(areaList, priceList, 1)
    return fit_points


def myloop(iteration,new_x,new_c,areaList,priceList):
    counter = 0
    while counter < iteration:
        new_x, new_c =  gradientDescent(new_x, new_c, areaList, priceList)
        counter += 1
    plot(new_x,new_c,areaList,priceList)


def gradientDescent(x,c,areaList,priceList):
    fit_function = np.poly1d([x,c])
    predicted_price = fit_function(areaList)
    e = list()
    for i in range(0,len(predicted_price)):
        t = priceList[i] - predicted_price[i]
        t_2 = t ** 2
        e.append(t_2)

    sse = sum(e) * 0.5

    print('-----',sse)

    a = list()
    b = list()

    for i in range(0,len(priceList)):
        a1 = -(float(priceList[i])-float(predicted_price[i]))
        b1 = -(priceList[i]-predicted_price[i])*areaList[i]
        a.append(a1)
        b.append(b1)


    new_x = x - 0.01 * sum(b)
    new_c = c - 0.01 * sum(a)

    return new_x,new_c


def plot(x,c,areaList,priceList):
    print(x,c)
    fit_function = np.poly1d([x,c])
    plt.scatter(areaList, priceList)
    plt.plot(areaList, priceList, 'yo', areaList, fit_function(areaList), '--k')
    plt.show()


if __name__ =='__main__':
    areaList, priceList = readCSV('train.csv')
    x,c = linearRegression(areaList,priceList)
    new_x, new_c = gradientDescent(x,c,areaList,priceList,)
    myloop(10,new_x,new_c,areaList,priceList)

