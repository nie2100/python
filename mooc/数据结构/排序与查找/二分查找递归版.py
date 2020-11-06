def binarySearch(list, item):
    if len(list) == 0:
        return False
    else:
        mindpoint = len(list) / 2
        if list[mindpoint] == item:
            return True
        else:
            if item < list[mindpoint]:
               return binarySearch(list[:mindpoint],item)
            else:
                return binarySearch(list[mindpoint+1:],item)