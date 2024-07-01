def fib(term):
    if term <= 1:
        return term
    else:
        return fib(term - 1) + fib(term - 2)


# Change this value to adjust the number of terms in the sequence.
number_of_terms = int(input())
for i in range(number_of_terms):
    print(fib(i))


# Or,
def fibonacci(n):
  """
  This function calculates the nth term of the Fibonacci sequence.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Get user input for the term
term = int(input("Enter the term you want to find: "))

# Calculate and print the nth Fibonacci term
print(fibonacci(term))
