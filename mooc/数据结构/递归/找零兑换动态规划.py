def dpMakeChange(coinValueList, change, minCoins,coninUsed):
    for cents in range(1, change + 1):
        coinCount = cents
        newCoin = 1

        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
            minCoins[cents] = coinCount
            coninUsed[cents]= newCoin
    return  minCoins[change]
def printCoins(coinsUsed,change):
    coin = change
    thisCoin = coinsUsed[coin]
    print(thisCoin)
    coin = coin - thisCoin
print(dpMakeChange([1,5,10,21,25,],768,[0]*99999999))