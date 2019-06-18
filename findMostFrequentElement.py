import statistics
from statistics import mode 


'''
given a list ,find the most frequent element in it .
if there are multible elements that appear maximum number of times ,
'''
def most_frequent(list):
    counter =list.count(0)
    num= list[0]
    sequence=[]
    for i in list:
        curr_frequency=list.count(i)
        if (curr_frequency>counter):
            counter=curr_frequency
            num=i
    return num

  # approach :2
def most_frequent2(list):
    return max (set(list),key=list.count)
 # approach :3


def most_frequent3(list):
     return mode(list)
            
            
   
list1=[2,2,2,2,4,4,5,5,1,1,1,3,1,3,1,2,2,3]
print (most_frequent3(list1))