class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None
        self.NodeCount = 0
        if node is not None:
            self.NodeCount += 1

    def FindNodeByKey(self, key):
        result = BSTFind()
        if self.Root is None:
            return result

        def find(node):
            if key < node.NodeKey:
                if node.LeftChild is None:
                    result.Node = node
                    result.ToLeft = True
                    return
                find(node.LeftChild)
            elif key > node.NodeKey:
                if node.RightChild is None:
                    result.Node = node
                    result.ToLeft = False
                    return
                find(node.RightChild)
            elif key == node.NodeKey:
                result.Node = node
                result.NodeHasKey = True
                return

        find(self.Root)
        return result

    def AddKeyValue(self, key, val):
        searchResult = self.FindNodeByKey(key)
        if searchResult.NodeHasKey is True:
            return False
        node = BSTNode(key, val, None)
        if searchResult.Node is None:
            self.Root = node
            self.NodeCount += 1
            return True
        if searchResult.ToLeft is True:
            searchResult.Node.LeftChild = node
            node.Parent = searchResult.Node
            self.NodeCount += 1
            return True
        if searchResult.ToLeft is False:
            searchResult.Node.RightChild = node
            node.Parent = searchResult.Node
            self.NodeCount += 1
            return True

    def FinMinMax(self, FromNode, FindMax):
        if self.Root is None:
            return None
        if FindMax is True:
            if FromNode.RightChild is None:
                return FromNode
            return self.FinMinMax(FromNode.RightChild, True)
        if FindMax is False:
            if FromNode.LeftChild is None:
                return FromNode
            return self.FinMinMax(FromNode.LeftChild, False)

    def isLeaf(self, node):
        if node.LeftChild is None and node.RightChild is None:
            return True
        return False
    
    def __insertLeftRight(self, nodeDelete, nodeSuccessor):
        if nodeDelete.NodeKey < nodeDelete.Parent.NodeKey:
            nodeDelete.Parent.LeftChild = nodeSuccessor
        else:
            nodeDelete.Parent.RightChild = nodeSuccessor

    def __insert(self, nodeDelete, nodeSuccessor):
        if nodeDelete == self.Root:
            self.Root = nodeSuccessor
            self.Root.Parent = None
        else:
            self.__insertLeftRight(nodeDelete, nodeSuccessor)
            nodeSuccessor.Parent = nodeDelete.Parent
        nodeSuccessor.LeftChild = nodeDelete.LeftChild
        nodeSuccessor.RightChild = nodeDelete.RightChild

    
    def DeleteNodeByKey(self, key):
        deletedNodeSearch = self.FindNodeByKey(key)
        deletedNode = deletedNodeSearch.Node
        # если нет такого значения в дереве
        if deletedNodeSearch.NodeHasKey is False:
            return False
        # если в дереве только один узел
        if self.isLeaf(deletedNode) is True and deletedNode.Parent is None:
            self.Root = None
            self.NodeCount -= 1
            return True
        # если удаляем листок
        if self.isLeaf(deletedNode) is True:
            self.__insertLeftRight(deletedNode, None)
            self.NodeCount -= 1
            return True
        
        if deletedNode.RightChild is None and deletedNode.Parent is None:
            self.Root = deletedNode.LeftChild
            self.Root.Parent = None
            self.NodeCount -= 1
            return True
        insertNode = self.FinMinMax(deletedNode.RightChild, False)

        # если у преемника нет потомков и родитель является удаляемым узлом
        if insertNode.Parent == deletedNode and self.isLeaf(insertNode):
            insertNode.Parent.RightChild = None
            deletedNode.LeftChild.Parent = insertNode
            self.__insert(deletedNode, insertNode)
        # если у преемника нет потомков
        elif insertNode.Parent == deletedNode and not self.isLeaf(insertNode):
            insertNode.Parent.RightChild = insertNode.RightChild
            deletedNode.LeftChild.Parent = insertNode
            self.__insert(deletedNode, insertNode) 
        # если у преемника есть только правый потомок и родитель является удаляемым узлом
        elif self.isLeaf(insertNode):
            insertNode.Parent.LeftChild = None
            deletedNode.RightChild.Parent = insertNode
            deletedNode.LeftChild.Parent = insertNode
            self.__insert(deletedNode, insertNode)
        # если у преемника есть только правый потомок
        elif not self.isLeaf(insertNode):
            deletedNode.LeftChild.Parent = insertNode
            deletedNode.RightChild.Parent = insertNode
            insertNode.Parent.LeftChild = insertNode.RightChild
            insertNode.RightChild.Parent = insertNode.Parent
            self.__insert(deletedNode, insertNode)
        self.NodeCount -= 1
        return True
        
    def Count(self):
        return self.NodeCount
    
    def WideAllNodes(self):
        outputList = []       
        if self.Root is None:
            return () 
        node = self.Root
        childrens = [node]

        while childrens:
            childrensCurrent = []
            for item in childrens:
                outputList.append(item)
                if item.LeftChild:
                    childrensCurrent += [item.LeftChild]
                if item.RightChild:
                    childrensCurrent += [item.RightChild]
            childrens = childrensCurrent

        return tuple(outputList)
    
    def DeepAllNodes(self, typeOfOrder):
        outputList = []
        node = self.Root
        if self.Root is None:
            return ()
        
        def inOrderSearch(node):
            if node.LeftChild is not None:
                inOrderSearch(node.LeftChild)
            outputList.append(node)
            if node.RightChild is not None:
                inOrderSearch(node.RightChild)
        
        def postOrderSearch(node):
            if node.LeftChild is not None:
                postOrderSearch(node.LeftChild)
            if node.RightChild is not None:
                postOrderSearch(node.RightChild)
            outputList.append(node)

        def preOrderSearch(node):
            outputList.append(node)
            if node.LeftChild is not None:
                preOrderSearch(node.LeftChild)
            if node.RightChild is not None:
                preOrderSearch(node.RightChild)
            
        if typeOfOrder == 0:
            inOrderSearch(node)
            return tuple(outputList)
        if typeOfOrder == 1:
            postOrderSearch(node)
            return tuple(outputList)
        if typeOfOrder == 2:
            preOrderSearch(node)
            return tuple(outputList)

#    def Inversion(self):
        # tree = self
        # node = self.Root
        
        # def invers(node):
        #     #print("YAHA", node.NodeKey)
        #     node.LeftChild, node.RightChild = node.RightChild, node.LeftChild

        # def postOrderSearch(node):
        #     #print("gg", node.NodeKey)
        #     if node.LeftChild is not None:
        #         postOrderSearch(node.LeftChild)
        #     if node.RightChild is not None:
        #         postOrderSearch(node.RightChild)
        #     invers(node.Parent)

        # postOrderSearch(node)
       
        # return tree
        