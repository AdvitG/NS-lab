def encrypt():
    a=input("enter the text to be encrypted: ")
    b=input("enter the key: ")
    c=a.strip()
    c=c.replace(" ","")
    d=[[]]
    lenb=int(len(b))
    lengb=int(len(b))
    #print(b[lenb-lengb])
    
    letter=65
    '''
    for i in range(0,5):
        if lenb-lengb<5:
            door=b[lenb-lengb]
            print(door) 
            lengb=lengb-1
    print(lengb)
    '''
    for i in range(0,5):
        for j in range(0,5):
            
            if lengb==0:
                d[i][j]=chr(letter)
                letter=letter+1
               
            if lenb-lengb<5:
                door=b[lenb-lengb]
                print(door) 
                lengb=lengb-1
            
            


    for i in range(0,5):
        for j in range(0,5):
            print(d[i,j])
encrypt()
                
                
        
        
