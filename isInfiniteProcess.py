'''
Given integers a and b,
determine whether the
following pseudocode results
in an infinite loop
Assume that the program is executed
on a virtual machine which can store
arbitrary long numbers and execute forever.
'''
def isInfiniteProcess(a, b):
    if a==b:
        return False
    for i in range(20):
        a+=1
        b-=1
        if a==b:

        
            m=False
        # print(m)
            break
        else:
            m=True
        # print(m)
    return m


