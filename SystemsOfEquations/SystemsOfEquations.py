import numpy

file = open("data.txt","r")
readFile = file.readlines()
file.close()
unknownsNumber = int(readFile[0])
coefficientMatrix = []
constants = []

for i in range(1,(unknownsNumber + 1)):
    currentLine = readFile[i].strip().split()
    coefficientMatrix.append(currentLine[:-1])
    constants.append(currentLine[len(currentLine) - 1])

coefficientMatrix = numpy.matrix(coefficientMatrix, dtype = "float")
constants = numpy.matrix(constants, dtype = "float").transpose()
determinants = []

for i in range(unknownsNumber):
    iMatrix = coefficientMatrix.copy()
    iMatrix[:, i] = constants
    iDeterminant = round(numpy.linalg.det(iMatrix), 13)
    determinants.append(iDeterminant)

mainDeterminant = round(numpy.linalg.det(coefficientMatrix), 13)

if mainDeterminant != 0:
    unknows = [i / mainDeterminant for i in determinants]
    print("For given system of equations unknowns have been computed as:")
    for i in range(len(unknows)):
        print("x%i = %f" %(i + 1, unknows[i]))

elif all([i == 0 for i in determinants]):
    print("Given system of equations is indeterminate.")

else:
    print("Given system of equations is inconsistent.")
