def postortdereval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    res1 = None
    res2 = None
    if tree:
        res1 = postortdereval(tree.getLeftChild())
        res2 = postortdereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res2,re2)
        else:
            return tree.getRootVal()