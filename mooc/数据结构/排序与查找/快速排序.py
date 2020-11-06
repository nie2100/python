def quickSort(alist):
    quikSortHelper(alist, 0, len(alist) - 1)



def partition(alist, first, last):
    print(alist)
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        if leftmark > rightmark:
            done = True

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1

        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


def quikSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quikSortHelper(alist, first, splitpoint - 1)
        quikSortHelper(alist, splitpoint + 1, last)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

quickSort(alist)
