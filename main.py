from matplotlib import pyplot as plt
from functions import makelist, plotList, correctFile, makeAverageList, plotWithError


a = makelist() # Assigns a variable 'a' to our 'makelist' function

plotList('North hemisphere', a, 'slateblue', 'year', 'temperature anomalies')
plt.savefig('A3part1.png') # Saves the figure as a png with the specified name (A3part2e.png)
plt.show() # Shows the graph plot from the data

correctFile('J:\Physics\Teaching\spa4601\Materials\Data.monthly_nh.txt', 'Data.monthly_nh.average.txt') # Corrects the data files into the format we require
correctFile('J:\Physics\Teaching\spa4601\Materials\Data.monthly_ns.txt', 'Data.monthly_ns.average.txt')
correctFile('J:\Physics\Teaching\spa4601\Materials\Data.monthly_sh.txt', 'Data.monthly_sh.average.txt')
correctFile('J:\Physics\Teaching\spa4601\Materials\Data.monthly_tropical.txt', 'Data.monthly_tropical.average.txt')


granularity = 48

nhlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_nh.average.txt', 1, 2, granularity) # The function 'makeAverageList' is run to create lists for the corrected files
plotList('Northern Hemisphere', nhlist, 'black', 'Year', 'Temperature Anomalies') # This plots the list that is created

nslist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_ns.average.txt', 1, 2, granularity) # The function 'makeAverageList' is run to create lists for the corrected files
plotList('Global Average', nslist, 'slateblue', 'Year', 'Temperature Anomalies') # This plots the list that is created

shlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_sh.average.txt', 1, 2, granularity) # The function 'makeAverageList' is run to create lists for the corrected files
plotList('Southern Hemisphere', shlist, 'red', 'Year', 'Temperature Anomalies') # This plots the list that is created

mtlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_tropical.average.txt', 1, 2, granularity) # The function 'makeAverageList' is run to create lists for the corrected files
plotList('Tropical', mtlist, 'green', 'Year', 'Temperature Anomalies') # This plots the list that is created

plt.savefig('A3part2a(4years).png') # Saves the figure as a png with the specified name (A3part2e.png)
plt.show() # Shows the graph plot from the data


granularity = 120

nhlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_nh.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 120 months is generated for the data set
plotList('Northern Hemisphere', nhlist, 'black', 'Year', 'Temperature Anomalies') # Plots the lists that are generated for the data set into a graph

nslist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_ns.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 120 months is generated for the data set
plotList('Global Average', nslist, 'slateblue', 'Year', 'Temperature Anomalies') # Plots the lists that are generated for the data set into a graph

shlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_sh.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 120 months is generated for the data set
plotList('Southern Hemisphere', shlist, 'red', 'Year', 'Temperature Anomalies') # Plots the lists that are generated for the data set into a graph

mtlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_tropical.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 120 months is generated for the data set
plotList('Tropical', mtlist, 'green', 'Year', 'Temperature Anomalies') # Plots the lists that are generated for the data set into a graph

plt.savefig('A3part2a(10years)') # Saves the figure as a png with the specified name (A3part2e.png)
plt.show() # Shows the graph plot from the data


granularity = 1

nhlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_nh.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 1 month is generated for the data set
plotList('Northern Hemisphere', nhlist, 'black', 'Year', 'Temperature Anomalies') # Plots the lists generated for the data set into a graph

nslist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_ns.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 1 month is generated for the data set
plotList('Global Average', nslist, 'slateblue', 'Year', 'Temperature Anomalies') # Plots the lists generated for the data set into a graph

shlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_sh.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 1 month is generated for the data set
plotList('Southern Hemisphere', shlist, 'red', 'Year', 'Temperature Anomalies') # Plots the lists generated for the data set into a graph

mtlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_tropical.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 1 month is generated for the data set
plotList('Tropical', mtlist, 'green', 'Year', 'Temperature Anomalies') # Plots the lists generated for the data set into a graph

plt.savefig('A3part2a(1month).png') # Saves the figure as a png with the specified name (A3part2e.png)
plt.show() # Shows the graph plot from the data


granularity = 12

nhlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_nh.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 12 months is generated for the data set
plotList('Northern Hemisphere', nhlist, 'black', 'Year', 'Temperature Anomalies')  # Plots the lists generated for the data set

nslist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_ns.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 12 months is generated for the data set
plotList('Global Average', nslist, 'slateblue', 'Year', 'Temperature Anomalies')  # Plots the lists generated for the data set

shlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_sh.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 12 months is generated for the data set
plotList('Southern Hemisphere', shlist, 'red', 'Year', 'Temperature Anomalies')  # Plots the lists generated for the data set

mtlist = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\Data.monthly_tropical.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 12 months is generated for the data set
plotList('Tropical', mtlist, 'green', 'Year', 'Temperature Anomalies')  # Plots the lists generated for the data set into a graph

plt.savefig('A3part2a(1year).png') # Saves the figure as a png with the specified name (A3part2e.png)
plt.show() # Shows the graph plot from the data


granularity = 48
XY = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_nh.average.txt', 1, 2, granularity)  # Lists are generated with a granularity of 48 months is generated for the data set
YU = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_nh.average.txt', 1, 9, granularity)
YL = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_nh.average.txt', 1, 10, granularity)
x = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_nh.average.txt', 3, 11, granularity)
y = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_nh.average.txt', 3, 12, granularity)

plotWithError('Northern Hemisphere', 'All uncertainty Type', XY, x, y, 'red', 'lightblue') # Plots the errors for 'Northern Hemisphere'
plotWithError('', 'uncertainty', XY, YU, YL, 'red', 'slateblue') # Plots the errors
plt.savefig('A3part2b.png') # Saves the figure as a png with the specified name (A3part2e.png)
plt.show() # Shows the graph plot from the data


XY = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_ns.average.txt', 1, 2, granularity) # Lists are generated with a granularity of 48 months is generated for the data set
YU = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_ns.average.txt', 1, 9, granularity)
YL = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_ns.average.txt', 1, 10, granularity)
x = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_ns.average.txt', 3, 11, granularity)
y = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_ns.average.txt', 3, 12, granularity)

plotWithError('Global Average', 'All uncertainty Type', XY, x, y, 'red', 'lightblue') # Plots the errors for 'Global Average' in specific
plotWithError('', 'uncertainty', XY, YU, YL, 'red', 'slateblue') # Plots the errors with 'uncertainty' in specific
plt.savefig('A3part2c.png') # Saves the figure as a png with the specified name (A3part2e.png)
plt.show() # Shows the graph plot from the data


XY = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_sh.average.txt', 1, 2, granularity)
YU = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_sh.average.txt', 1, 9, granularity)
YL = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_sh.average.txt', 1, 10, granularity)
x = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_sh.average.txt', 3, 11, granularity)
y = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_sh.average.txt', 3, 12, granularity)

plotWithError('Southern Hemisphere', 'All uncertainty Type', XY, x, y, 'red', 'lightblue') # Plots the errors for 'Southern Hemisphere' in specific
plotWithError('', 'uncertainty', XY, YU, YL, 'red', 'slateblue') # Plots the errors with 'uncertainty' in specific
plt.savefig('A3part2d.png') # Saves the figure as a png with the specified name (A3part2e.png)
plt.show() # Shows the graph plot from the data


XY = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_tropical.average.txt', 1, 2, granularity)
YU = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_tropical.average.txt', 1, 9, granularity)
YL = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_tropical.average.txt', 1, 10, granularity)
x = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_tropical.average.txt', 3, 11, granularity)
y = makeAverageList('C:\\Users\\ap17064\SPA4601\PyCharmProjects\AKA_Project\A3\\Data.monthly_tropical.average.txt', 3, 12, granularity)

plotWithError('Tropical', 'All uncertainty Type', XY, x, y, 'red', 'lightblue')  # Plots the errors for 'Tropical' in specific
plotWithError('', 'uncertainty', XY, YU, YL, 'red', 'slateblue')  # Plots the errors for 'uncertainty' in specific
plt.savefig('A3part2e.png') # Saves the figure as a png with the specified name '(A3part2e.png)'
plt.show() # Shows the graph plot from the data

