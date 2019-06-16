def phoneCall(min1, min2_10, min11, s):
    m1=0
    m2=0
    m3=0
    f=0
    t1=0
    t12=0
    total=0
    t1=min1*1
    t12=min1*1+min2_10*9
    if s>t12:
        f=s-t12
        m3=int(f/min11)
        total=1+9+m3
    elif s<= t12 and s>t1:
        f=s-t1
        m2=int(f/min2_10)
        total=1+m2
    elif s<=t1:
        m1=int(s/min1)
        total =m1
    return (total)
