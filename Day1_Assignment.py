D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

#Union
D3= D1.copy()
for key, value in D2.items():
    D3[key]=value
print(D3)
    
#Intersection
print({key:D1[key] for key in D1 if key in D2 })
 
#Set Difference
difference={}
for key in D1:
    if key not in D2:
        difference[key]=D1[key]
print(difference)    

#merge
merge={}
for key in D1:
    merge[key]=D1[key]
for key in D2:
    if key in merge:
        merge[key]+= D2[key]
    else:
        merge[key]=D2[key]
print(merge)
        
