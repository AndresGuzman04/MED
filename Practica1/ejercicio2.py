
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if num1 > num2:
  print("{0} es mayor a {1}".format(num1, num2))
elif num1 < num2:
    print("{1} es mayor a {0}".format(num1, num2))
elif num1 == num2:
   print("{0} es igual a {1}".format(num1, num2))
else:
   print("Error")