def fizz_buzz(n):
        if n % 3 ==0 and n % 5 ==0:
            print("FizzBuzz")
        elif n % 5 ==0:
            print("Buzz")
        elif n % 3 ==0:
            print("Fizz")
        else: print("Not correct number. Try again, please!") 

fizz_buzz(10)
 
