class BST:
    """Binary Search algorithm is a logarithmic search For more information regarding BSTs, see:
    http://en.wikipedia.org/wiki/Binary_search_tree
    """

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    # def isEmpty(self):
    #         return self.head == None  # If BST has no head that means BST is an empty tree

    def insert(self, value: float):
        """adds new element to BST"""
        current = self

        while True:
            if self.value is None:
                self.value=value
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BST(value)
                    break
                else:
                    current = current.right
        return self

    def _len(self):
        if self.left and self.right:
            return 1 + self.left._len() + self.right._len()
        if self.left:
            return 1 + self.left._len()
        if self.right:
            return 1 + self.left._len()
        else:
            return 1

    def len(self):
        """returns the length of BST"""
        if self.value:
            return self._len()
        else:
            return 0

    def find(self, val):
        """Finds an element in BST"""
        current = self
        if current is not None:  # This makes sure that our tree is not empty
            while current is not None:
                if current.value == val:
                    return True
                elif val > current.value:
                    current = current.right
                elif val < current.value:
                    current = current.left
            else:
                return False

    def addList(self, numbers: list):
        """Converts a list into a BST"""
        for number in numbers:
            self.insert(number)

    def delete(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self.value

    def getMinValue(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value


BST1 = BST()
BST1.addList([i for i in range(10)])
print(BST1.find(2))