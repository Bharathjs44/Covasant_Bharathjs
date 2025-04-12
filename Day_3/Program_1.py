############ Day-3 ################

#Q- flatten lists

flatlist=[]

def flatten(mylist):
    for item in mylist:
        if type(item) is list:
            flatten(item)
        else:
            flatlist.append(item)
    return flatlist
    
list1= [1,2,3, [1,2,3,[3,4],2]]
print("flattend list is: ",flatten(list1))


#output: flattend list is:  [1, 2, 3, 1, 2, 3, 3, 4, 2]