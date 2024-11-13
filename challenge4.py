def gauss(numbers):
    for number in numbers:
        while len(numbers) > 0:
            num1 = numbers.pop(0)
            print(num1)
            num2 = numbers.pop(-1)
            print(num2)
            calc = num1 + num2
            print(str(num1) + " + " + str(num2) + " = " + str(calc))
    print("Final answer is: " + str(num1 * calc))
   
           
gauss(list(range(1,101)))