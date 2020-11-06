def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])


    merget = []
    print('alist:', alist, "left:", left, 'rigt', right)
    while left and right:
        if left[0] >= right[0]:
            merget.append(right.pop(0))
        else:
            merget.append(left.pop(0))
        print('merget:', merget, 'left', left, 'right', right)
    merget.extend(left if left else right)
    print('merget组合后：', merget)
    print('___________________________________________________')

    return merget


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

mergeSort(alist)
