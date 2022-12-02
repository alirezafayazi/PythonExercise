while True:
  try :
      # اعداد را از کاربر دریافت میکنیم
      number = int(input('-- please enter a number : '))
      break
  except:
      #اگر داده های ورودی به عدد صحیح تبدیل نشدند اخطار میدهیم تا کاربر عدد وارد کند
      print('\n ** please enter a number (Just enter number !) \n')

print(type(number),number)

print('''Please select a base to convert the number to base .
\n1.Binary \n2.OCT \n3.HEX
''')
base = int(input('inter 1 , 2 or 3 : '))

#تا زمانی که عدد وارد شد در گزینه ها نباشد از کاربر عدد میگیریم
while (base != 1) and (base != 2) and (base != 3):
    base = int(input('inter 1 , 2 or 3 : '))

if base == 1:
    print(bin(number)[2:])
elif base == 2:
    print(oct(number)[2:])
elif base == 3:
    print(hex(number)[2:])

