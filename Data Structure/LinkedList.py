# linked list
# used for storing data and searching data fast
# every node is an object with 2 properties: value and mextNode
# value is the integer value, nextNode is the next node which points to the next node in the chain
# many methods: insert, modify, delete
from operator import truediv
from platform import node
from tkinter.messagebox import NO


class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.nextNode= None


class LinkedList():
    def __init__(self) -> None:
        self.head = None


    def __str__(self) -> str:
        return f"The value of the head node is: {self.value}"



    # insert node at beginning
    # input: value
    # return: true if added, false if not
    # method:
    #   1. jodi input int na hoy:
    #       1.1. raise exception
    #   2. jodi head none hoy:
    #       2.1. head obj hobe input diye banano node
    #   3. noile:
    #       3.1. current node hobe input diye banano node
    #       3.2. current node er next node hobe head node
    #   4. return true
    def insertNodeAtBeginning(self, value):
        if type(value) != int:
            raise Exception("input has to be integer!")
        if self.head is None:
            self.head = Node(value)
        else:
            node = Node(value)
            node.nextNode = self.head
            self.head = node
        # print("head node is: ",self.head.value)
        # print("next of head is: ",self.head.nextNode.value)
        # print("next of head is: ",self.head.nextNode.nextNode.value)
        return True


    # insert node at end
    # input: value
    # return: true if inserted, false if not
    # method:
    #   1. input int na hoile exception throw
    #   2. input diye node banabo
    #   3. jodi head none hoy:
    #       3.1. head hobe node
    #   4. currentNode hobe head
    #   5. jotokkhon na porjonto current node none na hocche:
    #       5.1. currentNode hobe current node er next node
    #   6. current Node er next node hobe input diye banano node
    #   7. return true
    def insertNodeAtEnd(self, value):
        if type(value) != int:
            raise Exception("input must be an integer!")
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while(currentNode.nextNode is not None):
                currentNode = currentNode.nextNode
            currentNode.nextNode = node
        return True


    # print linked list
    # input: self object
    # return: string of all values of nodes
    # method:
    #   1. jodi head none hoy:
    #       1.1. eturn empty linked list str
    #   2. return str empty str
    #   3. current node hobe head obj
    #   4. jotokkhon na current node er next node none na hocche:
    #       4.1. return str er sathe append current node er value
    #       4.2. current node hobe current node er next ndoe
    #   5. return return str
    def returnLinkedListValuesInString(self):
        if self.head is None:
            return "The linked list is empty!"
        returnString = ""
        currentNode = self.head
        while(currentNode is not None):
            returnString += f"The value of the current node is: {currentNode.value} \n"
            currentNode = currentNode.nextNode
        returnString += "end of linked list"
        return returnString


    # update node
    # method: previous value, new value
    # retrun: true if updated, false if not found
    # method:
    #   1.  jodi self head node none hoy:
    #       1.1. return false
    #   2. current node hobe self head node
    #   3. jodi current node none na hoy:
    #       3.1. jodi current node er value previous value er soman hoy:
    #           3.1.1. current node er value updated with new value
    #           3.1.2. return true
    #       3.2. current node hobe current node er next node
    #   4. return fale
    def update(self, previousValue, newValue):
        if self.head is None:
            return False
        if type(previousValue) != int:
            raise Exception("previous value has to be integer!")
        if type(newValue) != int:
            raise Exception("new value has to be integer!")
        currentNode = self.head
        while(currentNode is not None):
            if currentNode.value == previousValue:
                currentNode.value = newValue
                return True
            currentNode = currentNode.nextNode
        return False


    # delete
    # input: value
    # return: true if deleted, false if not
    # method:
    #   1. jodi self head node none hoy:
    #       1.1. return false
    #   2. current node hobe self head node
    #   3. jotokkhon na current node none na hocche:
    #       3.1. jodi current node er next node er value value er soman hoy:
    #       3.2. previous node hobe current node
    #       3.3. node to delete hobe current node er next node
    #       3.4. next node hobe current node er next node er next node
    #       3.5. previous node er next node hobe next node
    #       3.6. return true
    def delete(self, value):
        previousNode = self.getPreviousNode(value)
        nextNode = self.getNextNode(value)
        if previousNode is not None and nextNode is not None:
            previousNode.nextNode = nextNode
            return True
        return False


    # get node
    # input: value
    # return: node if found, none if not
    # method:
    #   1. jodi value int na hoy:
    #       1.1. raise exception
    #   2. current node hobe self head obj
    #   3. jotokkhon na current node none hocche:
    #       3.1. jodi current node er value input er soman hoy:
    #           3.1.1. return current node obj
    #       3.2. current node hobe current node er next node
    #   4. return false
    def getNode(self, value):
        if type(value) != int:
            raise Exception("value must be integer!")
        currentNode = self.head
        while(currentNode is not None):
            if currentNode.value == value:
                return currentNode
            currentNode = currentNode.nextNode
        return False

        
    # get previous node
    # input: value
    # return: node obj if found, none if not
    # method:
    #   1. jodi value int na hoy:
    #       1.1. raise exception
    #   2. current node hobe self head node
    #   3. previous node empty str
    #   4. jotokkhon na current node none na hocche:
    #       4.1. jodi current node er next node none na hoy and current node er next node er value input value er soman hoy:
    #           4.1.1. return current node
    #       4.2. current node hobe current node er next node
    #   5. return none
    def getPreviousNode(self, value):
        if type(value) != int:
            raise Exception("input value must be integer!")
        currentNode = self.head
        while(currentNode is not None):
            if currentNode.nextNode is not None and currentNode.nextNode.value == value:
                return currentNode
            currentNode = currentNode.nextNode
        return None


    # get next node
    # input: value
    # return: next node of the value if found, none if not
    # method:
    #   1. jodi input value int na hoy:
    #       1.1. raise exception
    #   2. current node self head
    #   3. jotokkhon na current node none hocche:
    #       3.1. jodi current node er next node none na hoy and current node er value input value er soman hoy:
    #           3.1.1. return current node er next node
    #       3.2. current node hobe current node er next node
    #   4. return none
    def getNextNode(self, value):
        if type(value) != int:
            raise Exception("value must be integer!")
        currentNode = self.head
        while(currentNode is not None):
            if currentNode.nextNode is not None and currentNode.value == value:
                return currentNode.nextNode
            currentNode = currentNode.nextNode
        return False


head = LinkedList()
head.insertNodeAtEnd(1)
head.insertNodeAtEnd(2)
head.insertNodeAtEnd(3)
head.insertNodeAtBeginning(4)
head.insertNodeAtBeginning(5)
# head.update(2,6)
node = head.getPreviousNode(2)
print(node.value)
node = head.getNextNode(2)
print(node.value)
print(head.returnLinkedListValuesInString())

# 1. head = LinkedList()
# 2. self.head  = None
# 3. head.insert(1)
#   3.1. value = 1
#   3.2. if type(value) != int:
#   3.3. node = Node(value)
#   3.4. node = Node(1)
#   3.5. node = x123
#   3.6. if self.head is None:
#       3.6.1. self.head = node
#       3.6.2. self.head = x123
#       3.6.3. currentNode = x123
#   3.7. return true
# 4. head.insert(2)
#   3.1. value = 2
#   3.2. if type(value) != int:
#   3.3. node = Node(value)
#   3.4. node = Node(2)
#   3.5. node = y456
#   3.6. if self.head is None:
#   3.7. else:
#       3.7.1. currentNode = self.head
#       3.7.2. currentNode = x123
#       3.7.3. while(currentNode.nextNode is not None):
#       3.7.4. loop 1: 
#           3.7.4.1. currentNode.nextNode = x123.nextNode = none
#       3.7.5. currentNode.nextNode = node
#       3.7.6. currentNode.nextNode = y456
#   3.8. return true
# 5. print(head.returnLinkedListValuesInString())
# 6. if self.head is None:
# 7. if x123 is None:
# 8. returnString = ""
# 9. currentNode = self.head
# 10. currentNode = x123
# 11. while(currentNode.nextNode is not None):
#   11.1. loop1: 
#       11.1.1. currentNode.nextNode is not None
#       11.1.2. x123.nextNode is not None
#       11.1.3. y456 is not None:
#           11.1.4. returnString += f"The value of the current node is: {currentNode.value} \n"
#           11.1.5. returnString += "The value of the current node is: 1 \n"
#           11.1.6. currentNode = currentNode.nextNode
#           11.1.7. currentNode = x123.nextNode
#           11.1.8. currentNode = y456
#   11.2. loop2:
#       11.2.1. currentNode.nextNode is not None
#       11.2.2. 
