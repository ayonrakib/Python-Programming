# BST
# root node is the parent node
# root node has 2 nodes as child nodes
# both child nodes will be none at init, value will be input at init
# each node has 3 properties: value, leftchild and rightchild
# the lower values nodes will go to left child and higher valued nodes will go to right child
# same value? conflicting answer in google
# methods:
#   insert
#   search
#   modify
#   delete
class Node():
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


    def __str__(self):
        return f"The value of the node is {self.value}"


    # insert
    # input: value as integer
    # return: true if added, no return value if could not add
    # method:
    #   step 1. currentNode = rootNode
    #   step 2. infinite loop:
    #       step1. jodi currentNode.value == value hoy:
    #           step1. return true
    #       step2. jodi value < currentNode.value hoy: 
    #           step1. jodi currentNode.leftChild None na hoy:
    #               step1. currentNode = currentNode.leftChild
    #               step2. currentnode updated, so start the loop again
    #           step2. othoba:
    #               step1. currentNode.leftChild = Node(value)
    #               step2. return true
    #       step3. othoba:
    #           step1. jodi currentNode.rightChild None na hoy:
    #               step1. currentNode = currentNode.rightChild
    #               step2. currentnode updated, so start the loop again
    #           step2. othoba:
    #               step1. currentNode.rightChild = Node(value)
    #               step2. return true
    #   step3. return true
    def insert(self, value):
        currentNode = self
        while(True):
            if currentNode.value == value:
                return True
            if value < currentNode.value:
                if currentNode.leftChild is not None:
                    currentNode = currentNode.leftChild
                    continue
                else:
                    currentNode.leftChild = Node(value)
                    return True
            else:
                if currentNode.rightChild is not None:
                    currentNode = currentNode.rightChild
                    continue
                else:
                    currentNode.rightChild = Node(value)
                    return True


    # delete
    # input: value
    # return: true if deleted, false if could not delete
    # method:
    #   step1. jodi currentNode er left and right child both none hoy:
    #       step1. last node e eshe porsi, value khuje pai nai, return true
    #   step2. jodi rootNode er value = value hoy:
    #       step 1. rootNode.value = none
    #       step 2. true
    #   step3. currentNode = rootNode
    #   step4. infinite loop:
    #       step1. jodi value < currentNode.value hoy:
    #           step1. jodi currentNode.leftChild None na hoy:
    #               step1. jodi currentNode.leftChild.value = value hoy:
    #                   step1. currentNode.leftChild = None
    #                   step2. return True
    #               step2. othoba:
    #                   step 1. currentNode = currentNode.leftChild
    #       step2. othoba:
    #           step1. jodi currentNode.rightChild None na hoy:
    #               step1. jodi currentNode.rightChild.value = value hoy:
    #                   step1. currentNode.rightChild = None
    #                   step2. return True
    #               step2. othoba:
    #                   step 1. currentNode = currentNode.rightChild
    # def delete(self, value):
    #     if self.value == value:
    #         self.value = None
    #         return True
    #     currentNode = self
    #     while(True):
    #         if currentNode.leftChild is None and currentNode.rightChild is None:
    #             return True
    #         if value < currentNode.value:
    #             if currentNode.leftChild is not None:
    #                 if currentNode.leftChild.value == value:
    #                     currentNode.leftChild = None
    #                     return True
    #                 else:
    #                     currentNode = currentNode.leftChild
    #         else:
    #             if currentNode.rightChild is not None:
    #                 if currentNode.rightChild == value:
    #                     currentNode.rightChild = None
    #                     return True
    #                 else:
    #                     currentNode = currentNode.rightChild


    # delete
    # input: value
    # return: true if deleted, nothing if not deleted
    # method:
    #   step1. search the currentNode with value and its parent node and save the return values
    #   eikhane list/tuple akare return korte parbo na, karon duitai replace kortesi na, ekta korbo, so alada alada value return korbo
    #   step2. search the node to replace with and its parent node
    #   step3. establish previousParentNode relation with nodeToBeReplaced node and parentOfNodeToBeReplaced er child none hobe
    def delete(self, value):


rootNode = Node(50)

rootNode.insert(25)
# print(rootNode.leftChild)

rootNode.insert(63)
# print(rootNode.rightChild)

# rootNode.insert(20)
# print(rootNode.leftChild.leftChild)

rootNode.insert(37)
# print(rootNode.leftChild.rightChild)

rootNode.insert(26)
# print(rootNode.leftChild.rightChild.leftChild)

# rootNode.delete(25)
print(rootNode.leftChild)
print(rootNode.leftChild.leftChild)

# rootNode.delete(26)
# print(rootNode.leftChild.rightChild.leftChild)

# rootNode.delete(59)