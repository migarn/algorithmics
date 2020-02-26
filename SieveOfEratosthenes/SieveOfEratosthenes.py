from math import sqrt
from collections import OrderedDict
from numpy import *
import time

def eratostenesList(n):
    numbers = list(range(2, n))
    i = 0

    while True:
        currentNumber = numbers[i]
        j = i + 1

        while True:
            if numbers[j] % currentNumber == 0:
                numbers.pop(j)

            j = j + 1

            if j >= len(numbers):
                break
        
        if currentNumber >= sqrt(numbers[-1]):
            print("Wynik działania sita Eratostenesa dla przedziału od %i do %i:\n" %(2, n - 1))
            print(numbers)
            print("\nNa sicie zostało %i liczb" %len(numbers))
            break

        i = i + 1

def findNextKey(intKey, dictionary):
    lastNumberIndex = list(dictionary.keys())[-1]
    while True:
        if (intKey + 1) in dictionary or (intKey + 1) > lastNumberIndex:
            return intKey + 1
        else:
            intKey = intKey + 1

def eratostenesDictionary(n):
    numbers = OrderedDict()

    for i in range(2, n):
        numbers[i - 2] = i

    i = 0

    while True:
        currentNumber = numbers[i]
        j = findNextKey(i, numbers)

        while True:
            if numbers[j] % currentNumber == 0:
                numbers.pop(j)

            j = findNextKey(j, numbers)

            lastNumberIndex = list(numbers.keys())[-1]
            if j > lastNumberIndex:
                break
           
        if currentNumber >= sqrt(next(reversed(numbers))):
            print("Wynik działania sita Eratostenesa dla przedziału od %i do %i:\n" %(2, n - 1))
            print(list(numbers.values()))
            print("\nNa sicie zostało %i liczb" %len(list(numbers.values())))
            break

        i = findNextKey(i, numbers)

def eratostenesArray(n):
    numbers = zeros(n - 2)
    
    for i in range(2, n):
        numbers[i - 2] = i

    i = 0

    while True:
        currentNumber = numbers[i]
        j = i + 1

        while True:
            if numbers[j] % currentNumber == 0:
                numbers = delete(numbers, j)

            j = j + 1

            if j >= len(numbers):
                break

        if currentNumber >= sqrt(numbers[-1]):
            print("Wynik działania sita Eratostenesa dla przedziału od %i do %i:\n" %(2, n - 1))
            print(numbers)
            print("\nNa sicie zostało %i liczb" %len(numbers))
            break

        i = i + 1

startPoint = time.time()
eratostenesList(101)
endPoint = time.time()
timeElapsed = (endPoint - startPoint) * 1000
print("\nCzas wykonania: %i ms (struktura danych - lista)" %timeElapsed)
print("\n------------------------------------------------------------\n")
startPoint = time.time()
eratostenesDictionary(101)
endPoint = time.time()
timeElapsed = (endPoint - startPoint) * 1000
print("\nCzas wykonania: %i ms (struktura danych - słownik)" %timeElapsed)
print("\n------------------------------------------------------------\n")
startPoint = time.time()
eratostenesArray(101)
endPoint = time.time()
timeElapsed = (endPoint - startPoint) * 1000
print("\nCzas wykonania: %i ms (struktura danych - tablica)" %timeElapsed)
  
