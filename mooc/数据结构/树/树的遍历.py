# 前序遍历 根——左——右

def preoder(tree):
    if tree:
        print(tree.getRootVal())
        preoder(tree.getLeftChild())
        preoder(tree.getRightChild())

# 中序遍历 左——根——右

def inorder(tree):
    if tree != None:
        preoder(tree.getLeftChild())
        print(tree.getRootVal)
        preoder(tree.getRightChild())



# 后序遍历 左——右——根
def postorder(tree):
    if tree !=None:
        preoder(tree.getLeftChild())
        preoder(tree.getRightChild())
        print(tree.getRootVal)
