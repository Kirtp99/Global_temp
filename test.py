from matplotlib import pyplot as plt
from functions import makelist, plotList, correctFile, makeAverageList, plotWithError

a = makelist() # Assigns a label 'a' for the makelist function
print(a)
plotList('t', a, 'black', 'x', 'y') # 'plotList' function is used to test certain parameters
plt.savefig('testA.png')
plt.show()

correctFile('J:\Physics\Teaching\spa4601\Materials\Data.monthly_nh.txt', 'test_data_nh.average.txt')


granularity = 48 # Granularity of 48 months (4 years)
test1 = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\test_data_nh.average.txt', 1, 2, granularity)
granularity = 12 # Ganularity of 12 months (1 year)
test2 = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\test_data_nh.average.txt', 1, 2, granularity)
granularity = 1 # Granularity of 1 month
test3 = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\test_data_nh.average.txt', 1, 2, granularity)
plotList('4years', test1, 'red', 'Year', 'Temperature Anomalies')
plotList('1 year', test2, 'black', 'Year', 'Temperature Anomalies')
plotList('1 months', test3, 'green', 'Year', 'Temperature Anomalies')
plt.show()

XY = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\test_data_nh.average.txt', 1, 2, 12)
YU = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\test_data_nh.average.txt', 1, 9, 12)
YL = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\test_data_nh.average.txt', 1, 10, 12)

plotWithError('ErrorTest', 'uncertaintyType', XY, YU, YL)
plt.show()
