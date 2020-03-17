import random 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def tranverse(self):
        if self.left == None:
            print(self.value)
        else:
            self.left.tranverse()
            print(self.value)
        if self.right != None:
            self.right.tranverse()

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def tranverse(self):
        self.root.tranverse()

    def structure(self, bfsList = [], layer = 0):
        if layer == 0:
            if self.root == None:
                print("Tree is empty.")
                return 0
            else:
                bfsList.append(self.root)

        nodeList = len(bfsList)
        tempString = ''
        for i in range(0, nodeList):
            if bfsList[0].left == None and bfsList[0].right == None:
                if i == nodeList-1:
                    tempString += str(bfsList[0].value)
                else:
                    tempString += str(bfsList[0].value) + ", "
            else:
                if bfsList[0].left != None:
                    bfsList.append(bfsList[0].left)
                if bfsList[0].right != None:
                    bfsList.append(bfsList[0].right)

                if i == nodeList-1:
                    tempString += str(bfsList[0].value)
                else:
                    tempString += str(bfsList[0].value) + ", "
            bfsList.pop(0)

        print("Layer " + str(layer) + ": " + tempString)
        layer += 1
        if len(bfsList) != 0:
            self.structure(bfsList, layer)

# Initialization of the Binary Tree
binary_tree = BinaryTree()

# Test random values
tempString = 'Random numbers inserted into tree: \n'
for i in range(0, 10):
    num = random.randint(0, 100)
    binary_tree.insert(num)
    if i != 4:
        tempString += str(num) + ', '
    else:
        tempString += str(num)
print(tempString + "\n")

print("Tranverse tree using DFS (Depth-first search):\nIn-order (LNR):")
binary_tree.tranverse()

print("\nTree structure using BFS (Breadth-first search):")
binary_tree.structure()