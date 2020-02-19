# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:45:32 2020

@author: manuj.mehrotra
"""

class queue:
    
    def __init__(self):
        self.lst = []
    def push(self,data):
        self.lst.append(data)
        
    def pop(self):
        if self.lst:
            self.lst.pop(0)
        else:
            print("The queue is Empty")
             
    def printQueue(self):
        print(self.lst)
        
    def peek(self):
        if self.lst:
            return self.lst[0]
    
    
obj = queue()
obj.pop()
obj.printQueue()
obj.push(2)
obj.printQueue()
obj.push(3)
obj.printQueue()
obj.push(4)
obj.printQueue()
obj.push(5)
obj.printQueue()
obj.push(6)
obj.printQueue()
obj.push(7)
obj.printQueue()
obj.pop()
obj.printQueue()
obj.pop()
obj.printQueue()
print(obj.peek())