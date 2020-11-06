import Queue
from 词梯 import *


def bfs(g, start):  # 两个参数 图和起始顶点
    start.setDistance(0)  # 起始顶点初始为0
    start.setPred(None)  # 前驱初始为None
    vertQueue = Queue()  # 创建队列
    vertQueue.enqueue(start)  # 将初始顶点加入队列
    while (vertQueue.size() > 0):  # 只要队列中还有顶点
        currentVert = vertQueue.dequeue()  # 取队首做当前顶点
        for nbr in currentVert.getConnections():  # 遍历邻接顶点
            if (nbr.getColor() == 'white'):  # 如果邻接顶点式白色
                nbr.setColor('gray')  # 把此邻接顶点设置成灰色
                nbr.setDistance(currentVert.getDistance() + 1)  # 距离+1
                nbr.setPred(currentVert)  # 把前驱设置为此邻接顶点
                vertQueue.enqueue(nbr)  # 把此邻接顶点加入队列
            currentVert.setColor('black')  # 把当前顶点设置成黑色


def traverse(y):  # 回溯函数
    x = y
    while (x.getPre()):
        print(x.getId())
        x = x.getPre()
    print(x.geId())


wordgraph = bulidGraph('forletterwords.txt')
bfs(wordgraph, wordgraph.getVertext('Fool'))
traverse(wordgraph.getVertex('SAGE'))
