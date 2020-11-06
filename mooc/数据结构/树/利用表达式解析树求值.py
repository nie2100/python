import operator


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    lefC = parseTree.getLeftChild()
    rightC = parseTree.getRithtChild()

    if lefC and rightC:
       fn = opers[parseTree.getRootVal()]
       return fn(evaluate(lefC),evaluate(rightC))
    else:
        return parseTree.getRootVal()