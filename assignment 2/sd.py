import math
import random
import matplotlib.pyplot as plt
from collections import OrderedDict

daysInMonths = OrderedDict([
    ('January' ,31),
    ('February' ,28),
    ('March' ,31),
    ('April' ,30),
    ('May' ,31),
    ('June' ,30),
    ('July' ,31),
    ('August' ,31),
    ('September' ,30),
    ('October' ,31),
    ('November' ,30),
    ('December' ,31)
])

monthlyTemperature = OrderedDict()
meanMonthlyTemperature = OrderedDict()

for month, days in daysInMonths.items():
    monthlyTemperature[month] = random.sample(range(-4,55),days)
    meanMonthlyTemperature[month] = sum(monthlyTemperature[month]) / days


variances = OrderedDict()

for month,mean in meanMonthlyTemperature.items():
    varianceList = list()
    for days in monthlyTemperature[month]:
        varianceList.append(((mean - days) ** 2))

    variances[month] = sum(varianceList)


sd = OrderedDict({})
for month,variance in variances.items():
    sd[month] = math.sqrt(variance / daysInMonths[month])


colors = ("red", "green", "blue")

months = [1,2,3,4,5,6,7,8,9,10,11,12]

plt.scatter(months ,list(sd.values()),  c=colors)
plt.title('Scatter plot of standard deviation of temperature ')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.show()


