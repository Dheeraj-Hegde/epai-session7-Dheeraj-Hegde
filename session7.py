from functools import reduce
fib = (lambda n : reduce(lambda x, _ : x + [x[-1] + x[-2]], range(n-2), [0,1]))

fib_list = fib(10000)

fib_or_not = lambda n: filter(lambda x: x in fib_list, f)

