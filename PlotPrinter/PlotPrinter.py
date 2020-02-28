import pylab
from math import *

def plotChart(formula, minX, maxX):
    formula = formula.replace("y=","")
    xValues = pylab.arange(minX, maxX + (maxX - minX) / 5000, (maxX - minX) / 5000)
    yValues = []

    for i in range(0, len(xValues)):
        x = xValues[i]
        try:
            yValues.append(eval(formula))
            if i > 1 and abs(yValues[i] - yValues[i - 1]) > 20 * abs(yValues[i - 1] - yValues[i - 2]):
                yValues[i] = nan
        except ValueError:
            yValues.append(nan)
    
    pylab.plot(xValues, yValues)
    pylab.xlabel("x")
    pylab.ylabel("y")
    pylab.grid(True)
    pylab.title("Graph of function f(x)=%s for x from %s to %s" %(formula, minX, maxX))
    pylab.show()

plotChart("y=x*x-6*x+3", -500, 500)
plotChart("y=1/x", -1, 1)
plotChart("y=x*x*sin(x)*sqrt(x*x+2+x*x*x)/log(x*x*x)/(-x*x+20*x+9)", -20, 200)
plotChart("y=x*x*sin(x)*sqrt(x*x+2+x*x*x)/log(x*x*x)/(x*x+20*x+9)", -20, 50)



    
