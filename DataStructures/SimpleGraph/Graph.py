class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        output = []
        node = self.head
        while node is not None:
            if node.value == val:
                output.append(node)
            node = node.next
        return output

    def delete(self, val, all=False):
        node = self.head
        prev_node = None

        while node is not None:
            if node.value == val:
                if prev_node is None:
                    self.head = self.head.next
                    if self.head is None:
                        self.tail = None
                    if all is False:
                        if self.head is not None and self.head.next is None:
                            self.tail = self.head
                        node.next = None
                        break
                    else:
                        temp = node.next
                        node.next = None
                        node = temp
                        if self.head is not None and self.head.next is None:
                            self.tail = self.head
                        continue
                else:
                    prev_node.next = node.next
                    if all is False:
                        if node.next is None:
                            self.tail = prev_node
                        node.next = None
                        break
                    elif node.next is not None and node.next.value == val:
                        node = node.next
                        continue
                if node.next is None:
                    self.tail = prev_node
            prev_node = node
            node = node.next

    def clean(self):
        node = self.head
        while node is not None:
            temp = node.next
            node.next = None
            node = temp
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        output = 0
        while node is not None:
            output += 1
            node = node.next
        return output

    def insert(self, afterNode, newNode):
        if afterNode is None:
            node = self.head
            self.head = newNode
            newNode.next = node
            if self.head.next is None:
                self.tail = self.head

        else:
            node = afterNode.next
            afterNode.next = newNode
            newNode.next = node
            if node is None and self.head is not None:
                self.tail = newNode

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        node = Node(item)
        self.queue.add_in_tail(node)

    def dequeue(self):
        if self.queue.len() == 0:
            return None
        else:
            temp = self.queue.head.value
            self.queue.delete(temp)
            return temp

    def size(self):
        return self.queue.len()


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        #self.stack = Stack()
        self.queue = Queue()

    def AddVertex(self, v):
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return
        return
        # здесь и далее, параметры v -- индекс вершины
        # в списке  vertex
    def clearAdjancy(self):
        for i in range(self.max_vertex - 1):
            self.m_adjacency[1][i] = 0
            self.m_adjacency[i][1] = 0

    def RemoveVertex(self, v):
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                continue
            if self.vertex[i].Value == v:
                self.vertex[i] = None
                self.clearAdjancy()
        # ваш код удаления вершины со всеми её рёбрами

    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] == 1:
            return True
        return False
        # True если есть ребро между вершинами v1 и v2

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        # удаление ребра между вершинами v1 и v2
        pass

    def clearStack(self):
        i = self.stack.pop()
        while i != None:
            i = self.stack.pop()
            continue

    def clearHit(self):
        for i in self.vertex:
            i.hit = False

    def searchTargetInSelf(self, startIndex):
        for index in range(len(self.m_adjacency[startIndex])):
            if self.vertex[index].hit is False:
                return index
        return None

    def searchVertex(self, startIndex, endIndex):
        for i in range(len(self.m_adjacency[startIndex])):
            if self.m_adjacency[startIndex][endIndex] == 1:
                return True
        return False

    # def DepthSearch(self, startIndex, endIndex):
    #     currentVertexIndex = startIndex
    #     while True:
    #         self.vertex[currentVertexIndex].hit = True
    #         self.stack.push(currentVertexIndex)
    #         while True:
    #             if self.searchVertex(currentVertexIndex, endIndex):
    #                 self.stack.push(endIndex)
    #                 return self.stack
    #             currentVertexIndex = self.searchTargetInSelf(currentVertexIndex)
    #
    #             if currentVertexIndex is not None and currentVertexIndex <= endIndex:
    #                 break
    #             self.stack.pop()
    #             if self.stack.size() == 0:
    #                 #print("path not found")
    #                 return #path not found
    #             currentVertexIndex = self.stack.pop()
    #             self.vertex[currentVertexIndex].hit = True

    # def DepthFirstSearch(self, startIndex, endIndex):
    #     self.clearStack()
    #     self.clearHit()
    #     result = self.DepthSearch(startIndex, endIndex)
    #     if result is None:
    #         return []
    #     outputList = []
    #     resultElement = 1
    #     while True:
    #         resultElement = result.pop()
    #         if resultElement is None:
    #             break
    #         outputList.append(self.vertex[resultElement])
    #     outputList.reverse()
    #
    #     return outputList

    def SearchUnvisitedFriend(self, startIndex):
        for index in range(len(self.m_adjacency[startIndex])):
            if self.vertex[index].hit is False and self.searchVertex(startIndex, index):
                return index
        return None

    def clearQueue(self):
        i = self.queue.dequeue()
        while i != None:
            i = self.queue.dequeue()

    def BreadthFirstSearch(self, startIndex, endIndex):
        self.clearQueue()
        self.clearHit()
        currentVertexIndex = startIndex
        self.vertex[currentVertexIndex].hit = True
        path = []
        while True:
            temp = currentVertexIndex
            secondVertexIndex = self.SearchUnvisitedFriend(currentVertexIndex)

            if secondVertexIndex == endIndex and self.searchVertex(currentVertexIndex, secondVertexIndex):
                if len(path) == 0:
                    path.append(self.vertex[temp])
                path.append(self.vertex[secondVertexIndex])
                return path
            elif secondVertexIndex is None:
                if self.queue.size() == 0:
                    return []  # path not found
                currentVertexIndex = self.queue.dequeue()
                if len(path) == 0:
                    path.append(self.vertex[temp])
                path.append(self.vertex[currentVertexIndex])
                continue
            self.vertex[secondVertexIndex].hit = True
            self.queue.enqueue(secondVertexIndex)



