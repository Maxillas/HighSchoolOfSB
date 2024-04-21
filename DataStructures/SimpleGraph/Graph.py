class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return
        return
        # здесь и далее, параметры v -- индекс вершины
        # в списке  vertex

    def RemoveVertex(self, v):
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                continue
            if self.vertex[i].Value == v:
                self.vertex[i] = None
                for i in range(self.max_vertex - 1):
                    self.m_adjacency[1][i] = 0
                    self.m_adjacency[i][1] = 0
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
