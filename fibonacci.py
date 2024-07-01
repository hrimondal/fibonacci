
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
