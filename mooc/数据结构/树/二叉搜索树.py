class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self, key, val):  # 插入一个节点
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if key > currentNode:
                if currentNode.hasRightChild():
                    self._put(key, val, currentNode.rightChild)
                else:
                    currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.lefitChild)
        else:
            return self._get(key, currentNode.rightChild)

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error,key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error,key not in tree')

    def remove(self, key, currentNod):
        if currentNod.isLeaf():
            if currentNod == currentNod.parent.leftChild:
                currentNod.parent.leftChild = None
            else:
                currentNod.parent.rightChild = None

        elif currentNod.hasBothChilren:
            succ = currentNod.findSuccessor()
            succ.spliceOut()
            currentNod.key = succ.key
            currentNod.payload = succ.payload

        else:
            if currentNod.hasLeftChild():
                if currentNod.isLeftChild():
                    currentNod.leftChild.parent = currentNod.parent
                    currentNod.parent.leftChild = currentNod.leftChild
                elif currentNod.isRightChild():
                    currentNod.leftChild.parent = currentNod.parent
                    currentNod.parent.rightChild = currentNod.leftChild
                else:
                    currentNod.replaceNodeDate(currentNod.leftChild.key, currentNod.leftChild.payload,
                                               currentNod.leftChild.leftChild, currentNod.leftChild.rightChild)
            else:
                if currentNod.isLeftChild():
                    currentNod.rightChild.parent = currentNod.parent
                    currentNod.parent.leftChild = currentNod.rightChild
                elif currentNod.isRightChild():
                    currentNod.rightChild.parent = currentNod.parent
                    currentNod.parent.rightChild = currentNod.rightChild
                else:
                    currentNod.replaceNodeDate(currentNod.rightChild.key, currentNod.rightChild.payload,
                                               currentNod.rightChild.leftChild, currentNod.rightChild.rightChild)

    def __delitem__(self, key):
        self.delete(key)

    def __getitem__(self, key):  # 索引取值
        self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def __setitem__(self, key, value):  # 索引赋值
        self.put(key, value)

    def __len__(self):  # 可以用内置函数len调用
        return self.size

    def __iter__(self):  # 可以迭代 for in
        return self.root.__iter__()


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key  # 键值
        self.payload = val  # 所包含的数据项
        self.leftChild = left  # 左子节点
        self.rightChild = right  # 右子节点
        self.parent = parent  # 父节点

    def hasLeftChild(self):  # 是否拥有左子节点
        return self.leftChild

    def hasRightChild(self):  # 是否拥有右子节点
        return self.rightChild

    def isLeftChid(self):  # 判断是否是父节点的左子节点
        return self.parent and self.parent.leftChild == self

    def isRightChid(self):  # 判断是否是父节点的右子节点
        return self.parent and self.parent.rightChild == self

    def isRoot(self):  # 判断是否是根节点
        return not self.parent

    def isLeaf(self):  # 判断是否是叶节点
        return not (self.rightChild and self.leftChild)

    def hasAnyChild(self):  # 判断是否有子节点
        return self.rightChild or self.leftChild

    def hasBothChild(self):  # 判断是否同时有左右子节点
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):  # 更改键值、所包含数据项、左子节点、右子节点、
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():  # 重新链接左子节点
            self.leftChild.parent = self
        if self.hasRightChild():  # 重新链接右子节点
            self.rightChild.parent = self

    def findSuccessor(self):  # 寻找后继节点
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findmin()
        else:
            if self.parent:
                if self.isLeftChid():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.finSuccessor()
                    self.parent.rightChild = self
            return succ

    def splitceOut(self):  # 摘出叶节点
        if self.isLeaf():
            if self.isLeftChid():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChild():
            if self.hasLeftChild():
                if self.isLeftChid():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChid():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.hasRightChild():
                    yield elem
