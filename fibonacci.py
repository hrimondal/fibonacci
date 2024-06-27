def fibonacci(n):
    a, b = 0, 1
    for n in range(n):
          a,b = b, a + b
          
    return a 
fibonacci_2019 = fibonacci(2019)
print(fibonacci_2019)

