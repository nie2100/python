from Node import Node


class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current=current.getNext()
            return count

    def search(self,item):
        current = self.head
        fount = False
        while current != None and not fount:
            if current.getData() == item :
                fount = True
            else:
                current = current.getNext()
        return fount

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())