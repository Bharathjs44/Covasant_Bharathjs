#program-1
 
 ########GIVEN TASK##########
 
#a = Poly(1,2,3)  #an, ...., a0 
#b = Poly(1,0,1,1,2,3)
#c = a+b 
#print(c) #Poly ( 1,0,1, 2,4,6)

class Poly:
    def __init__(self, *args):
        self.data =list(args)
        
    def __add__(self, differ):
        i,j =len(self.data),len(differ.data)
        if i < j:
            self.data = [0]*(j-i)+self.data
        else:
            differ.data = [0]*(i-j)+differ.data
        res=[]  
        for i,j in zip(self.data,differ.data):
            res.append(i+j)
        
        return Poly(*res)
    
    def __repr__(self):
        return f"Poly({','.join(map(str,self.data))})"
            
    
if __name__ == '__main__':
    a = Poly(1,2,4,2,3,2)
    b = Poly(1,0,1,2)
    c = a + b
    print(c)
        
        
#output: Poly(1,2,5,2,4,4)    
        
     
