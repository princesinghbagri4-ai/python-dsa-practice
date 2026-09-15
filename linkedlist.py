class Node:
    def __init__(self,data):
        self.data=data

        self.next=None
c=0
s=0
        
node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
node=node1
while(node!=None ):
    c+=1

    s+=node.data
    print(node.data)
    node=node.next

print(c)
print(s)


    