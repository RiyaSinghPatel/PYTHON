#fibonacci serious

def fib(i):
  if i == 0:
    return 0
  elif i == 1:
    return 1
  else:
    fab = fib(i - 2) + fib(i - 1)
    return fab


for i in range(10):
  print(fib(i))

print("print the fibonacci seris=", fib(10))