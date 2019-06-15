def check(n,i) :
    if n%i==0:
        return i 
    else :
        return 0


def factoral(n):
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




       
      
          
            
            
    
print(factoral(625))
print(int('01001010',2))
v='{0:06b}'.format(74)
print (v)
def to_int(n):
    return (int(n,2))
def to_bit(d):
    return (bin(d)[2:])
def swap(n):
    b=to_bit(n)
    print (b)
    length= len(b)
    print(length)
    s=''
    #s=b[1]
    print (s)
    e='0'
    o='0'
    d=''
    if length%2==0:
         for x in range(int(length/2)):
           s=b[x]+b[x-1]
           print (s[::-1])
           f='',s[::-1]
           d=d.join(f)
    else :
        s=b[1]+b[0]
        f='',s[::-1]
        for x in range(2,int(length/2)):
           s=b[x]+b[x-1]
           print (s[::-1])
           f='',s[::-1]
           d=d.join(f)
       
   
        
        
            
    return d

def swap2(n):
    b=to_bit(n)
    print (b)
    length= len(b)
    print(length)
    even=[]
    odd=[]
    for x in range (length):
        if x%2==0:
            even.append(b[x])
        else:
            odd.append(b[x])
    print (odd)
    print (even)
    f=lambda a,b : a+ b ,even ,odd
    return f

print(swap2(74))
a='0110110'
g=bin(67)[2:]

#print(g[::-1])
