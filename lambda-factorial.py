# from zvoase
# https://ideone.com/MIorz
factorial = (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: (lambda n: n == 0 and 1 or n*f(n-1)))
