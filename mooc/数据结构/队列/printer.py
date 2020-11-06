# -*-coding:utf-8-*-
import random

from Queue import Queue


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度
        self.currentTask = None  # 打印任务
        self.timeRemaining = 0  # 任务倒计时

    def tick(self):  # 打印中，时间减1秒
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):  # 打印忙
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):  # 打印新作业
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time  # 生成时间戳
        self.pages = random.randrange(1, 21)  # 随机生成打印页数

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrinTask():  # 生成作业的概率
    num = random.randrange(1, 181)
    if num == 99:
        return True
    else:
        return False


def simulation(numSecond, pagesPerMinute):  # 模拟

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()

    waitingtimes = []

    for currenSecond in range(numSecond):

        if newPrinTask():  # 时间流逝
            task = Task(currenSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currenSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print('平均等待时间 %6.2f secs %3d 个任务待处理.' % (averageWait, printQueue.sieze()))


for i in range(10):
   simulation(600,3)