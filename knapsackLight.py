'''
You found two items in a treasure chest!
The first item weighs weight1 and is worth value1,
and the second item weighs weight2 and is worth value2.
What is the total maximum value of the items you can
take with you, assuming that your max weight capacity
is maxW and you can't come back for the items later?
Note that there are only two items and you can't bring
more than one item of each type,
i.e. you can't take two first items 
or two second items.
'''
def knapsackLight(value1, weight1, value2, weight2, maxW):
    amount =weight1+weight2
    if (maxW>=amount):
        return value1+value2
    else:
        
      if(value1>value2) and((maxW>=weight1)  and (maxW<weight2)) :
        return value1
      if(value1<value2) and((maxW>=weight1)  and (maxW<weight2)) :
        return value1
    
      if(value1<value2) and((maxW>=weight2)  and (maxW<weight1)) :
        return value2
      if(value1>value2) and((maxW>=weight2)  and (maxW<weight1)) :
        return value2
     
      
    
      if(maxW<weight1)and (maxW<weight2) :
        return 0
      if(maxW>=weight1)and (maxW>weight2) and (value1>value2):
        return value1
      if(maxW>weight1)and (maxW>=weight2) and (value2>value1):
        return value2
      if(maxW>=weight2)and (maxW>weight1) and (value1>value2):
        return value1
      if(maxW>weight2)and (maxW>=weight2) and (value2>value1):
        return value2
    
      if  (value2==value1) :
          return value1
    


