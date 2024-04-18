class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
		
    def __init__(self):
        self.Root = None # корень дерева
    
    def GenerateTree(self, a):
        orderedMas = a
        orderedMas.sort()
        
        def generator(parent, massive):
            centerIndex = (int)(len(massive) / 2)    
            node = BSTNode(massive[centerIndex], parent)
            if parent is None:
                self.Root = node
                node.Level = 0
            else:
                node.Level = parent.Level + 1       
            if len(massive) > 1:
                leftPart = massive[:centerIndex]
                node.LeftChild = generator(node, leftPart)
                rightPart = massive[centerIndex + 1:]
                node.RightChild = generator(node, rightPart)
            
            return node
        
        generator(None, orderedMas)

    def IsBalanced(self, root_node):
        maxLeftLevel = 0
        maxRightLevel = 0
        def balanced(node):
            rightIsBal = False
            leftIsBal = False
            if node is None:
                return True, 0
            
            rightIsBal, rightMax = balanced(node.RightChild)
            leftIsBal, leftMax = balanced(node.LeftChild)
            
            isBalanced = rightIsBal and leftIsBal and (abs(leftMax - rightMax) <= 1)

            return isBalanced, max(rightMax, leftMax) + 1

        return balanced(root_node)[0]
        
    