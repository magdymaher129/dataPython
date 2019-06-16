'''
Consider an arithmetic expression of the form
a#b=c. Check whether it is possible to replace #
with one of the four signs: +, -, * or / to obtain
a correct expression
'''
def arithmeticExpression(a, b, c):
    m=0
    if a+b==c:
        m=m+1 
    if a-b==c:
        m=m+1 
    if a*b==c:
        m=m+1 
    if a/b==c:
        m=m+1
    if m>0:
         return True
    else:
         return False
    
