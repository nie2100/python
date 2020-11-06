class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.righChild = None
        print(self.key, self.leftChild, self.righChild)

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            self.leftChild, BinaryTree(newNode).leftChild = BinaryTree(newNode).key, self.leftChild

    def insertRight(self, newNode):
        if self.righChild == None:
            self.righChild = BinaryTree(newNode)
        else:
            self.righChild, BinaryTree(newNode).righChild = BinaryTree(newNode), self.righChild

    def getRightChild(self):
        return self.righChild

    def getLiftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    # def preorder(self):
    #     print(self.key)
    #     if self.leftChild:
    #         self.leftChild.preorder()
    #     if self.righChild:
    #         self.righChild.preorder()

# r = BinaryTree('a')
# r.insertLeft('b')
# r.insertRight('c')
# r.getRightChild().setRootVal('hello')
# r.getLiftChild().insertRight('d')

