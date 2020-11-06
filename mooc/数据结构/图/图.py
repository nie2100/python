class Vertex:  # 顶点类
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):  # 添加临接顶点边和权重
        self.connectedTo[nbr] = weight  # 设置到邻接顶点的权重

    def __str__(self):  # 顶点字符串方法
        return str(self.id) + 'connectedTo' + str(x.id for x in self.connectedTo)

    def getConnections(self):  # 所连接的其它顶点
        return self.connectedTo.keys()

    def geId(self):  # 返回自己的key
        return self.id

    def geWeight(self, nbr):  # 返回邻接顶点的权重
        return self.connectedTo[nbr]


class Graph:  # 图类
    def __int__(self):  # 初始化属性
        self.vertList = {}  # 图表
        self.numVertices = 0  # 顶点计数

    def addVertext(self, key):  # 添加顶点方法
        self.numVertices += 1  # 顶点计数加一
        newVertex = Vertex(key)  # 格式化一个顶点
        self.vertList[key] = newVertex  # 添加新的顶点
        return newVertex  # 返回新加顶点

    def getVertex(self, n):  # 通过key查找顶点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):  # x in xx 判断操作
        return item in self.vertList

    def addEdge(self, f, t, const=0):  # 添加边
        if f not in self.vertList:  # 判断f是否在顶点列表里，如果不在添加f为新顶点
            nv = self.addVertext(f)
        if t not in self.vertList:  # 判断t是否在顶点列表中，如果不在，添加t为新顶点
            nv = self.addVertext(t)
        self.vertList[f].addNeighbor(self.vertList[t], const)

    def getVertext(self):  # 把图中的所有顶点用列表的方式返回
        return self.vertList.keys()

    def __iter__(self):  # 可以迭代
        return iter(self.vertList.values())
