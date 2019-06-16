def lateRide(n):
    h=int(n/60)
    sh=str(h)
    
    m=n%60
    sm=str(m)
    x=0
    y=0
    for n in sh:
        x+=int(n)
    for n in sm:
        y+=int(n)    
    
    
    total= x+y
    return total 
