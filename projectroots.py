import math
a = int(input("Введіть значення a = "))
b = int(input("Введіть значення b = "))
c = int(input("Введіть значення c = "))
D = b ** 2 - 4 * a * c
print(D)
if D < 0:
  print("Коренi вiдсутнi")
elif D == 0:
  x = -b /( 2 * a)
  print (x)
else:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 * a)
  print(x1)
  print(x2)
