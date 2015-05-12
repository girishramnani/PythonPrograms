

class node(object):

    def __init__(self,data):
        self.data  = data
        self.left = None
        self.right = None




class Tree(object):

    
    def __init__(self,data):

        self.head = node(data)

    def _insert(self,data,inode):
        if inode.data ==None:
            inode.data = data
        elif inode.data >data:
            if inode.left ==None:
                inode.left = node(data)
            else:
                self._insert(data,inode.left)
        else:
            if inode.right ==None:
                inode.right = node(data)
            else:
                self._insert(data,inode.right)

    
    def insert(self,data):
        if type(data) == list:
            print("list")
            for da in data:
                self._insert(da,self.head)
        else:
            self._insert(data,self.head)


    
    def inorder2(self,inode):
        if inode !=None:
            self.inorder2(inode.left)
            print(inode.data)
            self.inorder2(inode.right)
        

        
    def inorder(self):
        stack=[]
        stack.append(self.head)
        current = self.head
        while stack:
            current = stack.pop()
            while current != None:
                print(current.data)
                if current.right is not None:
                    stack.append(current.right)
                current = current.left
            


    

work = Tree(5)
work.insert([1,2,3,6,7])
work.inorder()

        
        
