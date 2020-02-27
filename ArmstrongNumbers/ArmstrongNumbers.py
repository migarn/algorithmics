upperLimit = 100000
print("Armstrong numbers in the range of 1-%i:" % upperLimit)

for i in range (1, upperLimit + 1):
    digits = []
    currentNumber = i

    while True:
        digit = currentNumber % 10
        digits.append(digit)
        currentNumber = (currentNumber - digit) // 10

        if currentNumber == 0:
            digitsSum = 0
            exponent = len(digits)
            
            for j in digits:
                digitsSum = digitsSum + j ** exponent

            if i == digitsSum:
                print(i)

            break;
