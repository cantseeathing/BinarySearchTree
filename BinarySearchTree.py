from Queue import Queue


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return 'The node has been added successfully!'


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def searchBST(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print('The value is found!')
    else:
        try:
            if nodeValue < rootNode.data:
                if rootNode.leftChild.data == nodeValue:
                    print('The value is found')
                else:
                    searchBST(rootNode.leftChild, nodeValue)
            else:
                if rootNode.rightChild.data == nodeValue:
                    print('The value is found')
                else:
                    searchBST(rootNode.rightChild, nodeValue)
        except AttributeError:
            print('The value is not found')


def minValue(rootNode):
    current = rootNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = minValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


def destroyBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The BST was deleted successfully!'


newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 60))
print(insertNode(newBST, 10))
print(insertNode(newBST, 100))
print(insertNode(newBST, 23))
print(insertNode(newBST, 35))
print(insertNode(newBST, 11))
print(insertNode(newBST, 204))
print(newBST.data)
print(newBST.leftChild.data)

print('------------')
preOrderTraversal(newBST)

print('------------')
inOrderTraversal(newBST)

print('------------')
postOrderTraversal(newBST)

print('------------')
levelOrderTraversal(newBST)

print('------------')
searchBST(newBST, 35)

print('------------')
deleteNode(newBST, 70)
levelOrderTraversal(newBST)

print('------------')
print(destroyBST(newBST))
levelOrderTraversal(newBST)
