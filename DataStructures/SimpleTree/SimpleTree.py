class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is None:
            return
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        NodeToDelete.Children.clear()

    def GetAllNodes(self):
        outputList = []

        def findNode(node):
            outputList.append(node)
            if len(node.Children) == 0:
                return outputList
            for item in node.Children:
                outputList + findNode(item)
            return outputList

        outputList + findNode(self.Root)
        return outputList

    def FindNodesByValue(self, val):
        outputList = []
        for item in self.GetAllNodes():
            if item.NodeValue == val:
                outputList.append(item)
        return outputList

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode.Parent is None:
            return
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        count = 0
        for item in self.GetAllNodes():
            if len(item.Children) == 0:
                count += 1
        return count