'''Fibonacci generator'''

def fib(max):
  a, b = 0, 1
  while a < max:
    yield a
    a, b = b, a + b

if __name__ == '__main__':
  for n in fib(1000):
    print(n, end=' ')
  print()
  print(list(fib(1000)))
  # import sys
  # if sys.argv[1:]:
  #     print(fib(sys.argv[1]))
  # else:
  #     print(__doc__)