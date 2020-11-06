from Queue import Queue


def hotPotato(namelist, numb):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.sieze() > 1:
        for i in range(numb):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()


print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 100))
