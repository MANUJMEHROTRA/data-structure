# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:10:44 2020

@author: manuj.mehrotra
"""
class stack:
    def __init__(self):
        self.lst = []
    
    def push(self,a):
        self.lst.append(a)
    
    def pop(self):
        if self.lst:
            self.lst.pop()
        else:
            print("The list is empty")
    def peek(self):
        if not self.is_empty():
            return self.lst[-1]
    
    def printStack(self):        
        if self.lst:
            print(self.lst)
        else:
            print("The list is empty")

obj = stack()
obj.pop()
obj.push(1)
obj.printStack()
obj.push(3)
obj.push(1)
obj.printStack()
obj.push(1)
obj.printStack()
obj.pop()
obj.printStack()