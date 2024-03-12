# Напишите функцию square, принимающую один аргумент — сторону квадрата — и возвращающую площадь квадрата.
# Если переданный аргумент был не целым, округлите результат вверх.
import math

def square():
      b = float(input("Type size: "))
      result = math.ceil(b*b)
      print(result)

square() 