from 图 import *


def genLegalMoves(x, y, bdsize):  # 定义合法的移动位置，参数（x，y）为当前位置，bdsize为边框大小
    newMvoes = []  # 新的起始点
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2 - 1), (2, 1)]  # 马走日的8个格子

    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdsize) and legalCoord(newY, bdsize):  # 确认不会走出边框
            newMvoes.append((newX, newY))  # 如果没有走出边框，就把相关点添加成新的起始点
    return newMvoes


def legalCoord(x, bdSize):  # 判断是否走出棋盘
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


def posToNodeId(row, col, bdSize):
    return row * bdSize + col


def KnightGraph(bdSize):  # 构建走棋关系图
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph
