string="ckpal"
# string=input("Enter String")
k=5
i=0
encString=""
for c in string:
    num=ord(c)
    if(i%2==0):
        if(num>=97 and num<=122):
            if(num+k>=122):
                subNum=122-ord(c)
                addNum=k-subNum
                num=96+addNum
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                encString=encString+chr(num)
            else:
                num=num+k
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                encString=encString+chr(num)
        else:
            if(num+k>=90):
                subNum=90-ord(c)
                addNum=k-subNum
                num=64+addNum
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                encString=encString+chr(num)
            else:
                num=num+k
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                encString=encString+chr(num)
    else:
        encString=encString+chr(num)
    i=i+1

print(f"The encrypted value is {encString}")
            
            
            
    # Decription
    deString=""
i=0
for c in encString:
    num=ord(c)
    if(i%2==0):
        if(num>=97 and num<=122):
            if(num-k<=96):
                subNum=num-96
                addNum=k-subNum
                num=96-addNum
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                deString=deString+chr(num)
            else:
                num=num-k
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                deString=deString+chr(num)
        else:
            if(num+k>=64):
                subNum=num-64
                addNum=k-subNum
                num=64-addNum
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                deString=deString+chr(num)
            else:
                num=num-k
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                deString=deString+chr(num)
    else:
        deString=deString+chr(num)   
    i=i+1
        
print(f"The encrypted value is {deString}")
            
            
    