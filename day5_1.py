string="DivYaZHiiUdF"
# string=input("Enter String")
k=5
i=0
encString=""
for c in string:
    num=ord(c)
    if(i%2==0):
        if(num>=97 and num<=122):
            if(num-k<=96):
                subNum=ord(c)-96
                addNum=k-subNum
                # print(addNum)
                num=122-addNum
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                encString=encString+chr(num)
            else:
                num=num-k
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                encString=encString+chr(num)
        else:
            if(num-k<=64):
                subNum=ord(c)-64
                addNum=k-subNum
                num=90-addNum
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                encString=encString+chr(num)
            else:
                num=num-k
                print(f"{c} is small char  {num} and Encode value os {chr(num)}")
                encString=encString+chr(num)
    else:
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
        
    i=i+1

print(f"The encrypted value is {encString}")


deString=""
i=0
for c in encString:
    num=ord(c)
    if(i%2==0):
        if(num>=97 and num<=122):
            if(num+k>=123):                
                remainNum=122-ord(c)
                addNum=k-remainNum
                # print(remainNum)
                encChar=96+addNum
                # print(encChar,"\n")
                deString=deString+chr(encChar)
            else:
                num=num+k                
                deString=deString+chr(num)
        else:
            if(num+k>=91):
                remainNum=90-ord(c)
                addNum=k-remainNum
                encChar=chr(64+addNum)
                deString=deString+encChar
            else:
                num=num+k                
                deString=deString+chr(num)
                # deString=deString+chr(num)
    else:
        if(num>=97 and num<=122):
            if(num-k<=96):
                remainNum=ord(c)-96
                addNum=k-remainNum
                encChar=122-addNum
                deString=deString+chr(encChar)
            else:
                num=num-k
                deString=deString+chr(num)
                # print("hii")
            
        else:
            if(num-k<=64):
                remainNum=ord(c)-64
                subNum=k-remainNum
                encChar=chr(90-subNum)
                deString=deString+encChar
            else:
                num=num-k
                deString=deString+chr(num)
     
        
    i=i+1
    
print(f"Decrypt String is {deString}   ")
                
                
print(deString)