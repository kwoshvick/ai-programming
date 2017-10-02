import matplotlib.pyplot as plt
import math
import random

daysInMonths = {
    'January' :31,
    'February' :28,
    'March' :31,
    'April' :30,
    'May' :31,
    'June' :30,
    'July' :31,
    'August' :31,
    'September' :30,
    'October' :31,
    'November' :30,
    'December' :31
}

monthlyTemperature = {}
meanMonthlyTemperature = {}

for month, days in daysInMonths.items():
    monthlyTemperature[month] = random.sample(range(-4,55),days)
    meanMonthlyTemperature[month] = sum(monthlyTemperature[month]) / days



variances = {}

for month,mean in meanMonthlyTemperature.items():
    varianceList = list()
    for days in monthlyTemperature[month]:
        varianceList.append(((mean - days) ** 2))

    variances[month] = sum(varianceList)


sd = {}
for month,variance in variances.items():
    sd[month] = math.sqrt(variance / daysInMonths[month])

# print(sd)
# print(list(sd.keys()))
# x, y = zip(*sd) # unpack a list of pairs into two tuples

plt.plot(list(sd.keys()),list(sd.values()))
plt.show()

