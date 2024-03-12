class Node():
    def __init__(self, key) -> None:
        self.val = key
        self.right = None
        self.left = None
        self.level = None
    

class BSTTree():
    
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, key ) -> None:
        
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root,key)
        
                
    def _insert_recursive(self,root, key):
        
        if key< root.val :
            if root.left is None:
                root.left = Node(key)
            else:
                return self._insert_recursive(root.left,key)
        
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                return self._insert_recursive(root.right,key)
            
            
    def preOrder(self):
        self._preOrder_recursive(self.root)
        print()
        
    
    def _preOrder_recursive(self,root):
        if root:
            print(root.val, end=" ")
            self._preOrder_recursive(root.left)
            self._preOrder_recursive(root.right)
                
    def inOrder(self):
        self._inorder_recursive(self.root)
        print()
        
    
    def _inorder_recursive(self,root):
        if root:
            self._inorder_recursive(root.left)
            print(root.val, end=" ")
            self._inorder_recursive(root.right)
    
    
    def postOrder(self):
        self._inorder_recursive(self.root)
        print()
        
    
    def _postOrder_recursive(self,root):
        if root:
            self._postOrder_recursive(root.left)
            self._postOrder_recursive(root.right)
            print(root.val, end=" ")
   
    def height(self):
        return self._recursive_height(self.root)
   
    def _recursive_height(self,root):
        if root is None:
            return -1
        return max(self._recursive_height(root.left),self._recursive_height(root.right)) +1
    
    
    def levelOrderTraversal(self):   
        if self.root is None:
            return None
        return_lst = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            return_lst.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return return_lst
    
    
    def topViewTree(self):
        if self.root is None:
            return None
        queue = [self.root]
        self.root.level = 0
        dict_node_pos = dict()
        while queue:
            node = queue.pop(0)
            
            if node.level not in dict_node_pos:
                dict_node_pos[node.level] = node.val
            
            if node.left:
                node.left.level = node.level-1
                queue.append(node.left)
                
            if node.right:
                node.right.level = node.level+1
                queue.append(node.right)

        
        return dict_node_pos
    
    
    def isBST(self):
        return self._recursive_isBST(self.root)
    
    def _recursive_isBST(self,node):
        if node:
            if node.right:
                if node.right.val < node.val:
                    return self._recursive_isBST(node.right)
                else:
                    return False
            if node.left:
                if node.left.val > node.val:
                    return self._recursive_isBST(node.left)
                else:
                    return False 
        return True

if __name__ == '__main__':
    bst = BSTTree()
    for i in [5,2,10,7,15,12,20,30,6,8]:
        bst.insert(i)
    
    print('=-------------done with Inserting----------')
    
    print('=-------------Started with preOrder----------')
    bst.preOrder()
    
    print('=-------------Started with InOrder----------')
    bst.inOrder()
    
    print('=-------------Started with PostOrder----------')
    bst.postOrder()
    
    print('=-------------Started with height of Tree----------')
    print(bst.height())
    
    print('=-------------Started with LevelOrder of Tree----------')
    print(bst.levelOrderTraversal())
    
    print('=-------------Started with topView of Tree----------')
    print(bst.topViewTree())