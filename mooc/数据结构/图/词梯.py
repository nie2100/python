from 图 import *


def bulidGraph(wordFile):  # 创建词图
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')  # 以只读的方式打开文件
    for line in wfile:  # 调用每一行
        word = line[:-1]  # 去掉换行符取值
        for i in range(len(word)):  # 调用单词的每一个字符
            bucket = word[:i] + '_' + word[i + 1:]  # 格式化字符成_XXX或者X_XXX模式
            if bucket in d:  # 判断格式化后的字符是否在字典d内
                d[bucket].append(word)  # 如果在字典d内则将单词word添加到格式化后的键对应的值内
            else:  # 如果不在
                d[bucket] = [word]  # 创建一个新的键值对
    for bucket in d.keys():  # 遍历词典d里每一个键
        for word1 in d[bucket]:  # 遍历键的每一个值
            for word2 in d[bucket]:  # 对比键里的每个值
                if word1 != word2:  # 如果单词有差异
                    g.addEdge(word1, word2)  # 在单词之间创建一个边
    return g  # 返回图g
