deString=""
for c in encString:
    num=ord(c)
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
print(f"The encrypted value is {deString}")
            
            
    