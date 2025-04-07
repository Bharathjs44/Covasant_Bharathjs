############ Day-3 ################

#Q- flatten lists

def flatten(mylist):
    flatlist=[]
    for item in mylist:
        if isinstance(item, list):
            flatlist.extend(flatten(item))
        else:
            flatlist.append(item)
    return flatlist
    
list1= [1,2,3, [1,2,3,[3,4],2]]
print("flattend list is: ",flatten(list1))

#######################################################################################

'''input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]'''

    
#Q - converting into list

data= [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]

converted =[]
for outer in data:
    outer_list =[]
    for inner in outer:
        inner_list=[]
        for item in inner:
            numbers=list(map(int,item.strip('()').split(',')))
            inner_list.append(numbers)
        outer_list.append(inner_list)
    converted.append(outer_list)
 
print("Converted list is:",converted) 
    
    