def maxMultiple(divisor, bound):
    max=0
    for n in range(bound+1):
        if n%divisor==0:
            max=n
    return max
