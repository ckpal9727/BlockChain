string="kApXx"
k=5
encString=""
for c in string:
    num=ord(c)
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
print(f"The encrypted value is {encString}")
            
            
            
    