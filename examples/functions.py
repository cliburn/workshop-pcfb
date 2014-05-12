def sum(xs):
    """Given a sequence of numbers, return the sum."""
    s = 0
    for x in xs:
        s += x
    return s

def prod(xs):
    """Given a sequence of numbers, return the product."""
    s = 1
    for x in xs:
        s *= x
    return s
