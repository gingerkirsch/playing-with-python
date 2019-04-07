import functools
def memoize(function):
	function.cache = dict()
	@functools.wraps(function)
	def _memoize(*args):
	    if args not in function.cache:
	        function.cache[args] = function(*args)
	    return function.cache[args]
	return _memoize

@memoize
	def fibonacci(n):
		if n < 2:
    		return n
	else:
	    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 7):
	print('fibonacci %d: %d' % (i, fibonacci(i)))
