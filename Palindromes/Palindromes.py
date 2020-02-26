maxTransformationsNumber = 0
numberWithMaxTransformations = 0

for i in range (1, 300):
    print("Sprawdzam hipotezę dla liczby %i:" % i)

    digits = []
    currentNumber = i
    count = 0

    while True:
        digit = currentNumber % 10
        digits.append(digit)
        currentNumber = (currentNumber - digit) // 10

        if currentNumber == 0:
            isPalindrome = True
            
            for j in range (0, len(digits) // 2):
                isPalindrome = (digits[j] == digits[len(digits) - 1 - j])

            if isPalindrome:               
                print("\tDla liczby %i udało się osiągnąć palindrom. Liczba dodatkowych przekształceń: %i\n" % (i, count))

                if count > maxTransformationsNumber:
                    maxTransformationsNumber = count
                    numberWithMaxTransformations = i
                    
                break;

            else:
                component1 = 0
                coefficient = 1

                for j in digits:
                    component1 = component1 + j * coefficient
                    coefficient = coefficient * 10

                component2 = 0
                coefficient = 1

                for j in reversed(digits):
                    component2 = component2 + j * coefficient
                    coefficient = coefficient * 10

                currentNumber = component1 + component2
                count = count + 1
                print("\t%i + %i = %i" % (component1, component2, currentNumber))
                digits.clear()

print("Największa liczba przekształceń została osiągnięta dla liczby %i (%i przekształceń)" % (numberWithMaxTransformations, maxTransformationsNumber))
