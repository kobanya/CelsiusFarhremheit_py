# mit váltasz mire

mertekegyseg = input ("Mit váltasz át :  C vagy F :  ")

def valassz():
        if mertekegyseg.upper()  == 'C' :
             celsius = float(input("Enter temperature in celsius/ Add meg a hőmérsékletet Celsius fokban: "))
             fahrenheit = (celsius * 9 / 5) + 32
             print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))
             print('%.2f Celsius fok az  %0.2f Fahrenheit fok' % (celsius, fahrenheit))
        elif  mertekegyseg.upper() =='F':
                fahrenheit = float(input("Enter temperature in fahrenheit / Add meg a hőmérsékletet Fahrenheit fokban: "))
                celsius = (fahrenheit - 32) * 5/9
                print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))
                print('%.2f Fahrenheit fok  %0.2f Celsius fok' % (fahrenheit, celsius))
        else:  print( "Csak C vagy F mértékegység adható meg")

valassz()