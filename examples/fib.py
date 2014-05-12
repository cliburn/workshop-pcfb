def fib(n):
    xs = [1,1]
    if n < 3:
        return xs[:n]
    else:
        for i in range(2, n):
            x = xs[i-1] + xs[i-2]
            xs.append(x)
    return xs

if __name__ == '__main__':
    print "fib(1) =", fib(1)
    print "fib(2) =", fib(2)
    print "fib(3) =", fib(3)
    print "fib(10) =", fib(10)
    
