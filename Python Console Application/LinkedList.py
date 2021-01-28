from random import randint
class Node():
    def __init__(self,value):
        self.value = value
        self.nextElement = None

# random value linked list generate
# method: random number linked list
# input: firstNode
# return: firsnothingtNode
# method:
#   list = []
#   firstNode = Node(10)
#   list.append(firstNode.value)
#   currentNode = firstNode
#   while(True):
#       if getLinkedListLength(firstNode) == length:
#           break
#       random value generate korbo
#       if value not in list:
#           nextNode = Node(value)
#           currentNode.nextElement = nextNode
#           currentNode = currentNode.nextElement
#   return firstNode
def randomNumberLinkedList(length):
    list = []
    firstNode = Node(10)
    list.append(firstNode.value)
    currentNode = firstNode
    while(True):
        if getLinkedListLength(firstNode) == length:
            break
        value = randint(0,10)
        if value not in list:
            list.append(value)
            nextNode = Node(value)
            currentNode.nextElement = nextNode
            currentNode = currentNode.nextElement
    return firstNode

# print linked list values
# input: firstnode
# return: print all values of nodes
# method:
#   infinite loop:
#       if firstNode.nextElement is not None:
#           print(firstNode.value)
#       else:
#           break
def getLinkedListValues(firstNode):
    while(True):
        print(firstNode.value)
        if firstNode.nextElement is not None:
            firstNode = firstNode.nextElement
        else:
            break

# print linked list length
# input: firstNode
# return: length in integer
# method:
#   length = 1
#   infinite loop:
#       if firstNode.nextElement is not None:
#           length += 1
#           firstNode = firstNode.nextElement
#       else:
#           return length
def getLinkedListLength(firstNode):
    length = 1
    while(True):
        if firstNode.nextElement is not None:
            length += 1
            firstNode = firstNode.nextElement
        else:
            return length

# getNode
# input: firstNode, index
# return: value in integer
# method:
#   if index > firstNode length:
#       raise Exception('index cannot be greater than linked list length!')
#   if index < 0:
#       raise Exception('index cannot be negative!')
#   linkedListLength = getLinkedListLength(firstNode)
#   currentNode = firstNode
#   for number in range(linkedListLength):
#       if index == number+1:
#           return currentNode
#       else:
#           currentNode = currentNode.nextElement

def getNode(firstNode,index):
    if index > getLinkedListLength(firstNode):
        raise Exception('index cannot be greater than linked list length!')
    if index < 0:
        raise Exception('index cannot be negative!')
    linkedListLength = getLinkedListLength(firstNode)
    currentNode = firstNode
    for number in range(linkedListLength):
        if index == number+1:
            return currentNode
        else:
            currentNode = currentNode.nextElement

# def get specific node value
# input: firstNode, index
# return: value as integer
# method:
#   if index > firstNode length:
#       raise Exception('index cannot be greater than linked list length!')
#   if index < 0:
#       raise Exception('index cannot be negative!')
#   linkedListLength = getLinkedListLength(firstNode)
#   currentNode = firstNode
#   for number in range(linkedListLength):
#       if index == number+1:
#           return currentNode.value
#       else:
#           currentNode = currentNode.nextElement
def getSpecificNodeValue(firstNode,index):
    if index > getLinkedListLength(firstNode):
        raise Exception('index cannot be greater than linked list length!')
    if index < 0:
        raise Exception('index cannot be negative!')
    linkedListLength = getLinkedListLength(firstNode)
    currentNode = firstNode
    for number in range(linkedListLength):
        if index == number+1:
            return currentNode.value
        else:
            currentNode = currentNode.nextElement

# insert node after specific index
# input: firstNode, targetNode, index
# output: firstNode
# method:
#   if index > size of linked list(firstnode):
#       raise Exception
#   if index is not integer:
#       raise Exception
#   if index < 0:
#       raise Exception
#   if index == size of linked list:
#       currentNode = getNode(firstNode, index)
#       currentNode.nextElement = targetNode
#       return firstNode
#   currentNode = getNode(firstNode,index)
#   nextNode = getNode(firstNode, index+1)
#   currentNode.nextElement = targetNode
#   targetNode.nextElement = nextNode
#   return firstNode

def insertNodeAfterSpecificIndex(firstNode, targetNode, index):
    if index > getLinkedListLength(firstNode):
        raise Exception('index cannot be higher than linked list size.')
    if type(index) != int:
        raise Exception('index has to be integer.')
    if index < 1:
        raise Exception('index has to be more than 0.')
    if index == getLinkedListLength(firstNode):
        currentNode = getNode(firstNode, index)
        currentNode.nextElement = targetNode
        return firstNode
    currentNode = getNode(firstNode,index)
    nextNode = getNode(firstNode, index+1)
    currentNode.nextElement = targetNode
    targetNode.nextElement = nextNode
    return firstNode

# insert node before a specific index
# input: firstNode, targetNode, index
# return: firstNode
# method:
#   if index < 0:
#       raise Exception
#   if type(index) != int:
#       raise Exception()
#   if index > size of linked list:
#       raise Exception()
#   if index == 1:
#       targetNode.nextElement = firstNode
#       return targetNode
#   previousNode = getNode(firstNode, index-1)
#   currentNode = getNode(firstNode, index)
#   previousNode.nextElement = targetNode
#   targetNode.nextElement = currentNode
#   return firstNode

def insertNodeBeforeSpecificIndex(firstNode,targetNode, index):
    if index < 0:
        raise Exception('index cannot be negative')
    if type(index) != int:
        raise Exception('index has to be integer')
    if index > getLinkedListLength(firstNode):
        raise Exception('index cannot be greater than linked list length.')
    if index == 1:
        targetNode.nextElement = firstNode
        return targetNode
    previousNode = getNode(firstNode,index-1)
    currentNode = getNode(firstNode,index)
    previousNode.nextElement = targetNode
    targetNode.nextElement = currentNode
    return firstNode

# check if value exists in Linked List
# input: firstNode, value
# return: boolean
# method:
#   if getLength(firstNode) == 1:
#       if value == firstNode.value:
#           return True
#       return False
#   while(True):
#       if firstNode.nextElement is not None:
#           if value != firstNode.nextElement.value:
#               firstNode = firstNode.nextElement
#           else:
#               return True
#       else:
#           return False

def checkIfValueExistsInLinkedList(firstNode, value):
    if getLinkedListLength(firstNode) == 1:
        if value == firstNode.value:
            return True
        return False
    while(True):
        if firstNode.nextElement is not None:
            if value == firstNode.value:
                return True
            else:
                firstNode = firstNode.nextElement
        else:
            return False
firstNode = randomNumberLinkedList(4)
getLinkedListValues(firstNode)
print('linked list length: ',getLinkedListLength(firstNode))
print('getnode:',getNode(firstNode,1))
print('getnodevalue:',getSpecificNodeValue(firstNode,1))
targetNode = Node(986)
modifiedNode = insertNodeBeforeSpecificIndex(firstNode, targetNode,3)
getLinkedListValues(modifiedNode)
print('')
targetNode = Node(986)
node = insertNodeAfterSpecificIndex(modifiedNode, targetNode, 1)
getLinkedListValues(node)
print('')
print(checkIfValueExistsInLinkedList(node, 10))