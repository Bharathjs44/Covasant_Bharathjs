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
    
    