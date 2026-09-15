class Node:
    def __init__(self,data):
        
       
        self.data=data

        self.next=None

   
node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3

def numbers(target):
  node=node1
  while(node!=None ):
    
    if node.data==target:
       return True
    
    node=node.next
  return False
print(numbers(20) ) 
print(numbers(50) )
    
