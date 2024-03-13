class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    
    
    def inserNode(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            
    def traverse(self):
        if self.head is None:
            return self.head
        else:
            current_node = self.head
            while current_node:
                print(current_node.val)
                current_node = current_node.next
    
    def inser_inBetween(self,val,newNode_val):
        newNode = Node(newNode_val)
        if self.head is None:
            self.head == newNode
        else:
            currentNode = self.head
            while currentNode.val == val and currentNode is not None:
                currentNode = currentNode.next
                
            next_Node = currentNode.next
            currentNode.next = newNode
            newNode.next = next_Node
    
    def delition(self,val):
        if self.head is None:
            return self.head
        dummyNode =Node(None)
        dummyNode.next = self.head
        currentNode = dummyNode
        while currentNode.val == val and currentNode is not None:
                currentNode = currentNode.next
        if currentNode.next:
            currentNode.next = currentNode.next.next
        
        
        


if __name__ == '__main__':
    linkdList = LinkedList()
    linkdList.inserNode(5)
    linkdList.inserNode(51)
    linkdList.inserNode(56)
    linkdList.inserNode(44)
    linkdList.inserNode(33)
    linkdList.inserNode(12)
    linkdList.traverse()
    linkdList.inser_inBetween(5,300)
    print('---------------INSERT INBETWEEN-----------------------')
    linkdList.traverse()
    linkdList.delition(300)
    print('---------------DELTION-----------------------')
    linkdList.traverse()
    
    
    

                
            