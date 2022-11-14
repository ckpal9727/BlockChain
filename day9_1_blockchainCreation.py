import hashlib
class Block:
    def __init__(self,data,prev):
        self.data=data
        self.prev=prev
class BlockChian():
    def __init__(self):
        self.head=Block('gensis',None)
        
    def add_block(self,data):
        self.head=Block(data,self.head)
def print_chain(chain):
    cur=chain.head
    while cur.prev is not None:
        print(cur.data)
        cur=cur.prev
        
def verify(chain):
    cur=chain.head
    while cur.prev is not None:
        if(cur.data=="Block2"):
            print("yes")
        else:
            print("no")
        cur=cur.prev
   
    
        
chain=BlockChian()
chain.add_block("Block1")
chain.add_block("Block2")
chain.add_block("Block3")

print_chain(chain)
verify(chain)
