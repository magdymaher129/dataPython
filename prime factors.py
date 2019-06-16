def primeFactors(n):
    k=[]
    i=2
    
    while n>1:
        z= check(n,i)
        if (z>0):
            k.append(i)
            n=int(n/i)
        elif z==0:
            i=i+1
           
    return k

def check(n,i) :
    if n%i==0:
        return i 
    else :
        return 0


