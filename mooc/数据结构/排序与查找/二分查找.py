def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    fund = False
    while first <= last and not fund:
        mindpoint = (first + last )/ 2
        if list[mindpoint] == item:
            fund = True
        else:
            if item < list[mindpoint]:
                last = mindpoint - 1
            else:
                first = mindpoint + 1
    return fund
