while True:
    try :
         # اعداد را از کاربر دریافت میکنیم
        firstNumber = int(input('-- please enter a two-digit number : '))
        secondNumber = int(input('-- please enter another two-digit number : '))
        
        # بررسی میکنیم که اعداد دو رقمی باشند
        while not((9<firstNumber<100) and (9<secondNumber<100)):
            print('\n ** Your input numbers are not correct ! \n')
             # اعداد را از کاربر دریافت میکنیم
            firstNumber = int(input('-- please enter a two-digit number : '))
            secondNumber = int(input('-- please enter another two-digit number : '))
        break
    except:
        #اگر داده های ورودی به عدد تبدیل نشدند اخطار میدهیم تا کاربر عدد وارد کند
        print('\n ** please enter a two-digit number (Just enter the number !) \n')



calculatedValue1 = ((firstNumber + secondNumber ) ** firstNumber)/((firstNumber+secondNumber) ** secondNumber)
calculatedValue2 =(firstNumber / secondNumber) ** (firstNumber + secondNumber)


print (f"""\nyour first number is : ---> {firstNumber} 
and your second number is : --->{secondNumber}""" )

if calculatedValue1 > calculatedValue2:
    print(f"\nThe first calculated value ({calculatedValue1}) is greater than the second calculated value ({calculatedValue2})")
elif calculatedValue1 < calculatedValue2:
    print (f"\nThe second calculated value ({calculatedValue2}) is greater than the first calculated value ({calculatedValue1})")
else:
    print (f"\nThe second calculated value ({calculatedValue2}) is equal to the first calculated value ({calculatedValue1})")