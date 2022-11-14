import hashlib
from hashlib import sha256
class Block:
    def __init__(self,data,prev):
        self.data=data
        self.prev=prev
        if prev is not None:
             self.hash=sha256(prev.data.encode('utf8')).hexdigest()
             # print(self.hash)
class BlockChian():
    def __init__(self):
        self.head=Block('gensis',None)
        
    def add_block(self,data):
        self.head=Block(data,self.head)
def print_chain(chain):
    cur=chain.head
    while cur.prev is not None:
        print(cur.data)
        # print(cur.prev.hash,"\n")
        cur=cur.prev
        
def verify(chain):
    cur=chain.head
    while cur.prev is not None:
        # print(cur.data)
        # print(cur.hash)
        # print(cur.prev.data)
        # print(sha256(cur.prev.data.encode('utf8')).hexdigest())
        # print(sha256(cur.prev.data.encode('utf8')).hexdigest())
        if(cur.hash!=sha256(cur.prev.data.encode('utf8')).hexdigest()):
           print("Hash changed =>",cur.prev.data)
        else:
           print(cur.prev.data)
        # if(cur.data=="Block2"):
        #     print("yes")
        # else:
        #     print("no")
        cur=cur.prev
   
    
        
chain=BlockChian()
chain.add_block("Block1")
chain.add_block("Block2")
chain.add_block("Block3")

verify(chain)
# verify(chain)
