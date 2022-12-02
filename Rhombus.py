while True:
    try :
        # اعداد را از کاربر دریافت میکنیم
        number = int(input('-- please enter a number : '))
        break
    except:
        #اگر داده های ورودی به عدد صحیح تبدیل نشدند اخطار میدهیم تا کاربر عدد وارد کند
        print('\n ** please enter a number (Just enter number !) \n')


if number%2==0:
    for i in range(2,number,2):
        if (i==2):
           print(' '*((number//2)-(i//2-2)) , '*'*2 , ' '*((number//2)-(i//2-2))  )
        else:
            print(' '*((number//2)-(i//2-2)),'*'*2+' '*(i-3)+'*'*2,' '*((number//2)-(i//2-1)))
    for i in range(number,0,-2):
        if (i==2):
           print(' '*((number//2)-(i//2-2)) , '*'*2 , ' '*((number//2)-(i//2-2))  )
        else:
            print(' '*((number//2)-(i//2-2)),'*'*2+' '*(i-3)+'*'*2,' '*((number//2)-(i//2-1)))
    
else:
    print('\n')
    for i in range(1, number, 2):
        print(" "*(number//2-i//2), "*"*i)
    for i in range(number, 0, -2):
        print(" "*(number//2-i//2), "*"*i)
    print('\n')

