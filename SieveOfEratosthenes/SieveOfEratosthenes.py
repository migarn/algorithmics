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

            j += 1

            if j >= len(numbers):
                break
        
        if currentNumber >= sqrt(numbers[-1]):
            print("Sieve of Eratosthenes' result of work for range %i-%i:\n" %(2, n - 1))
            print(numbers)
            print("\n%i numbers has remained on the sieve." %len(numbers))
            break

        i += 1

def findNextKey(intKey, dictionary):
    lastNumberIndex = list(dictionary.keys())[-1]
    while True:
        if (intKey + 1) in dictionary or (intKey + 1) > lastNumberIndex:
            return intKey + 1
        else:
            intKey += 1

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
            print("Sieve of Eratosthenes' result of work for range %i-%i:\n" %(2, n - 1))
            print(list(numbers.values()))
            print("\n%i numbers has remained on the sieve." %len(list(numbers.values())))
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

            j += 1

            if j >= len(numbers):
                break

        if currentNumber >= sqrt(numbers[-1]):
            print("Sieve of Eratosthenes' result of work for range %i-%i:\n" %(2, n - 1))
            print(numbers)
            print("\n%i numbers has remained on the sieve." %len(numbers))
            break

        i += 1

startPoint = time.time()
eratostenesList(101)
endPoint = time.time()
timeElapsed = (endPoint - startPoint) * 1000
print("\nExecution time: %i ms (data structure - list)" %timeElapsed)
print("\n------------------------------------------------------------\n")
startPoint = time.time()
eratostenesDictionary(101)
endPoint = time.time()
timeElapsed = (endPoint - startPoint) * 1000
print("\nExecution time: %i ms (data structure - dictionary)" %timeElapsed)
print("\n------------------------------------------------------------\n")
startPoint = time.time()
eratostenesArray(101)
endPoint = time.time()
timeElapsed = (endPoint - startPoint) * 1000
print("\nExecution time: %i ms (data structure - array)" %timeElapsed)
  
