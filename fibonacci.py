def fibonacci(n):
    a, b = 0, 1
    for n in range(n):
          a,b = b, a + b
          
    return a 
# in below code you have to add the serial number of the term
# suppose you want to find out the n-th term.
# fibonacci_n = fibonacci(n)
fibonacci_20 = fibonacci(20)
# print(fibonacci_n)
print(fibonacci_20)
# this code will primarily give output of the 20th term
