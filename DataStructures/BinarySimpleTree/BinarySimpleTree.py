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
            return
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

    def __get_all_nodes(self, node: BSTNode) -> list:
        '''
        Приватный метод рекурсивно проходит по дереву и
        возвращает список всех узлов.
        '''
        nodes = []
        nodes.append(node)
        if node.LeftChild:
            nodes += self.__get_all_nodes(node.LeftChild)
        if node.RightChild:
            nodes += self.__get_all_nodes(node.RightChild)
        return nodes

    def GetAllNodes(self) -> list:
        if not self.Root:
            return []
        return self.__get_all_nodes(self.Root)

    def DeleteNodeByKey(self, key):
        searchResult = self.FindNodeByKey(key)
        if searchResult.NodeHasKey is False:
            return False

        def find(node):
            if node is None:
                return None
            if node.LeftChild is None and node.RightChild is None:
                return node
            elif node.LeftChild is None and node.RightChild is not None:
                #if node.Parent is not None:
                    #node.Parent.LeftChild = node.RightChild
                return node
            else:
                return find(node.LeftChild)

        if searchResult.Node.RightChild is None and searchResult.Node.LeftChild is not None:
            self.Root = searchResult.Node.LeftChild
            self.Root.Parent = None
            self.NodeCount -= 1
            return True
        insertNode = find(searchResult.Node.RightChild)
        if insertNode is None:
            searchResult.Node.Parent.LeftChild = None
            searchResult.Node.Parent = None
            self.NodeCount -= 1
            return True
        if searchResult.Node.LeftChild is not None:
            #insertNode.LeftChild = searchResult.Node.LeftChild
            searchResult.Node.LeftChild.Parent = insertNode
        if searchResult.Node.Parent is not None:
            if searchResult.Node.Parent.LeftChild == searchResult.Node:
                searchResult.Node.Parent.LeftChild = insertNode
            elif searchResult.Node.Parent.RightChild == searchResult.Node:
                searchResult.Node.Parent.RightChild = insertNode
            insertNode.Parent = searchResult.Node.Parent
            if insertNode == searchResult.Node.RightChild:
                insertNode.LeftChild = searchResult.Node.LeftChild
                
        else:

            self.Root = insertNode
            if insertNode == insertNode.Parent.LeftChild:
                if insertNode.LeftChild is not None:
                    insertNode.Parent.LeftChild = insertNode.LeftChild
                    insertNode.LeftChild.Parent = insertNode.Parent
                elif insertNode.RightChild is not None:
                    insertNode.Parent.LeftChild  = insertNode.RightChild
                    insertNode.RightChild.Parent = insertNode.Parent
                else:
                    insertNode.Parent.LeftChild = None
            elif insertNode == insertNode.Parent.RightChild:
                insertNode.LeftChild = searchResult.Node.LeftChild
                searchResult.Node.Parent = None
                searchResult.Node.LeftChild = None
                searchResult.Node.RightChild = None
                self.Root.Parent = None
                self.NodeCount -= 1
                return True
            self.Root.LeftChild = searchResult.Node.LeftChild
            self.Root.LeftChild.Parent = insertNode
            self.Root.RightChild = searchResult.Node.RightChild
            self.Root.RightChild.Parent = insertNode
            self.Root.Parent = None
            #insertNode.Parent.LeftChild = None
            #insertNode.Parent.RightChild = None



        searchResult.Node.Parent = None
        searchResult.Node.LeftChild = None
        searchResult.Node.RightChild = None
        self.NodeCount -= 1
        return True

    def Count(self):
        return self.NodeCount