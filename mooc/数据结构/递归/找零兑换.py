import time

print(time.process_time())


def recMc(coinValueList, change, knownResults):

    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1

    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMc(coinValueList, change - i,knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins



print(recMc([1, 5, 20,25], 932,[0]*999))
print(time.process_time())
