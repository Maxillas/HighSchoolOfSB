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
        if searchResult.NodeHasKey is True or searchResult.Node is None:
            return False
        node = BSTNode(key, val, None)
        if searchResult.ToLeft is True:
            searchResult.Node.LeftChild = node
            node.Parent = searchResult.Node
            self.NodeCount += 1
            return
        if searchResult.ToLeft is False:
            searchResult.Node.RightChild = node
            node.Parent = searchResult.Node
            self.NodeCount += 1
            return

    def FinMinMax(self, FromNode, FindMax):
        if FindMax is True:
            if FromNode.RightChild is None:
                return FromNode
            return self.FinMinMax(FromNode.RightChild, True)
        if FindMax is False:
            if FromNode.LeftChild is None:
                return FromNode
            return self.FinMinMax(FromNode.LeftChild, False)

    def DeleteNodeByKey(self, key):
        searchResult = self.FindNodeByKey(key)
        if searchResult.NodeHasKey is False:
            return False

        def find(node):
            if node.LeftChild is None and node.RightChild is None:
                return node
            elif node.LeftChild is None and node.RightChild is not None:
                if node.Parent is not None:
                    node.Parent.LeftChild = node.RightChild
                return node
            else:
                return find(node.LeftChild)

        if searchResult.Node.RightChild is None and searchResult.Node.LeftChild is not None:
            self.Root = searchResult.Node.LeftChild
            self.Root.Parent = None
            return
        insertNode = find(searchResult.Node.RightChild)
        if searchResult.Node.LeftChild is not None:
            insertNode.LeftChild = searchResult.Node.LeftChild
            insertNode.RightChild = searchResult.Node.RightChild
        if searchResult.Node.Parent is not None:
            if searchResult.Node.Parent.LeftChild == searchResult.Node:
                searchResult.Node.Parent.LeftChild = insertNode
            elif searchResult.Node.Parent.RightChild == searchResult.Node:
                searchResult.Node.Parent.RightChild = insertNode
            insertNode.Parent = searchResult.Node.Parent
        else:
            insertNode.Parent.LeftChild = None
            self.Root = insertNode
            self.Root.Parent = None
            self.Root.RightChild = searchResult.Node.RightChild

        searchResult.Node.Parent = None
        searchResult.Node.LeftChild = None
        searchResult.Node.RightChild = None
        self.NodeCount -= 1

    def Count(self):
        return self.NodeCount