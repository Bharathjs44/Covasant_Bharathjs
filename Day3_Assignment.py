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

#######################################################################################

'''input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]'''

    
#Q - converting into list

data= [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]

def convert_to_list(data):
    conv_list =[]
    for item in data:
        if type(item) is list:
            conv_list.append(convert_to_list(item))
        elif type(item) is str:
            lis = item.strip('()').split(',')
            x=[]
            for i in lis:
              x.append(int(i))
            conv_list.append(x)  
              
    return conv_list
 
print("Converted list is:",convert_to_list(data)) 
    
    