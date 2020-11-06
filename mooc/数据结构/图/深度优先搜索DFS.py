def knightTour(n, path, u, limit):  # n：层次;path:路径；u：当前顶点；limit：搜索总深度
    u.setColor('gray', )  # 当前顶点设置成灰色
    path.append(u)  # 将当前顶点加入路径
    if n < limit:  # 如果当前层次小于总深度
        nbrList = list(u.getConnections())  # 对所有合法移动逐一深入
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':  # 选择白色未经过的顶点深入
                done = knightTour(n + 1, path, nbrList[i], limit)  # 层次+1,递归深入
            i += 1
        if not done:  # 如果无法完成总深度，回溯，试本层下一个顶点
            path.pop()
            u.setColor('white')
        else:
            done = True
        return done


def orderByAvaill(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getconnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append(c, v)
        resList.sort(key=lambda x: x[0])#按照列表中数据的第一个元素来排序
        return [y[1] for y in resList]
