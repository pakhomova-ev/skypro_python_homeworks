# Напишите функцию  fizz_buzz, которая принимает один аргумент — n (число).
# Функция должна печатать числа от 1 до n. При этом:
# если число делится на 3, печатать Fizz;
# если число делится на 5, печатать Buzz;
# если число делится на 3 и на 5, печатать FizzBuzz.

def fizz_buzz(num):
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0:
                print("Fizz")
            else: print(i) 

fizz_buzz(5)
 
