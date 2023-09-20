from matplotlib import pyplot as plt


def makelist(fullpath='J:\\Physics\\Teaching\\spa4601\\Materials\\Data.nh.txt'):
    data = []
    fr = open(fullpath, 'r')
    for i in fr.readlines():
        p = i.split()
        x = int(p[0])
        y = float(p[1])
        tup = (x, y)
        data.append(tup)
    return data


def plotList(plots, data, colour, xT, yT):
    x = []
    y = []
    for i in data:
        print(i)
        x.append(i[0])
        y.append(i[1])
    plt.xlabel(xT)
    plt.ylabel(yT)
    plt.plot(x, y, color=colour, label=plots)
    plt.legend()


def correctFile(inputname, outputname):
    fi = open(inputname, 'r')
    fo = open(outputname, 'w')

    for i in fi.readlines():
        data = i.split('   ')
        time = data[0]
        time = time.split('/')
        year = time[0]
        month_number = int(time[1])
        month = '{:0.2f}'
        month = month.format(float(month_number/12))
        raw_Date_And_Month = int(year) + float(month)
        rounded_Date_And_Month = '{:.2f}'
        rounded_Date_And_Month = rounded_Date_And_Month.format(raw_Date_And_Month)
        fo.write(year)
        fo.write(',')
        fo.write(rounded_Date_And_Month)
        for n in range(11):
            m = n + 1
            fo.write(',')
            fo.write(data[m])


def makeAverageList(inputFile, xc=1, yc=2, som=3):
    f = open(inputFile, 'r')
    xint = []
    yint = []
    for i in f.readlines():
        data = i.split(',')
        xint.append(data[xc])
        yint.append(data[yc])
    ax = []
    ay = []
    lx = len(xint)
    ly = len(yint)
    cm = 0
    for f in range(lx):
        cm = cm + float(xint[f])
        if (f+1) % som == 0:
            ax.append(cm/som)
            cm = 0
    cm = 0
    for f in range(ly):
        cm = cm + float(yint[f])
        if (f+1) % som == 0:
            ay.append(cm/som)
            cm = 0
    tuple_average = list(zip(ax, ay))
    return tuple_average


def plotWithError(PlotName, uncertaintyType, Txy, TerrorUpper, TerrorLower, colourCentral = "green", colourError = "red", xTitle = "Year", yTitle = "Temperature"):
    if len(Txy) == len(TerrorLower) and len(Txy) == len(TerrorUpper):
        pass
    else:
        print("Error: Length of three lists not the same")
        exit(0)
    x = []
    y = []
    for elem in Txy:
        x.append(elem[0])
        y.append(elem[1])
    yUpper = []
    yLower = []
    for elem in TerrorUpper:
        yUpper.append(elem[1])
    for elem in TerrorLower:
        yLower.append(elem[1])
    plt.fill_between(x, yLower, yUpper, color=colourError, label=uncertaintyType)
    plt.plot(x, y, color=colourCentral, label=PlotName)
    plt.legend()
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)

